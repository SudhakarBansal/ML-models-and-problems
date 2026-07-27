# Movie Recommendation System — Writeup

A top-N movie recommender on **MovieLens 25M** built around **Weighted Matrix Factorization
(Hu, Koren & Volinsky 2008)**, implemented both **from scratch (NumPy ALS)** and via the
`implicit` library, with a **content-based cold-start** extension using TMDB metadata.

This doc is the defensible summary of *what* was built, *why* each choice was made, and the
*honest limitations* — i.e. exactly what an interviewer will probe.

---

## 1. Problem framing

- **Task: top-N ranking**, not rating prediction. Modern systems decide *what to show*, not
  *what star you'd give* — so the metric is ranking quality, not RMSE.
- **Implicit feedback**: MovieLens has explicit 1–5 stars, but I treat every observed rating as a
  *positive interaction* (`p_ui = 1`) and use the rating value as a **confidence** weight
  `C_ui = 1 + alpha * r_ui`. A 5-star rating is a more confident positive than a 3-star one.
  This is the Hu/Koren/Volinsky formulation for implicit data.

## 2. Pipeline (notebooks)

| nb | What | Data |
|----|------|------|
| 01 | Data exploration (rating dist, sparsity, cold-start counts) | 25M |
| 02 | Filter consensus-bad movies → implicit confidence matrix → leave-one-out split → save artifacts | 25M |
| 03 | He-et-al. eval harness + popularity baseline | 25M |
| 04 | **WMF from scratch (ALS, NumPy)** + match vs `implicit` | 15K-user subsample |
| 05 | `implicit` ALS (WMF) + Surprise SVD benchmark | 25M / 2M |
| 06 | **Item cold-start** via TMDB content → latent projection | TMDB subset |
| 07 | Consolidated comparison + findings | — |

Shared logic (split, evaluation protocol, scoring) lives in `recsys_utils.py` so every model is
judged identically.

## 3. Key design decisions

- **Item filter**: drop movies where ≥80% of ratings are below 2.5 (consensus-bad → never worth
  recommending). Polarized movies are kept — learning *who* likes them is the model's job. (~3.6K of
  59K movies dropped.)
- **Split**: leave-one-out per user, holding out the **most recent** rating (predict the *next*
  interaction, the realistic task).
- **Evaluation (He et al., NCF 2017)**: rank the 1 held-out positive against **99 sampled negatives**
  the user never interacted with. `Recall@10 = Hit@10` (single relevant item); `NDCG@10` rewards
  ranking it higher. The candidate set is built once and reused by every model → fair comparison.
- **ALS over SGD** for the from-scratch model: closed-form per-vector updates, no learning rate,
  matches the original paper, and is the industry-standard solver for WMF.

## 4. Results (Recall@10 / NDCG@10)

| Model | Recall@10 | NDCG@10 | Notes |
|---|---|---|---|
| Popularity baseline (25M) | 0.925 | 0.661 | high — sampled-negative artifact |
| Surprise SVD (2M sample) | 0.514 | 0.307 | optimizes RMSE, not ranking |
| **implicit ALS / WMF (25M)** | **0.971** | **0.810** | best; +22.6% NDCG over baseline |
| WMF from scratch (15K users) | 0.926 | 0.697 | matches library (0.928/0.696) ✓ |
| Cold-start: content projection | 0.385 | 0.201 | vs ~0.10 random |

**Readings:**
1. WMF clearly beats popularity on the personalized metric (NDCG 0.81 vs 0.66).
2. The **from-scratch ALS matches the library to within 0.002** on identical data — the HKV
   closed-form update is implemented correctly.
3. **Surprise SVD loses to popularity**: it optimizes rating prediction (RMSE), not ranking. The
   *task framing* matters more than the algorithm choice.
4. **Cold-start**: projecting TMDB content (genres + keywords, TF-IDF → Ridge → latent space) takes
   brand-new, zero-interaction movies from ~0.10 (random) to 0.385 Recall@10. Plain CF can't rank
   them at all.

## 5. The cold-start method (nb 06)

CF has no vector for a movie with zero interactions. So: train WMF on **warm** movies to get their
latent vectors, then fit a **Ridge regression** from each warm movie's TMDB content features to its
learned latent vector. For a **cold** movie, run its content features through that regression to
*predict* a latent vector — now it can be scored against users. Held-out cold movies are ranked
~3.8× better than a no-content baseline. (Train R² to the latent space is a modest ~0.15: content is
a weak proxy for collaborative signal, but enough to beat random by a wide margin.)

## 5b. Reality check — sampled metrics are inflated (important)

The headline numbers above use the He-et-al. **sampled** protocol: rank the true item vs only **99
random negatives**. Those negatives are almost all obscure movies, while the held-out item is one the
user actually watched (usually popular) — so it wins easily. That's why even *popularity* scores 0.92.

To check whether the high numbers were real or an artifact, I re-ran evaluation as **full ranking** —
true item vs **all 55,413 movies** (masking already-seen), on a 5,000-user sample:

| Protocol | Recall@10 | NDCG@10 |
|---|---|---|
| Sampled (99 negatives) | 0.97 | 0.81 |
| **Full ranking (all items)** | **0.048** | **0.022** |

Same model, same code — the gap is entirely the protocol's difficulty. The ~5% full-ranking Recall@10
is the *realistic* MovieLens figure. **Takeaway:** absolute sampled numbers aren't trustworthy in
isolation (a known result — Rendle et al., 2020, "On Sampled Metrics for Item Recommendation"); the
meaningful signals are (a) the **gap between models** and (b) the **full-ranking** number. I report
the sampled metric because it's the standard paper protocol and fair for *comparing* models, but I
don't read its absolute value as "97% good."

## 6. Honest limitations

- **Offline sampled metrics**, not an online A/B test (the real production signal). Sampled-negative
  metrics flatter every model (popularity hits 0.92); the honest signal is the *gap* between models,
  and full ranking (~0.05 Recall@10) is the honest absolute measure (see §5b).
- **From-scratch ALS** validated on a 15K-user subsample — a pure-NumPy per-user loop doesn't scale
  to 162K users; the library (multithreaded C++) handles full 25M.
- **Single split**, no hyperparameter sweep on factors / alpha / regularization.

## 7. Where this goes next → reinforcement learning

This recommender is **static**: train once, serve the same scores. The real product question is
**sequential** — which item to show *now* to maximize long-run engagement, learning online from
each interaction. That reframes recommendation as a **contextual bandit**: context = user features
/ history, arm = candidate item, reward = engagement, balancing **exploration** of new items against
**exploitation** of known-good ones. When longer-term effects matter (don't over-recommend, sequence
content over time) it extends to full RL with the user's engagement state. The matrix-factorization
embeddings here become the *features* such a policy conditions on.

---

## Reproducing

Environment: `/.venv` (Python 3.13) with `numpy, pandas, scipy, scikit-learn, implicit,
scikit-surprise, nbformat, nbclient`.

Run order: `02 → 03 → 05` (full 25M), then `04` and `06` (self-contained subsamples), then `07`.
Notebooks were generated/executed by the `_build_nb*.py` scripts in the project root; the shared
logic is in `recsys_utils.py`.

# Recommendation System — How to Proceed Next

**Updated May 16, 2026** based on our scoping conversation. All 14 strategic decisions are locked in Section 1. The only open item is one implementation-level choice (Section 2: ALS vs SGD optimizer), to be decided at the implementation step in Week 1.

---

## 1. Locked decisions (final)

| # | Decision | Locked answer |
|---|---|---|
| 1 | **Task type** | Top-N ranking (NOT rating prediction) |
| 2 | **Algorithm to build from scratch** | Matrix factorization with weighted-positives loss |
| 3 | **Loss formulation** | Weighted Matrix Factorization (WMF), per Hu, Koren, Volinsky 2008 |
| 4 | **Failure mode to attack** | Cold start (both new-user and new-item) |
| 5 | **Rating → implicit conversion (item-side filter)** | Drop movies where ≥ 80% of raters gave < 2.5 stars (consensus-bad items only). Polarized movies stay — the model handles them. |
| 6 | **Rating → implicit conversion (per-interaction weight)** | All remaining user-movie interactions are positives, weighted by the rating value (5 = strong positive, 2 = weak positive). |
| 7 | **Dataset** | MovieLens 25M + TMDB metadata joined via `links.csv` |
| 8 | **Library for comparison** | `implicit` library (has WMF native), plus Surprise as a secondary classical comparison |
| 9 | **New-item filter handling** | Impute mean rating for filter check — new movies always pass the filter and reach the model |
| 10 | **Train/val/test split** | Leave-one-out per user (standard top-N ranking protocol) |
| 11 | **Primary ranking metric** | NDCG@10 primary, Recall@10 secondary |
| 12 | **Negative sampling at evaluation** | 99 random unseen items + held-out true item; check if true item ranks in top-10 (He et al. NCF protocol) |
| 13 | **New-item cold-start MODEL strategy** | Content-based embedding via TMDB features. Encode each new movie's features into a vector, learn a projection that maps this into the WMF item-embedding space. Trained on movies that exist in BOTH ml-25m and TMDB; applied to new movies at inference. |
| 14 | **Filter threshold tuning** | Empirical — decide concrete numbers after loading data and inspecting the consensus-rating distribution. Aim for 1-5% of catalog filtered. |

---

## 2. Implementation choice (not strategic — decide when at the step)

**Optimizer for from-scratch WMF.** The Hu/Koren/Volinsky 2008 paper uses **ALS (Alternating Least Squares)**, not SGD. Decision needed when you reach Week 1, Thursday.

### Why ALS over SGD for WMF

- **Closed-form updates.** Fix all user vectors → each item vector has a closed-form solution from regularized linear regression (one matrix inversion per item). Fix all item vectors → each user vector has a closed-form solution. Alternate between the two phases. No learning rate to tune, no gradient noise.
- **Embarrassingly parallel.** Within one phase (e.g., updating all user vectors), each user's update is independent of every other user's. Same for items. Trivially parallelizable across CPU cores or GPU.
- **Faster on sparse data.** Each user's update only depends on items they've actually rated, which is a small set (most users rate < 100 movies out of 62K). Computation is O(non-zeros) per iteration, not O(users × items).
- **Matches the original paper.** Hu/Koren/Volinsky's algorithm IS ALS. Section 4 of the paper derives the exact closed-form updates. Implementing it any other way deviates from the canonical formulation.
- **Industry standard.** Spark MLlib's `ALS`, the `implicit` library's `AlternatingLeastSquares`, and most production WMF systems all use ALS. Mentor will recognize the choice.

### Where SGD wins

- **Pedagogical familiarity:** matches Andrew Ng's course gradient-descent framing exactly.
- **Easier to implement non-standard losses:** if you want to add custom regularization, SGD via PyTorch autograd is more flexible.

For your project both reasons are weak — you have no reason to deviate from the standard loss.

### Resources for ALS

- **Hu, Koren, Volinsky (2008), Section 4.** This is the load-bearing read. The closed-form ALS updates for the confidence-weighted loss are derived here. Find via Google Scholar — search "Collaborative Filtering for Implicit Feedback Datasets Hu Koren Volinsky."
- **`implicit` library source code** at `https://github.com/benfred/implicit` — after you've drafted your own ALS implementation from the paper, read theirs to compare. Good for catching bugs.
- **Spark MLlib ALS documentation** — useful if you want to understand the distributed parallelization story (not required for your project scale, but good for mentor follow-up questions about scale).
- **Yehuda Koren's other papers** on matrix factorization (he was on the Netflix Prize-winning BellKor team). His "Matrix Factorization Techniques for Recommender Systems" article in IEEE Computer (2009) is a more accessible companion read.

### Recommendation

**ALS** — for paper alignment, speed, and mentor defensibility. Decide at the implementation step (Week 1, Thursday) — but bias your reading and prep toward ALS rather than SGD.

**All strategic decisions are locked. Move to implementation when ready.**

---

## 3. Why this shape — quick reasoning trail

### Why WMF over BPR or other top-N losses

You chose to use rating values as weighted positives (decision #6). Standard BPR is pairwise — observed > unobserved with no weights. Your weighted-positives intuition doesn't fit BPR. WMF (Hu, Koren, Volinsky 2008) is the canonical formulation for confidence-weighted implicit feedback. The math:

- For each user-item pair `(u, i)`: define a binary "preference" `p_{ui} ∈ {0, 1}` (1 if user rated it, 0 otherwise) and a "confidence" `c_{ui}` proportional to the rating value.
- Loss = `Σ c_{ui} × (p_{ui} − u^T v)² + λ × regularization` (over all user-item pairs, including unobserved ones).
- The confidence weighting means high-rated interactions contribute more strongly to the gradient than low-rated ones.

This is exactly what you wanted. It's also a well-known, defensible algorithm that the mentor will recognize.

### Why MovieLens 25M (switched from 1M)

The TMDB join requires `links.csv`, which exists in ml-25m but NOT in ml-1m. Switching to 25M:
- Pro: clean join to TMDB metadata for rich content-based features. Bigger dataset = more impressive. Standard scale for current rec-sys research.
- Con: ~25× more training time. Requires Colab GPU. Each epoch ~10-30 min vs ~30 seconds on ml-1m.

The tradeoff is worth it for the cold-start work and portfolio defense.

### Why cold start as the failure mode (both user-side AND item-side)

Initial plan attacked only user cold start. New consideration: your item-side filter (decision #5) sets up an item cold-start problem too — new movies pass the filter but have no embedding. So you're actually attacking BOTH:
- **New user (no rating history):** content-based or popularity fallback.
- **New item (no interaction history):** TMDB-feature-based embedding initialization.

This is a stronger story than handling just one side. It uses your TMDB join naturally.

---

## 4. Dataset shape (locked)

```
recommendation-system/
├── data/
│   ├── ml-25m/                         # MovieLens 25M dataset
│   │   ├── ratings.csv                 # userId, movieId, rating (0.5-5.0), timestamp
│   │   ├── movies.csv                  # movieId, title, genres
│   │   ├── tags.csv                    # user-applied tags (optional)
│   │   └── links.csv                   # movieId → imdbId, tmdbId
│   └── tmdb/
│       ├── tmdb_5000_movies.csv        # Kaggle TMDB metadata
│       └── tmdb_5000_credits.csv       # Kaggle TMDB cast/crew
├── notebooks/
│   ├── 01-data-exploration.ipynb
│   ├── 02-data-prep-and-join.ipynb     # Join ml-25m + TMDB, filter consensus-bad items
│   ├── 03-baseline.ipynb               # Popularity baseline, average baseline
│   ├── 04-wmf-from-scratch.ipynb       # Your WMF implementation
│   ├── 05-library-comparison.ipynb     # `implicit` WMF + Surprise SVD comparison
│   ├── 06-cold-start.ipynb             # Both new-user and new-item handling
│   └── 07-final-comparison.ipynb       # All approaches side-by-side + failure analysis
├── WRITEUP.md
└── README.md
```

Data downloads:
- MovieLens 25M: `https://files.grouplens.org/datasets/movielens/ml-25m.zip` (250 MB)
- TMDB 5000 from Kaggle: `https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata`

Join logic: `links.csv` provides `tmdbId` for each MovieLens `movieId`. Inner-join the two datasets on tmdbId to get rich item features.

---

## 5. Week-by-week breakdown (updated)

### Week 1 — Data, build, baseline

**Hours:** ~10-12 ML hours. Colab GPU for any training step.

- **Mon (1.5 hr):** Download ml-25m and TMDB. Set up project structure. Notebook `01-data-exploration.ipynb`: schema, rating distribution, user activity histogram, movie popularity histogram. Pre-fit prediction: write down what you expect before plotting.
- **Tue (1.5 hr):** Notebook `02-data-prep-and-join.ipynb`. Join ml-25m + TMDB via `links.csv`. Apply your item-level filter (80% rule). Measure: what % of movies got filtered? Adjust threshold if needed. Build the final user-movie-weight table.
- **Wed (1.5 hr):** Train/val/test split. Apply leave-one-out per user (decision #10). Notebook `03-baseline.ipynb`: popularity baseline (recommend most-rated movies to everyone), average-rating baseline. Compute Recall@10, Precision@10, NDCG@10.
- **Thu (1.5 hr):** Notebook `04-wmf-from-scratch.ipynb`: write WMF model in PyTorch. User embedding + item embedding. Loss = WMF (per the Hu/Koren/Volinsky formulation). Train on Colab GPU. Pre-fit prediction: what NDCG do you expect vs popularity baseline?
- **Fri (1.5 hr, light day):** Sanity checks on your WMF: do user embeddings cluster sensibly? Do item embeddings cluster by genre? Spot-check top-10 recommendations for 3-5 users.
- **Sat (5 hr, deep day):** Notebook `05-library-comparison.ipynb`: run `implicit` library's WMF on same split. Compare to your hand-built version — they should be close. If far off, debug. Also run Surprise's SVD as a sanity baseline. Tabulate all metrics.
- **Sun (3 hr):** Recovery + write findings. Plan week 2 in detail.

**Week 1 deliverable check:** Working WMF model. Library comparison done. Baselines beaten. Defensible reasoning for each design choice.

### Week 2 — Cold start, failure analysis, writeup

**Hours:** ~10-12 ML hours.

- **Mon (1.5 hr):** Notebook `06-cold-start.ipynb` — new-user cold start. Simulate by hiding all but K (K=0, 1, 5) ratings per user from the test set. Measure how WMF performance degrades. Quantify the cliff.
- **Tue (1.5 hr):** New-item cold start. Simulate by holding out N movies entirely from training. Use TMDB content features (cast, crew, keywords) to compute an embedding for these held-out movies. Measure NDCG on these "new items" vs warm items.
- **Wed (1.5 hr):** Hybrid switching: combine your WMF model with content-based fallback for cold-start cases. Compare to using only WMF.
- **Thu (1.5 hr):** Notebook `07-final-comparison.ipynb`: side-by-side comparison of all approaches (popularity baseline, your WMF, library WMF, Surprise SVD, content-based, hybrid). All metrics + cold-start specific metrics. Plots.
- **Fri (1.5 hr, light day):** Failure analysis. Pick 3-5 cases where hybrid still fails. Why? Are they polarized movies (your filter let through)? Cross-genre users? Document each case.
- **Sat (5 hr, deep day):** Write `WRITEUP.md` following the turn-detection structure: problem, approach landscape, your choices, dataset + preprocessing, results, failure analysis, latency/scale considerations, next steps. Push to GitHub.
- **Sun (3 hr):** Polish notebooks. Spaced review. Save for mock interview.

**Week 2 deliverable check:** GitHub repo with 7 notebooks, WRITEUP.md, working hybrid system for both user-side and item-side cold start, real failure analysis.

---

## 6. Key resources / references

Lock these for your reference. Read what you need from each, don't try to read end-to-end.

### Core paper (REQUIRED reading)
- **Hu, Y., Koren, Y., & Volinsky, C. (2008). "Collaborative Filtering for Implicit Feedback Datasets."** *IEEE International Conference on Data Mining (ICDM 2008), pp. 263-272.*
  - This is the canonical WMF paper. Section 4 (the math) is load-bearing.
  - Available via Google Scholar or Yifan Hu's personal page.
  - Read once before you start `04-wmf-from-scratch.ipynb`.

### Datasets
- **MovieLens 25M:** `https://files.grouplens.org/datasets/movielens/ml-25m.zip`
- **TMDB 5000 (Kaggle):** `https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata`

### Libraries
- **`implicit`** library — has WMF (Alternating Least Squares variant) native: `https://github.com/benfred/implicit`
- **Surprise** library — for classical SVD comparison: `https://surpriselib.com/`

### Reference document
- `research-notes.md` in this directory — your one-page primer on the field. Refer back as needed.

### Useful but not required
- Microsoft Recommenders repo — has WMF and many other algorithms implemented. Worth browsing.
- LightFM library — hybrid CF + content-based. Worth knowing exists, but `implicit` is the better fit for your locked design.

---

## 7. What I cannot help with

Per the operating mode (`feedback_user_drives_reasoning`):
- **Code generation.** I won't write the PyTorch WMF code. Build it from the Hu/Koren/Volinsky paper + your understanding.
- **Hyperparameter choices.** I won't tell you embedding dim = 64 is right. You experiment.
- **Architectural micro-choices.** Bias terms? Layer counts? Initialization? You decide.
- **Writeup structure.** The turn-detection writeup is a template. Adapt, don't copy.
- **Strategic decision-making.** When you hit a fork in the road, decide. I pressure-test after you commit.

What I can help with:
- Debugging code you wrote.
- Explaining specific concepts you encounter by name (e.g., "what does ALS optimization mean?").
- Pressure-testing decisions — asking "why this and not X?"
- Reviewing your draft writeup for clarity.
- Catching evaluation-protocol bugs (top-N ranking has many subtle traps).

---

## 8. How this connects to your bigger picture

- **Mentor track:** Problem 3 in his sequence. Three applied projects (turn detection, ASR or diarization, recommendations) before mock interview.
- **Indian job market alignment:** Rec sys is hired-for at Flipkart, Swiggy, Zomato, Myntra, MX Player, JioHotstar, Sharechat, Meesho. A defensible project hits the bar.
- **DSA discipline:** Keep daily drills. 15 min/day even during this project.
- **MCA:** June 27 exam deadline. 45 min/day. Don't sacrifice.
- **Bandwidth:** 10-12 hrs/week ML. If a week runs over, trim stretch goals.

---

## 9. When to ping me

- When you commit ALS vs SGD (Section 2) — I'll pressure-test the choice.
- When you have the week 1 WMF model trained and want me to ask sharp questions about your evaluation protocol or design.
- When you have a draft writeup and want a reviewer.
- When you're stuck on a specific concept or bug (specific, not "what should I do next").

Don't ping me asking "what should I work on today" — that pattern is closed.

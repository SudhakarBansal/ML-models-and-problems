"""Authors + executes notebook 07 (final comparison / capstone)."""
import os, time
import nbformat as nbf
from nbformat.v4 import new_notebook, new_code_cell, new_markdown_cell
from nbclient import NotebookClient

ROOT = os.path.dirname(os.path.abspath(__file__))
NB_DIR = os.path.join(ROOT, "notebooks")


def md(s): return new_markdown_cell(s)
def code(s): return new_code_cell(s)


NB07 = [
    md("# 07 — Final Comparison & Findings\n\n"
       "Consolidates every model in this project under one evaluation protocol\n"
       "(He et al. NCF: 1 held-out positive vs 99 sampled negatives; Recall@10 = Hit@10, plus NDCG@10).\n\n"
       "| Notebook | Model | Data |\n"
       "|---|---|---|\n"
       "| 03 | Popularity baseline | full 25M |\n"
       "| 05 | Surprise SVD (Funk-SVD, explicit) | 2M sample |\n"
       "| 05 | **implicit ALS (WMF)** | full 25M |\n"
       "| 04 | **WMF from scratch (HKV/ALS, NumPy)** | 15K-user subsample |\n"
       "| 06 | Cold-start: TMDB content projection | TMDB-covered subset |"),
    code("import os, sys, time\n"
         "os.environ['OPENBLAS_NUM_THREADS'] = '1'\n"
         "sys.path.insert(0, os.path.abspath('..'))\n"
         "import numpy as np, scipy.sparse as sp\n"
         "import recsys_utils as ru\n"
         "from implicit.cpu.als import AlternatingLeastSquares\n"
         "ART = '../artifacts'\n"
         "train_mat = sp.load_npz(f'{ART}/train_mat.npz')\n"
         "c = np.load(f'{ART}/cands.npz'); users, cands = c['users'], c['cands']\n"
         "print('full-data eval set:', train_mat.shape, '|', len(users), 'users')"),

    md("## Headline result on the full 25M dataset"),
    code("item_pop = np.asarray(train_mat.getnnz(axis=0)).ravel().astype(np.float32)\n"
         "r_pop, n_pop = ru.score_metrics(ru.score_popularity(item_pop, cands), k=10)\n"
         "als = AlternatingLeastSquares(factors=64, regularization=0.05, alpha=ru.ALPHA,\n"
         "                              iterations=15, random_state=42)\n"
         "als.fit(train_mat, show_progress=False)\n"
         "r_als, n_als = ru.score_metrics(ru.score_als(als.user_factors, als.item_factors, users, cands), k=10)\n"
         "print(f'{\"Model (full 25M)\":<24}{\"Recall@10\":>12}{\"NDCG@10\":>12}')\n"
         "print('-'*48)\n"
         "print(f'{\"Popularity baseline\":<24}{r_pop:>12.4f}{n_pop:>12.4f}')\n"
         "print(f'{\"implicit ALS (WMF)\":<24}{r_als:>12.4f}{n_als:>12.4f}')\n"
         "print(f'\\nWMF lifts NDCG@10 by {100*(n_als-n_pop)/n_pop:.1f}% over the popularity baseline.')"),

    md("## Full results table (across notebooks)\n\n"
       "| Model | Recall@10 | NDCG@10 | Notes |\n"
       "|---|---|---|---|\n"
       "| Popularity baseline (25M) | 0.925 | 0.661 | high — sampled-negative artifact (Rendle 2020) |\n"
       "| Surprise SVD (2M) | 0.514 | 0.307 | optimizes RMSE, not ranking → wrong task framing |\n"
       "| **implicit ALS / WMF (25M)** | **0.971** | **0.810** | best; the production-grade library |\n"
       "| WMF from scratch (15K users) | 0.926 | 0.697 | matches library (0.928/0.696) on same data ✓ |\n"
       "| Cold-start content projection | 0.385 | 0.201 | vs 0.10 random → content rescues new items |\n\n"
       "### What I'd say about these numbers\n"
       "1. **WMF clearly beats popularity** on the personalized metric (NDCG@10 0.81 vs 0.66).\n"
       "2. **My from-scratch ALS matches the library** to within 0.002 — evidence the HKV math is right.\n"
       "3. **Surprise underperforms popularity**: rating-prediction (RMSE) ≠ top-N ranking. The task\n"
       "   framing matters more than the algorithm.\n"
       "4. **Sampled-negative metrics flatter everything** (popularity hits 0.92); the honest signal is\n"
       "   the *gap* between models, and a full unsampled ranking would separate them further.\n"
       "5. **Cold-start**: a content→latent projection takes brand-new movies from ~0.10 (random) to\n"
       "   0.385 Recall@10 — collaborative filtering alone can't touch zero-interaction items.\n\n"
       "### Honest limitations\n"
       "- Offline sampled metrics, not an online A/B test (the real production signal).\n"
       "- From-scratch ALS validated on a 15K-user subsample (pure-NumPy per-user loop doesn't scale to 162K).\n"
       "- Single train/test leave-one-out split; no hyperparameter sweep on factors/alpha/reg.\n\n"
       "### Natural next step → reinforcement learning\n"
       "This is a *static* model: train once, serve. The real product question is sequential —\n"
       "*which* item to show *now* to maximise long-run engagement, learning online from feedback.\n"
       "That reframes recommendation as a **contextual bandit** (context = user history, arm = item,\n"
       "reward = engagement), balancing exploration of new items against exploitation of known-good ones.")
]


def run():
    nb = new_notebook(cells=NB07)
    nb.metadata["kernelspec"] = {"name": "python3", "display_name": "Python 3", "language": "python"}
    t = time.time()
    NotebookClient(nb, timeout=1200, kernel_name="python3",
                   resources={"metadata": {"path": NB_DIR}}).execute()
    nbf.write(nb, os.path.join(NB_DIR, "07-final-comparison.ipynb"))
    print(f"wrote 07-final-comparison.ipynb in {time.time()-t:.1f}s")


if __name__ == "__main__":
    run()

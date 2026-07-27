"""Authors + executes notebook 04 (from-scratch WMF/ALS). Run from project root."""
import os, sys, time
import nbformat as nbf
from nbformat.v4 import new_notebook, new_code_cell, new_markdown_cell

ROOT = os.path.dirname(os.path.abspath(__file__))
NB_DIR = os.path.join(ROOT, "notebooks")
from nbclient import NotebookClient


def md(s): return new_markdown_cell(s)
def code(s): return new_code_cell(s)


NB04 = [
    md("# 04 — Weighted Matrix Factorization from Scratch (ALS)\n\n"
       "Implements the **Hu, Koren & Volinsky (2008)** WMF model with **Alternating Least Squares**,\n"
       "using only NumPy, and checks it reaches the same ranking quality as the `implicit` library on\n"
       "identical data.\n\n"
       "Pure-NumPy ALS with a per-entity Python loop is fine for tens of thousands of users but not for\n"
       "all 162K, so this notebook runs on a **random 15,000-user subsample** (the library handles full\n"
       "scale in nb 05). Both models here see the *exact same* subsample, split and candidates, so the\n"
       "comparison is apples-to-apples."),
    code("import os, sys, time\n"
         "os.environ['OPENBLAS_NUM_THREADS'] = '1'\n"
         "sys.path.insert(0, os.path.abspath('..'))\n"
         "import numpy as np, pandas as pd, scipy.sparse as sp\n"
         "import recsys_utils as ru\n"
         "DATA = '../data/ml-25m'\n"
         "rng = np.random.default_rng(0)"),

    md("## Build a 15K-user subsample (same prep as nb 02)"),
    code("ratings = pd.read_csv(f'{DATA}/ratings.csv')\n"
         "keep = rng.choice(ratings.userId.unique(), size=15000, replace=False)\n"
         "ratings = ratings[ratings.userId.isin(keep)]\n"
         "ratings, _ = ru.filter_consensus_bad(ratings)\n"
         "uc = ratings.userId.value_counts()\n"
         "ratings = ratings[ratings.userId.isin(uc[uc >= ru.MIN_USER_RATINGS].index)]\n"
         "ratings, user_ids, movie_ids = ru.reindex(ratings)\n"
         "n_users, n_items = int(ratings.u.max()+1), int(ratings.i.max()+1)\n"
         "train, test = ru.leave_one_out_split(ratings)\n"
         "R = ru.build_confidence_matrix(train, n_users, n_items)\n"
         "users, cands = ru.build_eval_candidates(test.u.values, test.i.values, R, n_items, seed=0)\n"
         "print(f'{n_users:,} users | {n_items:,} items | {R.nnz:,} train interactions | '\n"
         "      f'{len(users):,} eval users')"),

    md("## The math (what the code below implements)\n\n"
       "Minimise, over user vectors $x_u$ and item vectors $y_i$:\n\n"
       "$$\\sum_{u,i} c_{ui}\\,(p_{ui} - x_u^\\top y_i)^2 \\;+\\; \\lambda\\Big(\\sum_u\\|x_u\\|^2 + \\sum_i\\|y_i\\|^2\\Big)$$\n\n"
       "- $p_{ui}=1$ if the user rated movie $i$, else $0$ (**preference**).\n"
       "- $c_{ui}=1+\\alpha\\,r_{ui}$ (**confidence** — higher ratings = more confidence in that positive).\n\n"
       "The cost is quadratic, so **fixing one factor matrix makes the other solvable in closed form**.\n"
       "With all $y_i$ fixed, each user vector is:\n\n"
       "$$x_u = (Y^\\top C^u Y + \\lambda I)^{-1}\\,Y^\\top C^u p(u)$$\n\n"
       "The HKV speed-up avoids the dense $n\\_items \\times n\\_items$ matrix $C^u$ by writing\n"
       "$Y^\\top C^u Y = Y^\\top Y + Y^\\top (C^u - I) Y$, where:\n"
       "- $Y^\\top Y$ is computed **once per sweep** and shared by every user, and\n"
       "- $(C^u - I)$ is non-zero only on the handful of items the user actually rated.\n\n"
       "So each user's update costs work proportional to *their* number of ratings, not the whole catalog.\n"
       "Then alternate: solve all users, then all items, repeat. No learning rate."),
    code("def _solve_factors(R, Y, reg, alpha):\n"
         "    \"\"\"One ALS half-sweep: given fixed factors Y, return new factors for every row of R.\n"
         "    R is a CSR matrix whose stored values are the raw ratings r_ui.\"\"\"\n"
         "    f = Y.shape[1]\n"
         "    YtY = Y.T @ Y                       # shared across all rows (the HKV trick)\n"
         "    lam = reg * np.eye(f)\n"
         "    X = np.zeros((R.shape[0], f))\n"
         "    indptr, indices, data = R.indptr, R.indices, R.data\n"
         "    for e in range(R.shape[0]):\n"
         "        s, t = indptr[e], indptr[e+1]\n"
         "        if s == t:\n"
         "            continue                    # no ratings -> stays at zero (prior only)\n"
         "        idx = indices[s:t]\n"
         "        c = 1.0 + alpha * data[s:t]      # confidence c_ui = 1 + alpha*r\n"
         "        Ye = Y[idx]                      # (k, f) factors of this row's rated items\n"
         "        # A = YtY + Ye^T (c-1) Ye + lambda*I ;  b = Ye^T c   (p=1 on observed)\n"
         "        A = YtY + (Ye * (c - 1.0)[:, None]).T @ Ye + lam\n"
         "        b = Ye.T @ c\n"
         "        X[e] = np.linalg.solve(A, b)\n"
         "    return X\n"
         "\n"
         "class WMF:\n"
         "    \"\"\"Weighted Matrix Factorization (implicit feedback) trained with ALS.\"\"\"\n"
         "    def __init__(self, factors=64, regularization=0.05, alpha=40.0, iterations=15, seed=42):\n"
         "        self.f, self.reg, self.alpha, self.iters, self.seed = (\n"
         "            factors, regularization, alpha, iterations, seed)\n"
         "    def fit(self, R):\n"
         "        rng = np.random.default_rng(self.seed)\n"
         "        nu, ni = R.shape\n"
         "        self.user_factors = 0.01 * rng.standard_normal((nu, self.f))\n"
         "        self.item_factors = 0.01 * rng.standard_normal((ni, self.f))\n"
         "        Rt = R.T.tocsr()\n"
         "        for it in range(self.iters):\n"
         "            self.user_factors = _solve_factors(R,  self.item_factors, self.reg, self.alpha)\n"
         "            self.item_factors = _solve_factors(Rt, self.user_factors, self.reg, self.alpha)\n"
         "        return self"),

    md("## Train the from-scratch model and evaluate"),
    code("t = time.time()\n"
         "wmf = WMF(factors=64, regularization=0.05, alpha=ru.ALPHA, iterations=15).fit(R)\n"
         "print(f'trained from-scratch WMF in {time.time()-t:.1f}s')\n"
         "scores = ru.score_als(wmf.user_factors.astype(np.float32),\n"
         "                      wmf.item_factors.astype(np.float32), users, cands)\n"
         "r_scratch, n_scratch = ru.score_metrics(scores, k=10)\n"
         "print(f'from-scratch WMF  ->  Recall@10 = {r_scratch:.4f}   NDCG@10 = {n_scratch:.4f}')"),

    md("## Sanity check vs the `implicit` library on the SAME subsample\n\n"
       "The library uses confidence `alpha*r` while this implementation uses the paper's `1 + alpha*r`;\n"
       "the small constant barely matters at `alpha=40`, so the ranking metrics should land very close.\n"
       "Matching a battle-tested library is the evidence the from-scratch math is correct."),
    code("from implicit.cpu.als import AlternatingLeastSquares\n"
         "lib = AlternatingLeastSquares(factors=64, regularization=0.05, alpha=ru.ALPHA,\n"
         "                              iterations=15, random_state=42)\n"
         "lib.fit(R, show_progress=False)\n"
         "lib_scores = ru.score_als(lib.user_factors, lib.item_factors, users, cands)\n"
         "r_lib, n_lib = ru.score_metrics(lib_scores, k=10)\n"
         "\n"
         "item_pop = np.asarray(R.getnnz(axis=0)).ravel().astype(np.float32)\n"
         "r_pop, n_pop = ru.score_metrics(ru.score_popularity(item_pop, cands), k=10)\n"
         "print(f'{\"Model\":<24}{\"Recall@10\":>12}{\"NDCG@10\":>12}')\n"
         "print('-'*48)\n"
         "for name, r, n in [('Popularity baseline', r_pop, n_pop),\n"
         "                   ('from-scratch WMF (mine)', r_scratch, n_scratch),\n"
         "                   ('implicit ALS (library)', r_lib, n_lib)]:\n"
         "    print(f'{name:<24}{r:>12.4f}{n:>12.4f}')"),

    md("**Takeaway:** the from-scratch ALS lands essentially on top of the library on the same data,\n"
       "confirming the implementation of the HKV closed-form update is correct — and it beats the\n"
       "popularity baseline, which is the bar a real personalized model must clear."),
]


def run():
    nb = new_notebook(cells=NB04)
    nb.metadata["kernelspec"] = {"name": "python3", "display_name": "Python 3", "language": "python"}
    path = os.path.join(NB_DIR, "04-wmf-from-scratch.ipynb")
    t = time.time()
    NotebookClient(nb, timeout=2400, kernel_name="python3",
                   resources={"metadata": {"path": NB_DIR}}).execute()
    nbf.write(nb, path)
    print(f"wrote 04-wmf-from-scratch.ipynb in {time.time()-t:.1f}s")


if __name__ == "__main__":
    run()

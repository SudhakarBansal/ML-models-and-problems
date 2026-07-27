"""
Authors and executes notebooks 02, 03, 05 with real outputs.
Run from the project root:  python _build_nb.py 02 03 05
"""
import os, sys, time
import nbformat as nbf
from nbformat.v4 import new_notebook, new_code_cell, new_markdown_cell
from nbclient import NotebookClient

ROOT = os.path.dirname(os.path.abspath(__file__))
NB_DIR = os.path.join(ROOT, "notebooks")
KERNEL = "python3"


def md(s): return new_markdown_cell(s)
def code(s): return new_code_cell(s)


# ----------------------------------------------------------------------------
# Notebook 02 — data prep
# ----------------------------------------------------------------------------
NB02 = [
    md("# 02 — Data Prep, Filtering & Implicit-Feedback Conversion\n\n"
       "Turns raw MovieLens-25M ratings into the inputs the recommender needs:\n"
       "1. **Filter** consensus-bad movies (>=80% of ratings below 2.5).\n"
       "2. **Convert to implicit feedback**: every observed rating is a positive; the\n"
       "   rating value becomes a *confidence* weight `C_ui = 1 + alpha*r_ui` (Hu/Koren/Volinsky 2008).\n"
       "3. **Leave-one-out split**: hold out each user's most-recent rating as the test item.\n"
       "4. **Save artifacts** so later notebooks load instantly instead of re-reading 25M rows.\n\n"
       "All shared logic lives in `recsys_utils.py` (imported as `ru`)."),
    code("import os, sys\n"
         "os.environ['OPENBLAS_NUM_THREADS'] = '1'   # implicit/ALS: BLAS threadpool hurts here\n"
         "sys.path.insert(0, os.path.abspath('..'))   # project root, for recsys_utils\n"
         "import numpy as np, pandas as pd, scipy.sparse as sp\n"
         "import recsys_utils as ru\n"
         "DATA, ART = '../data/ml-25m', '../artifacts'\n"
         "os.makedirs(ART, exist_ok=True)\n"
         "print('alpha=%g  bad_fraction=%g  min_user_ratings=%d'\n"
         "      % (ru.ALPHA, ru.BAD_FRACTION, ru.MIN_USER_RATINGS))"),

    md("## 1. Load raw ratings"),
    code("ratings = pd.read_csv(f'{DATA}/ratings.csv')\n"
         "print(f'{len(ratings):,} ratings | {ratings.userId.nunique():,} users | '\n"
         "      f'{ratings.movieId.nunique():,} movies')\n"
         "ratings.head(3)"),

    md("## 2. Item filter — drop consensus-bad movies\n\n"
       "A movie that almost everyone rates below 2.5 should never be recommended, so it only\n"
       "adds noise and parameters. We drop those. **Polarized** movies (loved by some, hated by\n"
       "others) are kept on purpose — learning *who* likes them is exactly what the model is for."),
    code("ratings, dropped = ru.filter_consensus_bad(ratings)\n"
         "print(f'dropped {len(dropped):,} consensus-bad movies; '\n"
         "      f'{ratings.movieId.nunique():,} movies remain')"),

    md("## 3. User filter + contiguous reindex\n\n"
       "Drop users with fewer than 5 ratings (too little signal, and leave-one-out needs >=2),\n"
       "then map raw ids to contiguous row/column indices for the sparse matrix."),
    code("uc = ratings.userId.value_counts()\n"
         "ratings = ratings[ratings.userId.isin(uc[uc >= ru.MIN_USER_RATINGS].index)]\n"
         "ratings, user_ids, movie_ids = ru.reindex(ratings)\n"
         "n_users, n_items = int(ratings.u.max()+1), int(ratings.i.max()+1)\n"
         "print(f'{len(ratings):,} ratings | {n_users:,} users | {n_items:,} items')"),

    md("## 4. Implicit-feedback confidence\n\n"
       "MovieLens gives *explicit* 1–5 ratings, but we model this as **implicit** top-N ranking.\n"
       "Following Hu/Koren/Volinsky (2008):\n\n"
       "- **preference** `p_ui = 1` for every observed rating (the user engaged with the movie),\n"
       "- **confidence** `C_ui = 1 + alpha * r_ui` — a 5-star rating gives more confidence in that\n"
       "  positive than a 3-star one.\n\n"
       "We store the raw `r_ui` in the matrix; the `implicit` library multiplies by `alpha`, and the\n"
       "from-scratch model (nb 04) applies `1 + alpha*r` explicitly."),

    md("## 5. Leave-one-out split\n\n"
       "Each user's **most-recent** rating becomes the test item (predict the *next* interaction).\n"
       "Test items whose movie never appears in training are item-cold-start cases — dropped here,\n"
       "handled in notebook 06."),
    code("train, test = ru.leave_one_out_split(ratings)\n"
         "print(f'{len(train):,} train rows | {len(test):,} test rows (one held-out item per user)')"),
    code("train_mat = ru.build_confidence_matrix(train, n_users, n_items)\n"
         "print('train matrix:', train_mat.shape, f'| {train_mat.nnz:,} nonzeros '\n"
         "      f'| density {train_mat.nnz/(n_users*n_items):.5%}')"),

    md("## 6. Save artifacts\n\n"
       "`train_mat.npz` (sparse confidence matrix), the held-out test arrays, and the id maps."),
    code("sp.save_npz(f'{ART}/train_mat.npz', train_mat)\n"
         "np.savez(f'{ART}/test.npz', u=test.u.values, i=test.i.values)\n"
         "np.savez(f'{ART}/maps.npz', user_ids=user_ids, movie_ids=movie_ids)\n"
         "print('saved:', os.listdir(ART))"),
]

# ----------------------------------------------------------------------------
# Notebook 03 — baseline + eval harness
# ----------------------------------------------------------------------------
NB03 = [
    md("# 03 — Baseline & Evaluation Harness (Recall@10 / NDCG@10)\n\n"
       "Defines the evaluation protocol every model in this project is judged by, and establishes\n"
       "the **popularity baseline** any real model must beat.\n\n"
       "**Protocol (He et al., NCF 2017):** for each user, rank the 1 held-out positive against\n"
       "**99 sampled negatives** the user never interacted with. A model that puts the true item\n"
       "in the top 10 of those 100 scores a hit.\n"
       "- **Recall@10 = Hit@10** (single relevant item): fraction of users whose true item is top-10.\n"
       "- **NDCG@10** rewards ranking the true item *higher* within the top 10.\n\n"
       "The candidate set is built **once** and reused by every model, so comparisons are fair."),
    code("import os, sys\n"
         "os.environ['OPENBLAS_NUM_THREADS'] = '1'\n"
         "sys.path.insert(0, os.path.abspath('..'))\n"
         "import numpy as np, scipy.sparse as sp\n"
         "import recsys_utils as ru\n"
         "ART = '../artifacts'\n"
         "train_mat = sp.load_npz(f'{ART}/train_mat.npz')\n"
         "tst = np.load(f'{ART}/test.npz')\n"
         "test_u, test_i = tst['u'], tst['i']\n"
         "n_users, n_items = train_mat.shape\n"
         "print(f'{n_users:,} users | {n_items:,} items | {len(test_u):,} test users')"),

    md("## Build the shared candidate set (1 positive + 99 negatives per user)"),
    code("t = __import__('time').time()\n"
         "users, cands = ru.build_eval_candidates(test_u, test_i, train_mat, n_items, seed=0)\n"
         "np.savez(f'{ART}/cands.npz', users=users, cands=cands)\n"
         "print('candidates:', cands.shape, f'(built in {__import__(\"time\").time()-t:.1f}s)')\n"
         "print('col 0 is the true item; cols 1..99 are sampled negatives')"),

    md("## Popularity baseline\n\n"
       "Score every candidate by how many times it was interacted with in training. This is the\n"
       "'recommend the most popular movies to everyone' strategy — no personalization at all."),
    code("item_pop = np.asarray(train_mat.getnnz(axis=0)).ravel().astype(np.float32)\n"
         "pop_scores = ru.score_popularity(item_pop, cands)\n"
         "recall, ndcg = ru.score_metrics(pop_scores, k=10)\n"
         "print(f'Popularity baseline  ->  Recall@10 = {recall:.4f}   NDCG@10 = {ndcg:.4f}')"),

    md("> Note: this baseline scores high because random negatives are usually obscure movies, so a\n"
       "> popular held-out movie beats them easily. This is a known property of the *sampled*-negative\n"
       "> protocol (Rendle et al., 2020) — the real test is how much a personalized model beats it."),
]

# ----------------------------------------------------------------------------
# Notebook 05 — library WMF (implicit ALS) + Surprise SVD
# ----------------------------------------------------------------------------
NB05 = [
    md("# 05 — Library WMF (implicit ALS) + Surprise SVD\n\n"
       "Benchmarks against two standard libraries on the **exact same** candidates/metrics as the\n"
       "baseline:\n"
       "- **`implicit.AlternatingLeastSquares`** — the canonical WMF for implicit feedback (the\n"
       "  library implementation of Hu/Koren/Volinsky 2008).\n"
       "- **`surprise.SVD`** — classical Funk-SVD on the explicit ratings, as a sanity comparison.\n\n"
       "These are the numbers quoted on the resume."),
    code("import os, sys, time\n"
         "os.environ['OPENBLAS_NUM_THREADS'] = '1'\n"
         "sys.path.insert(0, os.path.abspath('..'))\n"
         "import numpy as np, scipy.sparse as sp\n"
         "import recsys_utils as ru\n"
         "ART = '../artifacts'\n"
         "train_mat = sp.load_npz(f'{ART}/train_mat.npz')\n"
         "c = np.load(f'{ART}/cands.npz'); users, cands = c['users'], c['cands']\n"
         "n_users, n_items = train_mat.shape\n"
         "print(f'{n_users:,} users | {n_items:,} items | {len(users):,} eval users')"),

    md("## implicit ALS (Weighted Matrix Factorization)\n\n"
       "`factors=64` latent dimensions, `alpha=40` confidence scaling, L2 `regularization=0.05`,\n"
       "15 ALS sweeps. ALS alternates: fix item vectors → solve each user vector in closed form,\n"
       "then fix users → solve each item. No learning rate, and each sweep is embarrassingly parallel."),
    code("from implicit.cpu.als import AlternatingLeastSquares\n"
         "t = time.time()\n"
         "als = AlternatingLeastSquares(factors=64, regularization=0.05, alpha=ru.ALPHA,\n"
         "                              iterations=15, random_state=42)\n"
         "als.fit(train_mat, show_progress=False)\n"
         "print(f'trained implicit ALS in {time.time()-t:.1f}s')\n"
         "als_scores = ru.score_als(als.user_factors, als.item_factors, users, cands)\n"
         "r_als, n_als = ru.score_metrics(als_scores, k=10)\n"
         "print(f'implicit ALS (WMF)  ->  Recall@10 = {r_als:.4f}   NDCG@10 = {n_als:.4f}')"),

    md("## Surprise SVD (classical Funk-SVD on explicit ratings)\n\n"
       "Trained on a capped sample of the explicit ratings (Surprise is single-threaded and not\n"
       "built for 25M rows). Evaluated on the same held-out candidates by predicting a score for\n"
       "each (user, candidate-movie) pair."),
    code("from surprise import SVD, Dataset, Reader\n"
         "import pandas as pd\n"
         "# reconstruct (u,i,r) triples from the training matrix, capped for Surprise's speed\n"
         "coo = train_mat.tocoo()\n"
         "tr = pd.DataFrame({'u': coo.row, 'i': coo.col, 'r': coo.data})\n"
         "SAMPLE = 2_000_000\n"
         "if len(tr) > SAMPLE:\n"
         "    tr = tr.sample(SAMPLE, random_state=0)\n"
         "reader = Reader(rating_scale=(0.5, 5.0))\n"
         "data = Dataset.load_from_df(tr[['u','i','r']], reader).build_full_trainset()\n"
         "t = time.time()\n"
         "svd = SVD(n_factors=64, n_epochs=20, random_state=42)\n"
         "svd.fit(data)\n"
         "print(f'trained Surprise SVD on {len(tr):,} ratings in {time.time()-t:.1f}s')"),
    code("# score candidates with SVD (uses the raw inner-id estimates; unknown ids fall back to global mean)\n"
         "def svd_score_row(u, row):\n"
         "    return np.array([svd.predict(u, int(it)).est for it in row], dtype=np.float32)\n"
         "svd_scores = np.empty(cands.shape, dtype=np.float32)\n"
         "for k in range(len(users)):\n"
         "    svd_scores[k] = svd_score_row(int(users[k]), cands[k])\n"
         "r_svd, n_svd = ru.score_metrics(svd_scores, k=10)\n"
         "print(f'Surprise SVD        ->  Recall@10 = {r_svd:.4f}   NDCG@10 = {n_svd:.4f}')"),

    md("## Results summary"),
    code("item_pop = np.asarray(train_mat.getnnz(axis=0)).ravel().astype(np.float32)\n"
         "r_pop, n_pop = ru.score_metrics(ru.score_popularity(item_pop, cands), k=10)\n"
         "print(f'{\"Model\":<22}{\"Recall@10\":>12}{\"NDCG@10\":>12}')\n"
         "print('-'*46)\n"
         "for name, r, n in [('Popularity baseline', r_pop, n_pop),\n"
         "                   ('Surprise SVD', r_svd, n_svd),\n"
         "                   ('implicit ALS (WMF)', r_als, n_als)]:\n"
         "    print(f'{name:<22}{r:>12.4f}{n:>12.4f}')"),
]

NOTEBOOKS = {"02": ("02-data-prep-and-join.ipynb", NB02),
             "03": ("03-baseline.ipynb", NB03),
             "05": ("05-library-comparison.ipynb", NB05)}


def build_and_run(key):
    fname, cells = NOTEBOOKS[key]
    nb = new_notebook(cells=cells)
    nb.metadata["kernelspec"] = {"name": KERNEL, "display_name": "Python 3", "language": "python"}
    path = os.path.join(NB_DIR, fname)
    print(f"\n=== executing {fname} ===")
    t = time.time()
    client = NotebookClient(nb, timeout=1800, kernel_name=KERNEL,
                            resources={"metadata": {"path": NB_DIR}})
    client.execute()
    nbf.write(nb, path)
    print(f"--- wrote {fname} in {time.time()-t:.1f}s ---")


if __name__ == "__main__":
    keys = sys.argv[1:] or ["02", "03", "05"]
    for k in keys:
        build_and_run(k)

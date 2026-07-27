"""Authors + executes notebook 06 (item cold-start via TMDB content projection)."""
import os, sys, time
import nbformat as nbf
from nbformat.v4 import new_notebook, new_code_cell, new_markdown_cell

ROOT = os.path.dirname(os.path.abspath(__file__))
NB_DIR = os.path.join(ROOT, "notebooks")
from nbclient import NotebookClient


def md(s): return new_markdown_cell(s)
def code(s): return new_code_cell(s)


NB06 = [
    md("# 06 — Item Cold-Start via TMDB Content Projection\n\n"
       "**Problem:** collaborative filtering can't recommend a movie with *zero* interactions — it has\n"
       "no learned latent vector. **Fix (decision #13):** learn a map from a movie's *content features*\n"
       "(TMDB genres + keywords) into the WMF latent space, then embed brand-new movies from content alone.\n\n"
       "**Setup:**\n"
       "1. Keep movies that have TMDB metadata. Hold out 20% of them as **cold** (removed from training entirely).\n"
       "2. Train WMF on the **warm** movies -> user factors + warm item factors.\n"
       "3. Fit a **Ridge regression**: TMDB content features (warm) -> warm item factors.\n"
       "4. Apply it to **cold** movies to predict their latent vectors from content only.\n"
       "5. Evaluate: can we rank a user's held-out cold movie above 99 other cold movies? Compare the\n"
       "   content projection against a no-content baseline (every cold movie = the mean warm vector)."),
    code("import os, sys, time, json\n"
         "os.environ['OPENBLAS_NUM_THREADS'] = '1'\n"
         "sys.path.insert(0, os.path.abspath('..'))\n"
         "import numpy as np, pandas as pd, scipy.sparse as sp\n"
         "import recsys_utils as ru\n"
         "from sklearn.feature_extraction.text import TfidfVectorizer\n"
         "from sklearn.linear_model import Ridge\n"
         "DATA = '../data/ml-25m'\n"
         "rng = np.random.default_rng(0)"),

    md("## 1. Build content text (genres + keywords) per movieId via the TMDB join"),
    code("tmdb = pd.read_csv('../data/tmdb/tmdb_5000_movies.csv')\n"
         "links = pd.read_csv(f'{DATA}/links.csv').dropna(subset=['tmdbId'])\n"
         "links['tmdbId'] = links.tmdbId.astype(int)\n"
         "def names(js):\n"
         "    try: return ' '.join(d['name'].replace(' ', '_') for d in json.loads(js))\n"
         "    except Exception: return ''\n"
         "tmdb['content'] = (tmdb.genres.apply(names) + ' ' + tmdb.keywords.apply(names)).str.strip()\n"
         "tmdb = tmdb[tmdb.content != ''][['id', 'content']].rename(columns={'id': 'tmdbId'})\n"
         "movie_content = links.merge(tmdb, on='tmdbId')[['movieId', 'content']]\n"
         "print(f'{len(movie_content):,} movieIds have TMDB content features')"),

    md("## 2. Load ratings, restrict to TMDB-covered movies, subsample users for speed"),
    code("ratings = pd.read_csv(f'{DATA}/ratings.csv')\n"
         "ratings, _ = ru.filter_consensus_bad(ratings)\n"
         "ratings = ratings[ratings.movieId.isin(set(movie_content.movieId))]\n"
         "keep_users = rng.choice(ratings.userId.unique(),\n"
         "                        size=min(40000, ratings.userId.nunique()), replace=False)\n"
         "ratings = ratings[ratings.userId.isin(keep_users)]\n"
         "print(f'{len(ratings):,} ratings | {ratings.userId.nunique():,} users | '\n"
         "      f'{ratings.movieId.nunique():,} TMDB-covered movies')"),

    md("## 3. Split movies into warm (train) and cold (held out entirely)"),
    code("movies = ratings.movieId.unique()\n"
         "cold_movies = set(rng.choice(movies, size=int(0.20*len(movies)), replace=False))\n"
         "warm = ratings[~ratings.movieId.isin(cold_movies)]\n"
         "cold = ratings[ratings.movieId.isin(cold_movies)]\n"
         "# contiguous ids over WARM training data\n"
         "warm = warm.copy()\n"
         "warm['u'] = warm.userId.astype('category').cat.codes\n"
         "u_cats = warm.userId.astype('category').cat.categories\n"
         "warm['i'] = warm.movieId.astype('category').cat.codes\n"
         "i_cats = warm.movieId.astype('category').cat.categories\n"
         "uid2u = {uid: k for k, uid in enumerate(u_cats)}\n"
         "n_users, n_warm = len(u_cats), len(i_cats)\n"
         "R = sp.csr_matrix((warm.rating.values.astype(np.float32), (warm.u.values, warm.i.values)),\n"
         "                  shape=(n_users, n_warm))\n"
         "print(f'warm: {n_users:,} users x {n_warm:,} items ({R.nnz:,} interactions) | '\n"
         "      f'cold movies held out: {len(cold_movies):,}')"),

    md("## 4. Train WMF on warm movies (library ALS, full warm matrix)"),
    code("from implicit.cpu.als import AlternatingLeastSquares\n"
         "als = AlternatingLeastSquares(factors=64, regularization=0.05, alpha=ru.ALPHA,\n"
         "                              iterations=15, random_state=42)\n"
         "als.fit(R, show_progress=False)\n"
         "user_f = als.user_factors            # (n_users, 64)\n"
         "warm_item_f = als.item_factors       # (n_warm, 64)  <- the regression target\n"
         "print('user factors', user_f.shape, '| warm item factors', warm_item_f.shape)"),

    md("## 5. Learn the content -> latent projection (Ridge) on warm movies\n\n"
       "TF-IDF over the genre+keyword text gives each movie a sparse content vector; Ridge maps that\n"
       "to the 64-dim WMF item vector. We fit on warm movies (where we have a *true* latent vector)\n"
       "and apply to cold movies (where we don't)."),
    code("cmap = dict(zip(movie_content.movieId, movie_content.content))\n"
         "warm_text = [cmap[m] for m in i_cats]\n"
         "vec = TfidfVectorizer(max_features=2000)\n"
         "Xw = vec.fit_transform(warm_text)\n"
         "proj = Ridge(alpha=20.0)\n"
         "proj.fit(Xw, warm_item_f)\n"
         "r2 = proj.score(Xw, warm_item_f)\n"
         "print(f'content features: {Xw.shape[1]} | Ridge train R^2 to latent space: {r2:.3f}')"),

    md("## 6. Embed cold movies from content, build the cold-start eval\n\n"
       "Eval users = users with a warm-history factor who also rated >=1 cold movie. For each such\n"
       "(user, cold movie) we rank the true cold movie against 99 other cold movies the user didn't\n"
       "rate, scoring with `user_vector . predicted_cold_vector`."),
    code("cold_ids = sorted(cold_movies)\n"
         "c2idx = {m: k for k, m in enumerate(cold_ids)}\n"
         "cold_text = [cmap[m] for m in cold_ids]\n"
         "cold_f_proj = proj.predict(vec.transform(cold_text))      # content projection\n"
         "cold_f_mean = np.repeat(warm_item_f.mean(0, keepdims=True), len(cold_ids), axis=0)  # no-content baseline\n"
         "\n"
         "# (user, cold-item) eval pairs, only for users seen in warm training\n"
         "cold = cold[cold.userId.isin(uid2u)]\n"
         "user_cold = {u: set(g) for u, g in cold.groupby('userId').movieId}\n"
         "pairs = [(uid2u[u], c2idx[m], u) for u, m in zip(cold.userId, cold.movieId)]\n"
         "if len(pairs) > 20000:\n"
         "    sel = rng.choice(len(pairs), 20000, replace=False); pairs = [pairs[k] for k in sel]\n"
         "n_cold = len(cold_ids)\n"
         "print(f'{len(pairs):,} cold-start eval pairs over {n_cold:,} cold movies')"),
    code("def eval_cold(cold_factors):\n"
         "    hr = ndcg = 0.0\n"
         "    for uidx, citem, uid in pairs:\n"
         "        seen = user_cold[uid]\n"
         "        negs = []\n"
         "        while len(negs) < 99:\n"
         "            for x in rng.integers(0, n_cold, size=200):\n"
         "                xi = int(x)\n"
         "                if cold_ids[xi] not in seen and xi != citem:\n"
         "                    negs.append(xi)\n"
         "                    if len(negs) == 99: break\n"
         "        cand = np.array([citem] + negs)\n"
         "        s = cold_factors[cand] @ user_f[uidx]\n"
         "        # rank with RANDOM tie-breaking: a constant-score model must score ~random (0.10),\n"
         "        # not a fake perfect 1.0 from `>` counting zero ties.\n"
         "        nz = rng.random(len(s))\n"
         "        rank = int(((s > s[0]) | ((s == s[0]) & (nz > nz[0]))).sum())\n"
         "        if rank < 10:\n"
         "            hr += 1; ndcg += 1.0/np.log2(rank+2)\n"
         "    return hr/len(pairs), ndcg/len(pairs)\n"
         "\n"
         "r_proj, n_proj = eval_cold(cold_f_proj)\n"
         "r_mean, n_mean = eval_cold(cold_f_mean)\n"
         "print(f'{\"Cold-start strategy\":<28}{\"Recall@10\":>12}{\"NDCG@10\":>12}')\n"
         "print('-'*52)\n"
         "print(f'{\"No content (mean vector)\":<28}{r_mean:>12.4f}{n_mean:>12.4f}')\n"
         "print(f'{\"TMDB content projection\":<28}{r_proj:>12.4f}{n_proj:>12.4f}')"),

    md("**Takeaway:** projecting TMDB content features into the WMF latent space lets the model rank\n"
       "brand-new movies it has never seen an interaction for, well above the no-content baseline —\n"
       "a concrete solution to item cold-start. (A random ranking would score ~0.10 Recall@10.)"),
]


def run():
    nb = new_notebook(cells=NB06)
    nb.metadata["kernelspec"] = {"name": "python3", "display_name": "Python 3", "language": "python"}
    path = os.path.join(NB_DIR, "06-cold-start.ipynb")
    t = time.time()
    NotebookClient(nb, timeout=2400, kernel_name="python3",
                   resources={"metadata": {"path": NB_DIR}}).execute()
    nbf.write(nb, path)
    print(f"wrote 06-cold-start.ipynb in {time.time()-t:.1f}s")


if __name__ == "__main__":
    run()

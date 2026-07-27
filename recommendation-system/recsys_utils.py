"""
Shared utilities for the movie-recommender project.

Keeping the data-prep, leave-one-out split, and the He-et-al. (NCF) evaluation
protocol in ONE place means every notebook uses the *exact same* protocol, so the
popularity baseline, the library WMF, the from-scratch WMF and the cold-start model
are all comparable. This is also the single file to read when defending the
evaluation methodology in an interview.

Design decisions (locked in next-steps.md):
  - Task: top-N ranking (not rating prediction).
  - Implicit feedback: every observed rating is a positive; the rating *value*
    becomes the confidence weight  C_ui = 1 + alpha * r_ui   (Hu/Koren/Volinsky 2008).
  - Item filter: drop "consensus-bad" movies (>=80% of ratings below 2.5).
  - Split: leave-one-out per user -- the user's most recent interaction is the test item.
  - Metric: Recall@10 and NDCG@10 under the He-et-al. protocol
    (1 held-out positive vs 99 sampled negatives the user has not interacted with).
"""
import numpy as np
import scipy.sparse as sp

BAD_THRESHOLD = 2.5      # a rating below this counts as a negative vote
BAD_FRACTION = 0.80      # drop a movie if >= this fraction of its ratings are negative
MIN_USER_RATINGS = 5     # a user needs at least this many ratings to be usable
ALPHA = 40.0             # confidence scaling in C_ui = 1 + alpha * r_ui
DEFAULT_K = 10
DEFAULT_N_NEG = 99


def filter_consensus_bad(ratings):
    """Drop movies where >= BAD_FRACTION of ratings are below BAD_THRESHOLD.

    Rationale: a movie everyone dislikes is noise for a top-N recommender -- it should
    never be recommended, so it only adds parameters and slows training. We KEEP
    polarized movies (loved by some, hated by others); the latent-factor model is
    exactly the tool that learns *who* likes them.
    """
    is_bad = ratings.rating < BAD_THRESHOLD
    bad_frac = is_bad.groupby(ratings.movieId).mean()
    drop = set(bad_frac[bad_frac >= BAD_FRACTION].index)
    return ratings[~ratings.movieId.isin(drop)], drop


def reindex(ratings):
    """Map raw userId/movieId to contiguous 0..N-1 codes (rows/cols of the matrix)."""
    ratings = ratings.copy()
    u_cat = ratings.userId.astype("category")
    i_cat = ratings.movieId.astype("category")
    ratings["u"] = u_cat.cat.codes
    ratings["i"] = i_cat.cat.codes
    user_ids = u_cat.cat.categories.to_numpy()   # code -> raw userId
    movie_ids = i_cat.cat.categories.to_numpy()  # code -> raw movieId
    return ratings, user_ids, movie_ids


def leave_one_out_split(ratings):
    """Hold out each user's MOST RECENT rating (by timestamp) as the test item.

    Using the most-recent interaction (not a random one) mimics the real task:
    predict what the user will engage with *next* given their history.
    Test items whose movie never appears in the training set are dropped here
    (those are item-cold-start cases, handled separately in notebook 06).
    """
    ratings = ratings.sort_values("timestamp")
    last_idx = ratings.groupby("u").tail(1).index
    test = ratings.loc[last_idx]
    train = ratings.drop(last_idx)
    train_items = np.unique(train.i.values)
    test = test[test.i.isin(set(train_items.tolist()))]
    return train, test


def build_confidence_matrix(train, n_users, n_items):
    """Sparse users x items matrix whose stored values are the raw ratings r_ui.

    We store r_ui (not 1 + alpha*r) because the `implicit` library applies the
    `alpha` multiplier itself; the from-scratch model applies C_ui = 1 + alpha*r
    explicitly. Storing r keeps both consumers honest about the same input.
    """
    return sp.csr_matrix(
        (train.rating.values.astype(np.float32), (train.u.values, train.i.values)),
        shape=(n_users, n_items),
    )


def _sample_negatives(seen_indices, true_i, n_items, n_neg, rng):
    """Sample n_neg item ids the user has NOT interacted with (and != true item)."""
    blocked = set(seen_indices.tolist())
    blocked.add(int(true_i))
    negs = []
    while len(negs) < n_neg:
        draw = rng.integers(0, n_items, size=n_neg * 2)
        for x in draw:
            xi = int(x)
            if xi not in blocked:
                negs.append(xi)
                if len(negs) == n_neg:
                    break
    return negs


def build_eval_candidates(test_u, test_i, train_csr, n_items, n_neg=DEFAULT_N_NEG, seed=0):
    """Build the (n_test, 1 + n_neg) candidate matrix: column 0 is the true item.

    Returned once and reused by every model so all models rank the *same* candidates.
    `test_u` / `test_i` are 1-D arrays of user codes and held-out item codes.
    """
    rng = np.random.default_rng(seed)
    tu = np.asarray(test_u)
    ti = np.asarray(test_i)
    cands = np.empty((len(tu), n_neg + 1), dtype=np.int64)
    cands[:, 0] = ti
    for row, (u, t) in enumerate(zip(tu, ti)):
        seen = train_csr.indices[train_csr.indptr[u]:train_csr.indptr[u + 1]]
        cands[row, 1:] = _sample_negatives(seen, t, n_items, n_neg, rng)
    return tu, cands


def score_metrics(scores, k=DEFAULT_K, seed=0):
    """Given (n, 1+n_neg) scores with the true item in column 0, return Recall@k, NDCG@k.

    Single relevant item per user, so:
      Recall@k == Hit@k  (is the true item in the top k of its 100 candidates?)
      NDCG@k   == 1/log2(rank+2) when hit, else 0.

    Ties are broken RANDOMLY (not in the true item's favour). This matters for models with
    discrete scores -- e.g. the popularity baseline scores by integer interaction counts, so
    many candidates tie; a naive `score > true` would count zero ties and hand the true item a
    fake rank 0. Random tie-breaking gives a constant-score model its honest ~k/100 hit rate.
    """
    rng = np.random.default_rng(seed)
    noise = rng.random(scores.shape)
    true_s = scores[:, [0]]
    true_n = noise[:, [0]]
    beats = (scores > true_s) | ((scores == true_s) & (noise > true_n))  # col 0 never beats itself
    ranks = beats.sum(axis=1)  # 0-based rank of the true item among its candidates
    hit = ranks < k
    recall = float(hit.mean())
    ndcg = float(np.where(hit, 1.0 / np.log2(ranks + 2), 0.0).mean())
    return recall, ndcg


def score_als(user_factors, item_factors, users, cands, batch=4096):
    """Score ALS candidates: dot(user_vec, item_vec) for each (user, candidate).

    Batched over users to keep peak memory bounded (the gathered item factors are
    the memory hog: batch x 100 x factors).
    """
    n = len(users)
    out = np.empty(cands.shape, dtype=np.float32)
    for s in range(0, n, batch):
        e = min(s + batch, n)
        uf = user_factors[users[s:e]]                 # (b, f)
        vf = item_factors[cands[s:e]]                 # (b, 100, f)
        out[s:e] = np.einsum("bf,bcf->bc", uf, vf)    # (b, 100)
    return out


def score_popularity(item_pop, cands):
    """Popularity baseline: every candidate scored by its training interaction count."""
    return item_pop[cands].astype(np.float32)

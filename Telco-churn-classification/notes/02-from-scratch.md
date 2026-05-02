# Project 2 — LR from Scratch (Notebook 04) — Saturday Deliverable


## What I built

- Logistic regression from scratch in numpy: `sigmoid`, `compute_cost` (log loss), `compute_gradient`, `gradient_descent`.
- No sklearn for the model itself. Sklearn used only for `train_test_split` and metrics.
- **Verified correct by reproducing Notebook 02's sklearn baseline metrics exactly on the test set.**

## Pipeline + training config

- Same data prep as Nb 02/03 (no §4 collapse — v1 baseline consistency).
- `pd.get_dummies(drop_first=True, dtype="int")` for categoricals.
- **Per-column z-score normalization** (after a critical bug fix — see Reflection §2).
- `α = 0.3`, `num_iters = 10000`.
- Final training cost: **0.4126** (plateaued by ~iter 1000, refined slightly through 10K).

## Results — exact match to Nb 02

| Metric          | Nb 02 (sklearn, C=1.0) | Nb 04 (from scratch, no reg) | Match? |
|-----------------|------------------------|------------------------------|--------|
| Accuracy        | 0.8055                 | 0.8055                       | ✅ exact |
| F1 (positive)   | 0.6040                 | 0.6040                       | ✅ exact |
| ROC-AUC         | 0.842                  | 0.8424                       | ✅ within rounding |
| Confusion matrix | `[[926, 109], [165, 209]]` | `[[926, 109], [165, 209]]` | ✅ identical |

**Every test-set classification matches Nb 02 byte-for-byte.** The implementation is correct.

## Comparison to sklearn(C=1e10) — the implicit-regularization finding

Fitting `sklearn.LogisticRegression(C=1e10, solver='lbfgs', max_iter=100000)` on the *exact same normalized matrix*:

| Diff metric vs sklearn(C=1e10) | Value |
|---|---|
| Max absolute prediction diff | 0.059 |
| Mean absolute prediction diff | 0.0066 |

So my from-scratch model:
- Matches sklearn(**C=1.0**) — *regularized* — exactly in classifications.
- Does NOT match sklearn(**C=1e10**) — *unregularized* — within 1e-3.

Even though my model has *no explicit regularization*. **What's going on**: see Reflection §3.

## α experiment — three regimes observed

| α    | iters | final cost | observation |
|------|-------|------------|-------------|
| 0.5  | 100k  | ~0.460     | undertrained — cost still decreasing |
| 3    | 100k  | 0.457      | converged |
| 5    | 100k  | 0.455      | converged (sweet spot for this data) |
| **7** | 100k | **0.468**  | **bouncing regime** — plateaus higher than smaller α |
| 0.3  | 1M    | 0.4126     | converged (just slow) |
| **0.3** | **10k** | **0.4126** | **converged in only 10K iters** — after fixing scaling bug |

**Three regimes seen empirically**:
1. **Undertrained**: α too small or iters too few → cost still descending at cutoff.
2. **Converged**: α in a range that lets steps shrink properly near the minimum → reaches actual minimum.
3. **Bouncing (α=7)**: steps too large → near the minimum, each step *overshoots* and lands at a slightly higher-cost point on the other side. Optimizer oscillates between two near-optimal points without ever reaching the actual bottom. **Doesn't diverge** (cost doesn't blow up), but *plateaus higher than achievable*.

Critical observation: after fixing the scaling bug, **α=0.3 with just 10K iters reaches a cost of 0.4126** — meaningfully lower than any of the broken-scaling runs. *Most of the convergence pain on the broken-scaling pipeline was the input being unreasonable, not the optimizer being slow.*

---

## Reflection — four stories

### §1 — The calculus gap (and what I did about it)

Honest answer to "hardest part of the gradient derivation": **I didn't derive it cold.** — at this point I don't yet have the multivariate-chain-rule + sigmoid-derivative-trick fluency to derive

`dL/dw = (1/m) · X.T @ (σ(Xw + b) − y)`

from the log-loss

`L = −(1/m) · Σ [y · log(p) + (1−y) · log(1−p)]`

on paper, where `p = σ(Xw + b)`.

What I did instead: read the derivation, understood the key cancellation (`σ'(z) = σ(z)·(1 − σ(z))` cancels the `1/p` and `1/(1−p)` from the log-derivative, leaving the clean `(p − y)` form), and implemented it in numpy. Tested by checking `compute_cost` returns `log(2) ≈ 0.6931` for `w=0, b=0` (right answer for "no information" predictions) and watching the cost decrease monotonically during training.


### §2 — The scaling bug — most important lesson of the day

I spent over a million GD iterations, ran an entire α experiment, and chased a 5%+ prediction discrepancy with sklearn before realizing the actual problem.

My custom `z_score_normalization` function called `np.mean(X)` and `np.std(X)` on a pandas DataFrame **without `axis=0`**. On a DataFrame with mixed columns, this returned **single scalars** — the global mean and std across *all values in all features mashed together* — instead of per-column Series.

```python
# What I had — silently broken
mu = np.mean(X)           # → scalar 80.18 (mean of EVERYTHING)
sigma = np.std(X)         # → scalar 585.79
X_norm = (X - mu) / sigma # → every value shifted/scaled by same numbers

# Diagnosis
print(type(mu))           # numpy.float64  ← bug
# Fixed:
mu = np.mean(X, axis=0)   # → Series of per-column means
```

What this did to my features:
- `tenure` (range 0–72) → all values squashed into roughly `[−0.137, −0.014]` — almost no variance left.
- `MonthlyCharges` (range 18–118) → roughly `[−0.106, +0.065]` — nearly flat.
- Binary 0/1 dummies → either `−0.137` or `−0.135` — **essentially indistinguishable**.
- `TotalCharges` (range 0–8684) → roughly `[−0.137, +14.7]` — **still dominates the entire feature space**.

The model wasn't learning much from anything except `TotalCharges`. Effectively a 1-feature LR. No error, no warning — just degraded performance and a 5%+ prediction gap I couldn't explain.

After fix: same α=0.3 but only 10K iters → reproduced sklearn baseline exactly.

### §3 — Implicit regularization (the surprise)

After the scaling fix, my from-scratch model — which has **no regularization** — produced classifications **exactly** matching `sklearn.LogisticRegression(C=1.0)` (which has *L2 regularization* enabled by default). Same confusion matrix, same metrics to 4 decimal places.

But my predictions differed from `sklearn.LogisticRegression(C=1e10)` (effectively *unregularized* sklearn) by up to ~6% in absolute terms.

This was confusing at first — how can my no-regularization model act like a regularized one?

**The answer: finite-iteration GD is itself a form of regularization.**

My GD with α=0.3 plateaued at training cost 0.4126 by iter ~1000 and barely budged through iter 10000. That plateau is **not** the actual unregularized minimum. The true unregularized minimum (which sklearn's LBFGS reaches with second-order curvature info) is slightly lower, with weights of *larger magnitude*. My GD ran out of meaningful steps before getting there — its weights stayed *closer to zero* than the true optimum.

Smaller weights = same effect as L2 regularization (which explicitly penalizes `‖w‖²`). So my "early-stopped GD" and sklearn's "explicit L2 with C=1.0" landed on essentially the same point through *different mechanisms*:
- **Sklearn**: explicit `λ‖w‖²` penalty pulls weights toward zero.
- **My GD**: finite iterations don't have enough "time" to push weights all the way to the unregularized optimum.

This is well-documented in ML literature: **"early stopping ≈ implicit L2 regularization"**.

**Why classifications match Nb 02 exactly despite probability differences with C=1e10**: a 0.06 max abs diff in probability only changes a classification if a row's probability crosses 0.5. Most predictions are confident (probabilities near 0 or 1) and the small global shift doesn't move many rows across the threshold. My model and sklearn(C=1.0) agree on every test row's classification, even though their probabilities differ slightly. The agreement is *threshold-stable*, not probability-identical.

### §4 — α and divergence — the math behind the bouncing regime

GD update rule: `w_new = w − α · ∇L`. The step size in weight-space is `α · |∇L|`.

Near the minimum, `∇L` is small but nonzero. Whether GD actually settles into the minimum depends on the relationship between α and the local curvature (second derivative / Hessian). For a quadratic loss with curvature `H`, the critical learning rate is `α* ≈ 2/H_max`. Below that → convergence. Above that → divergence. **In between sits the "bouncing regime"** — α is too large to converge to the minimum but not large enough to diverge: every step jumps past the minimum to a slightly higher-cost point on the other side, and the optimizer oscillates between two points without ever landing at the actual minimum.

That's what α=7 was doing in my experiment. α=15 or α=20 would likely have actually diverged (cost growing unbounded → NaN). I sat at the *edge* of divergence without quite tipping over.

**Connection to deep learning**: this is exactly the "exploding gradient" mechanism in deep nets. Each step amplifies the next step → cost grows unbounded → training fails. The fix in DL is gradient clipping and adaptive optimizers (Adam, RMSprop) that auto-scale step sizes. Same mechanism, propagated through layers.

---

## Files

- `model/04-logistic-regression-from-scratch.ipynb` — this notebook, Saturday deliverable
- `notes/01-eda-and-baseline.md` — Notebook 02/03 baseline, EDA decisions, single-split + CV results
- `notes/02-from-scratch.md` — this file

---

*Created: May 2, 2026 (Saturday Wk 3, Phase 1 LR-from-scratch deliverable).*

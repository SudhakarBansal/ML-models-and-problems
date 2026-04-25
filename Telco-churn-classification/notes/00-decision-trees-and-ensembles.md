# Decision Trees & Ensembles — Depth Reference

> Permanent reference for tree-based methods. Built from the 5-question depth check after Course 2 W4 + StatQuest revision (Apr 25, 2026).
>
> Re-read this file every Sunday spaced-review cycle. If any answer reads fuzzy on re-read, fix it that day.

---

## Q1: Why don't tree models need feature scaling?

**Short answer:** Trees compare *within* one feature; LR/NN sum *across* features. Cross-feature arithmetic is what makes scale matter.

### Tree mechanism at one split
A decision tree node performs a **yes/no test on a single feature against a threshold drawn from that feature's own values** — e.g., `is income > 50,000?`. The threshold lives in the feature's own units, so the scales of other features never enter the calculation. Random Forest and XGBoost inherit this property because they're built from the same kind of splits.

### Why LR / NN do need scaling
LR and NN compute a **weighted sum across all features**: `z = w₁·x₁ + w₂·x₂ + … + b`. When features sit on wildly different scales (e.g., `age ∈ [0, 100]` vs `income ∈ [10K, 10M]`):
- The gradient of the cost w.r.t. weights is dominated by the large-scale feature.
- A single global learning rate can't be simultaneously right for small-scale and large-scale weights → unstable updates, slower convergence, sometimes worse accuracy.

That's why `StandardScaler` / `MinMaxScaler` is mandatory before LR/NN training, while trees are scale-invariant by construction.

---

## Q2: Bagging vs Boosting — mechanisms, what each reduces, and what RF randomizes beyond bagging

### Bagging (Bootstrap AGGregating)
- **Bootstrap step**: from the training set of N rows, draw N rows **with replacement** to form a new bootstrap dataset. ~63% of unique rows show up; some are duplicated, ~37% are left out (out-of-bag, useful for free validation). Repeat to make B different bootstrap datasets.
- **Aggregating step**: train one tree on each bootstrap dataset (B trees total). For prediction: average predictions for regression, majority vote for classification.
- **What it reduces: variance.** Averaging N independent models reduces variance by a factor of N — but only if the models are independent. Bagged trees on the same features are NOT fully independent (see RF below).

### Boosting — two distinct flavors, often confused

**AdaBoost** (the one I keep wrongly defaulting to)
- Trees are **stumps** (depth = 1).
- After each stump, **sample weights are updated**: misclassified examples get larger weights, correctly classified ones get smaller weights. The next stump is trained on the reweighted dataset.
- Final prediction = weighted vote across all stumps (each stump's vote weighted by its accuracy).

**Gradient Boosting** (and its descendants: XGBoost, LightGBM)
- Trees are **deeper** (depth typically 4-8), not stumps.
- **Sample weights are NOT updated.** Instead: each new tree is trained to predict the **residual** of the ensemble's current prediction. Residual = `(actual − current prediction)`.
- For MSE loss, the residual literally IS the negative gradient of the loss w.r.t. the prediction → "gradient" boosting. For other losses (log-loss for classification), the new tree fits the gradient of the loss directly.
- Final prediction = sum of all tree predictions (scaled by a learning rate).

**Key contrast to keep straight:**
| | AdaBoost | Gradient Boosting |
|---|---|---|
| Tree shape | Stumps (depth 1) | Deeper trees (depth 4-8) |
| What changes between trees | Sample **weights** are updated | Sample **target** changes (becomes the residual) |
| Aggregation | Weighted vote | Sum of predictions |

- **What boosting reduces: bias.** Each new tree corrects the ensemble's previous mistakes, so the model gets progressively closer to the true function. Risk: can overfit if too many trees.

### Random Forest — what it randomizes BEYOND bagging

RF = bagging (rows) + **per-split feature subsampling** (columns).

- The row sampling is plain bagging, just like above.
- The column sampling is the critical detail: **at every single split node** — root, child, grandchild, every node in every tree — RF samples a fresh random subset of features (typically √p for classification, p/3 for regression, where p = total features) and picks the best split among ONLY those candidates. Then it builds the next split node and re-samples features again. Per-split, not per-tree.

**Why per-split matters — the decorrelation argument:**
- Plain bagged trees → every tree picks the same single strongest feature as the root split → trees highly correlated → averaging them barely helps.
- Per-tree feature sampling → root splits diverge, but within each tree, the same "next best feature in the subset" gets reused at every depth → still partial correlation.
- Per-split feature sampling → at the root of one tree, the strongest predictor might not even be in the candidate set → forces a different split. Different splits at different depths consider different features. Trees become genuinely decorrelated → variance reduction kicks in fully.

This is the detail that separates "I read about RF" from "I understand RF." It's also the answer to "why doesn't bagging alone achieve what RF achieves?"

---

## Q3: How do Random Forest trees become different *enough* to make the ensemble help?

### Two compounding sources of randomness

1. **Bootstrap row sampling (from bagging).** For every tree, draw N rows with replacement from the training set. Each tree ends up seeing roughly 63% of the unique rows; the rest are out-of-bag. Different trees see different row samples → different trees would learn different splits even if the feature set were fixed.

2. **Per-split feature subsampling (RF's special sauce).** At every split node inside every tree, RF samples a fresh random subset of features (~√p classification, p/3 regression) and picks the best split among only that subset. This forces trees to diverge even when they share rows.

Either source alone is weaker than the combination:
- **Just bagging** (row sampling, all features available): every tree picks the single strongest predictor as the root split → trees stay highly correlated.
- **Just feature sampling** (no bootstrap): identical training rows pull trees toward similar splits despite the feature randomness.
- **Both together**: trees disagree on rows AND disagree on candidate features at each split → genuine decorrelation.

### Why correlated trees don't help (the intuition)

If all 100 trees produce the same prediction, averaging them is no better than using one tree. "Same opinion ×100 = same opinion." The whole point of an ensemble is that different trees make *different mistakes* on different rows, so when you average, the wrong predictions cancel out and the right ones reinforce.

The math says it explicitly: variance of the average of N predictions = (1/N)·variance + ((N−1)/N)·covariance. If trees are perfectly correlated (covariance = variance), the ensemble's variance equals a single tree's variance — averaging buys nothing. The lower the correlation, the more the (1/N) term dominates and variance shrinks toward zero.

So RF's two-layer randomization isn't decoration — it's the entire reason the ensemble outperforms a single tree.

---

## Q4: Gini vs Entropy as splitting criteria

### Both are impurity measures, doing the same operation

Both Gini and entropy measure how "mixed" the classes are at a node. The tree picks the split that **maximally reduces** impurity from parent to weighted-average children:
- **Gini gain** = `Gini(parent) − Σ (n_child/n_parent) · Gini(child)`
- **Information gain** = `Entropy(parent) − Σ (n_child/n_parent) · Entropy(child)`

Same operation. Different impurity function. There is no "Gini = minimize purity, Entropy = maximize information gain" distinction — that's a misframing.

### Do they produce different trees in practice?

**Almost never.** Empirically, Gini and Entropy disagree on maybe ~2% of split decisions, and the resulting trees perform near-identically. Both functions are concave, both peak when classes are balanced, both bottom out at pure nodes — so they rank candidate splits very similarly.

### Which is the default — and why?

**Gini is sklearn's default**, because Gini = `1 − Σ pᵢ²` involves only multiplication and addition, while Entropy = `−Σ pᵢ · log₂(pᵢ)` requires log computations → Entropy is slightly more expensive. For large datasets / many splits, Gini wins on speed. Both are decades old (Gini coefficient: 1912; Shannon entropy: 1948). Neither is "more modern."

### Shape of entropy

**Binary classification** (p = probability of class 1):
- `H(p) = −p·log₂(p) − (1−p)·log₂(1−p)`
- Maximum at **p = 0.5**, where `H = 1 bit` (perfect uncertainty).
- Minimum (= 0) at **p = 0 or p = 1**, where the node is pure.
- Shape: an inverted-bowl curve, symmetric around p = 0.5.

**3-class classification:**
- `H(p₁, p₂, p₃) = −Σ pᵢ · log₂(pᵢ)` over all three classes.
- Inputs live on a triangle (2-simplex) of valid probability distributions.
- **Maximum at the centroid** (p₁ = p₂ = p₃ = 1/3), giving `H = log₂(3) ≈ 1.585 bits`.
- **Zero at the three corners** (one class has p=1).

**General K-class:** max entropy = `log₂(K)`, achieved when all classes are equally likely.

### Gini shape (for completeness)

**Binary**: `Gini(p) = 1 − p² − (1−p)² = 2p(1−p)`. Maximum at p=0.5 where `Gini = 0.5`. Zero at p=0 or p=1. Same inverted-bowl character as entropy, just slightly different curvature.

---

## Q5: In gradient boosting, what does each new tree predict? How does this differ from AdaBoost?

> ⚠️ This was the weakest area on first depth check AND second pass. **Re-drill in Sunday spaced review for at least 3 weeks.** Re-watch StatQuest Gradient Boost Part 1 if anything below feels fuzzy on re-read.

### Each new tree fits the RESIDUALS of the ensemble's current prediction.

Residual = `y − F_current(x)` — i.e., the gap between the actual target and what the ensemble currently predicts. Not "wrong examples." Not "reweighted samples." A continuous-valued correction signal computed for **every training row** at every iteration.

### Algorithm step-by-step

1. **F₀ (baseline)**: predict the average of y for every row. F₀ is a constant — *no tree exists yet*.
2. **Compute residuals**: r₁ = y − F₀ (for every row).
3. **Train Tree 1**: a regression tree (typical depth 4-8, NOT a stump) fitted to predict r₁.
4. **Update ensemble**: F₁ = F₀ + η · Tree₁(x), where η is a small learning rate (commonly 0.1).
5. **New residuals**: r₂ = y − F₁ (every row gets a fresh residual).
6. **Train Tree 2** to predict r₂. Update: F₂ = F₁ + η · Tree₂(x).
7. Continue for M trees. **Final prediction**: F_M = F₀ + η · Σ Tree_m(x).

The learning rate η shrinks each tree's contribution → the ensemble takes many small corrective steps rather than a few big ones. Smaller η + more trees usually generalizes better.

### Why "gradient" boosting?

For MSE loss, the residual `y − F_current` literally equals the negative gradient of the loss with respect to the prediction: `−∂L/∂F = y − F`. Fitting the residual = taking a step in the direction that reduces loss. For other losses (log-loss in classification, Huber loss for robust regression), the new tree fits the **gradient of the loss** directly — same general idea, different concrete formula. Hence "gradient" boosting.

### Contrast with AdaBoost — the central distinction

| | AdaBoost | Gradient Boosting |
|---|---|---|
| What changes between iterations? | Sample **weights** (misclassified rows weighted higher) | Sample **target** (becomes the residual y − F_{m-1}) |
| Tree shape | Stumps (depth 1) | Deeper trees (depth 4-8) |
| Final prediction | Weighted vote of all stumps | Sum of all tree outputs (with learning rate) |
| Loss optimized | Exponential loss (specific) | Any differentiable loss (general) |

**Mental hook**: AdaBoost reweights *rows*. Gradient boost reweights the *target*. Different mechanism, similar overall goal (each new model corrects what's left over).

### Why GB trees are deeper than AdaBoost stumps

Each AdaBoost stump is a weak learner — does just slightly better than random. The ensemble combines many weak votes. Gradient boost's trees fit residuals, which can have intricate patterns the ensemble hasn't captured yet → deeper trees model those patterns. But not too deep, or one tree overfits the noise in the residuals.

---

## Sunday review checklist (re-read this section every spaced-review cycle)

For each of Q1–Q5, before you re-read the answer:
1. Close this file. Try to state the one-liner from memory.
2. If you can't → that one needs deeper drill, schedule a re-attempt.
3. **Q5 specifically**: walk through the gradient boosting algorithm step-by-step from F₀ to F_M without peeking. Verify residuals appear in every step.

Last updated: Apr 25, 2026 (after StatQuest revision + 5-question depth re-check).

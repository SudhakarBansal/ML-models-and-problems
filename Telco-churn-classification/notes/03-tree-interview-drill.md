# Trees & Ensembles — Interview Drill & Resume Log

> Mock-interview practice file. Created Jun 10, 2026 after a 17-question live mock.
> **How to use:** cover the answers, ask yourself each question out loud, then check.
> The point is not "do I know it" — it's "can I say it in *precise* terms under pressure."

---

## ⚠️ My recurring weakness (read this first, every time)

Across the whole mock, the pattern was the same: **intuition correct, terminology imprecise.**
I reason to the right *conclusion* but reach for the loose word instead of the exact one. That's
the gap between "read about it" and "can defend it" — i.e. exactly the mentor-track depth bar.

Concrete examples from the mock where I was right-ish but not interview-precise:
- Said boosting trees fit "the errors" → correct term is **negative gradient / pseudo-residuals**.
- Said a tree can't reach $700K because it's "sensitive to outliers" → real reason is **a leaf
  outputs the average of its training rows, so predictions are bounded by the training range
  (no extrapolation)**.
- Guessed feature importance was *low* for influential features → it's **high** for features used
  in **top splits** that cut impurity a lot.
- Called entropy "stricter than Gini" → they're **both impurity measures**, nearly identical.

**Drill instruction: when an answer below is in bold, that's the word the interviewer is listening
for. Say the bold word, not a paraphrase.**

---

## Part A — Resume log: the 17 mock questions, scored

Legend: ✅ solid · 🟡 right idea, imprecise · ❌ didn't know

| # | Question | Score | The one fix |
|---|----------|-------|-------------|
| 1 | Classification split criteria + regression criterion | 🟡 | Named Gini/entropy but not "impurity"; **missed regression = MSE/variance reduction** |
| 2 | Why full-depth tree overfits + 2 hyperparameters | 🟡 | Intuition good; **couldn't name hyperparameters** (see Part C-1) |
| 3 | Bagging vs boosting + which reduces variance/bias | ✅ | Forgot to state **bagging→variance, boosting→bias** explicitly |
| 4 | RF's extra trick beyond bagging | ✅ | Word is **decorrelation** via per-split feature subsampling |
| 5 | What each GB tree predicts (precise) | 🟡 | Said "errors" → **negative gradient / pseudo-residuals** |
| 6 | XGBoost vs vanilla GBM (2 additions) | ❌ | See Part C-3 |
| 7 | Train 99% / val 72% — diagnose + fix | ✅ | Trap: **more trees won't fix it** |
| 8 | Single tree more interpretable? trade-off | ✅ | — |
| 9 | RF "which features mattered" | ❌ | **Feature importance**; top splits = HIGH (I had it backwards) |
| 10 | Learning rate / shrinkage | ✅ | **Low LR + many trees = better generalization** |
| 11 | Do trees need feature scaling? | ✅ | **Splits depend on order, not magnitude** |
| 12 | Imbalanced churn, 90% acc trap | ✅ | Metric = **accuracy**; fix = class_weight / resample / threshold |
| 13 | Regression tree, $700K extrapolation | 🟡 | Right answer, **wrong reason** (leaf average, not outliers) |
| 14 | One-hot 1000 cities — why bad for trees | 🟡 | **One-city-at-a-time splits fragment signal** |
| 15 | RF vs XGBoost — when to pick which | 🟡 | Gave bias/variance; wanted **practical** trade-off (Part C-4) |
| 16 | The "free" RF validation score | ❌ | **OOB (out-of-bag)** — the ~37% unseen rows |
| 17 | Early stopping in boosting | 🟡 | Stops **adding trees** (not depth); signal = **val loss stops improving** |

**Resume point for next session: re-attempt #1, #5, #6, #9, #13, #14, #16, #17 cold.**

---

## Part B — Topics ALREADY in my permanent notes (00-decision-trees-and-ensembles.md)

Don't re-learn these — re-*retrieve* them faster. They're solid on paper, they just didn't
come out crisp under pressure:
- Gini vs entropy = impurity measures, Gini is sklearn default (cheaper, no log) — `00 §Q4`
- Bagging = bootstrap+aggregate → variance ; boosting = sequential residuals → bias — `00 §Q2`
- RF = bagging + per-split feature subsampling → decorrelation — `00 §Q2-Q3`
- GB fits residuals = negative gradient; AdaBoost reweights rows — `00 §Q5`
- No feature scaling for trees (order, not magnitude) — `00 §Q1`

---

## Part C — Gaps NOT in my notes yet (the real homework)

### C-1. Hyperparameters & overfitting control
**Pre-pruning (stop the tree growing):**
- `max_depth` — cap tree height
- `min_samples_split` — min rows needed to split a node
- `min_samples_leaf` — min rows that must land in a leaf
- `max_leaf_nodes`, `min_impurity_decrease` — cap growth / require minimum gain
- `max_features` — (RF) features considered per split; lower = more decorrelation

**Post-pruning:** `ccp_alpha` — **cost-complexity pruning**: grow full tree, then prune back the
branches whose accuracy gain doesn't justify their complexity (this is the "regularization
penalty" for trees).

**Trap (Q7):** with a Random Forest overfitting, **adding more trees does NOT close the
train/val gap** — averaging reduces variance from the ensemble but each tree still overfits.
Fix with min_samples_leaf ↑, max_depth ↓, max_features ↓.

### C-2. Splitting criteria — the full set
- Classification: **Gini** (`1 − Σpᵢ²`) or **entropy** (`−Σpᵢlog₂pᵢ`) — both impurity.
- Regression: **MSE / variance reduction** (default) or **MAE**. ← was missing from my notes.

### C-3. XGBoost vs vanilla Gradient Boosting
Two-liner that scores:
- **Objective/math side:** explicit **L1/L2 regularization on leaf weights** (vanilla GBM has
  none — this is the headline), and uses **second-order info (gradient + Hessian / Newton step)**.
- **Engineering side:** **parallelized histogram-based split finding**, **native missing-value
  handling** (learns a default direction), cache-aware / out-of-core for big data.

### C-4. RF vs XGBoost — when to use which (practical)
- **Random Forest:** parallel (fast), hard to overfit, strong **out-of-the-box with little
  tuning**. → strong baseline fast.
- **XGBoost:** usually **higher accuracy**, but sequential, **needs tuning**, easier to overfit.
  → when optimizing for the last few points and you have time + a validation setup.
- One-liner: *"RF for a strong low-effort baseline; XGBoost when I can tune for max accuracy."*

### C-5. Feature importance
- **Gini/impurity importance** (default): feature scores high if, summed over all trees, its
  splits reduced impurity a lot → features near the **top** of trees score **high**.
- **Permutation importance**: shuffle one feature's values, measure accuracy drop. Big drop =
  important. More reliable; not biased toward high-cardinality features the way Gini importance is.

### C-6. OOB (out-of-bag) score
Each tree trains on a bootstrap sample ≈ 63% of rows; the ~**37%** it didn't see are "out-of-bag."
Predict each row using only the trees that didn't train on it → free validation, no hold-out set.

### C-7. Trees can't extrapolate
A tree/RF predicts a **constant per leaf = average of that leaf's training rows**, so predictions
are **bounded by the training target range**. Outside the observed range it outputs a flat value;
it cannot project a trend the way a linear model does.

### C-8. Categorical handling
- sklearn trees: need encoding; **one-hot of high-cardinality** features forces **one-city-at-a-
  time splits** that fragment signal across sparse columns.
- **LightGBM / CatBoost**: handle categoricals natively, can split a category into **two groups in
  one split** — far more powerful than one-hot.

### C-9. Early stopping (boosting)
Stops **adding boosting rounds (trees)** — *not* tree depth. Signal: **validation loss stops
improving for N rounds (patience)** → keep best round. Prevents later trees from fitting **noise**.

---

## Part D — Common interview question bank (broader than the mock)

Grouped by theme. Use as a fresh question source next session.

### Decision trees (fundamentals)
1. How does a tree decide where to split? (impurity gain — Gini/entropy/MSE)
2. Gini vs entropy — difference, default, do they give different trees? (≈identical; Gini default)
3. Why does a full-depth tree overfit? Pre- vs post-pruning?
4. Do trees need feature scaling? Why not?
5. What kind of decision boundary does a tree produce? (**axis-aligned / staircase**)
6. Can a tree extrapolate? (No — leaf averages, bounded range)
7. How does a tree handle a continuous feature? (sorts values, tries midpoints as thresholds)

### Random Forest / bagging
8. What is bootstrapping? How much data does each tree see? (~63% in-bag, ~37% OOB)
9. What does RF randomize beyond bagging, and why? (per-split features → decorrelation)
10. Bagging reduces variance or bias? Why averaging helps only if trees are decorrelated.
11. What is the OOB score?
12. How do you read feature importance from an RF? Gini vs permutation, and Gini's bias.
13. Does adding more trees overfit an RF? (No — but doesn't fix per-tree overfit either)

### Boosting / GBM / XGBoost
14. Bagging vs boosting — mechanism + bias/variance.
15. AdaBoost vs Gradient Boosting — what changes between iterations? (weights vs target/residual)
16. What does each GB tree fit? Why is it called "gradient" boosting?
17. Role of learning rate / shrinkage; LR vs n_estimators trade-off.
18. What does XGBoost add over vanilla GBM? (regularization, 2nd-order, engineering)
19. XGBoost vs LightGBM? (**leaf-wise vs level-wise growth**, histogram speed)
20. Early stopping in boosting — what/signal/why.
21. Is GBM sensitive to outliers? (Yes — fits residuals, chases them; RF is more robust)
22. Why is boosting more prone to overfitting than bagging?

### Practical / modeling
23. RF vs XGBoost — when to pick which.
24. Why do trees beat linear models on tabular data? (auto non-linear **interactions**)
25. Handling categorical features in trees (one-hot pitfalls; native handling in LGBM/CatBoost).
26. Handling missing values (XGBoost/LightGBM default direction; sklearn needs imputation).
27. Imbalanced classes with trees — metrics + fixes (class_weight / scale_pos_weight / SMOTE /
    threshold; prefer **PR-AUC, recall** over accuracy).
28. How would you tune an XGBoost model? (learning_rate↓ + n_estimators↑, max_depth, subsample,
    colsample_bytree, min_child_weight, reg_lambda/alpha; use early stopping on a val set).

### Curveballs
29. Your RF and XGBoost give similar accuracy but RF trains 5× faster — which ship? Why?
30. A single feature has 90% importance — is that good or a red flag? (possible **leakage**)
31. Train acc 100%, val acc 70% on an XGBoost — what knobs, in what order?
32. Can trees give probability estimates? How calibrated are they? (leaf class fractions; often
    need calibration — Platt / isotonic)

---

## Part E — Next-session protocol

1. Re-attempt the 8 flagged questions from Part A **cold** (no peeking): #1, 5, 6, 9, 13, 14, 16, 17.
2. Then pull 5 random questions from Part D you haven't said out loud yet.
3. For any answer where I used a loose word, write the **bold precise term** in the margin.
4. Move anything I now own permanently into `00-decision-trees-and-ensembles.md`; this file is the
   scratch/drill log, that file is the permanent reference.

*Created: Jun 10, 2026. Source: 17-question live mock + gap analysis vs notes 00/01/02.*

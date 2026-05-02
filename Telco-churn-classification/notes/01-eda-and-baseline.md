# Project 2 — Telco Churn — EDA + Baseline


## Data

- **Source**: `WA_Fn-UseC_-Telco-Customer-Churn.csv` (Kaggle / IBM sample)
- **Shape**: 7,043 rows × 21 cols → after cleaning: 7,043 × 20 (dropped `customerID`)
- **Target**: `Churn` (Yes/No → 1/0)
- **Class balance**: ~26% positive (Churn=Yes), ~74% negative (Churn=No) — imbalanced

## Cleaning decisions

- **`customerID` dropped** — pure identifier, no signal, leakage risk if the model memorized IDs.
- **`TotalCharges` → numeric, `fillna(0)`** — column came in as `object` because some rows had blank strings. Investigation showed those rows have `tenure=0` (brand-new customers who haven't been billed). `0` is the semantically correct fill — they literally haven't paid anything yet. (Revisit: a `NaN`-and-keep-flag approach might preserve more signal than coercing to 0.)
- **`SeniorCitizen` 0/1 → "Yes"/"No"** — pipeline routing hygiene. Once I switched to `ColumnTransformer` with separate numeric/categorical paths, the dtype determines which transformer applies. As `int64`, `SeniorCitizen` would have gone through `StandardScaler` with continuous features (semantically wrong even if mathematically harmless). As `object`, it routes through `OneHotEncoder`.
- **§4 collapse ("No internet service" / "No phone service" → "No") — DEFERRED to v2 iteration**. Current baseline keeps these as separate OHE categories. Decision: comparing Notebook 02 (single-split) vs Notebook 03 (CV) is only meaningful on the same feature matrix; collapsing in one but not the other muddies the experimental design. v2 baseline (next iteration) will collapse and re-fit, isolating the §4 effect from sampling variance.

## Pipeline (Notebook 02 + 03)

```python
ColumnTransformer:
  cat → OneHotEncoder(handle_unknown='ignore', drop='if_binary')
  num → StandardScaler()
+ LogisticRegression(max_iter=1000, penalty='l2', C=1.0)  # sklearn defaults — L2 active by default
```

## Results — Notebook 02 (single 80/20 stratified split, `random_state=42`)

| Metric    | Value  |
|-----------|--------|
| Accuracy  | 0.8055 |
| Precision | 0.657  |
| Recall    | 0.559  |
| F1        | 0.604  |
| ROC-AUC   | 0.842  |

**Confusion matrix**:
```
              Pred No   Pred Yes
True No  →   926       109
True Yes →   165       209
```

## Results — Notebook 03 (5-fold StratifiedKFold, shuffle=True)

| Metric   | Mean ± Std       |
|----------|------------------|
| Accuracy | 0.8058 ± 0.0115  |
| F1       | 0.6018 ± 0.0282  |
| ROC-AUC  | 0.8451 ± 0.0134  |

## CV vs single-split

| Metric    | Single-split | CV mean | Diff   | Inside ±1 std? |
|-----------|--------------|---------|--------|----------------|
| Accuracy  | 0.8055       | 0.8058  | −0.0003 | ✅             |
| F1        | 0.604        | 0.6018  | +0.0022 | ✅             |
| ROC-AUC   | 0.842        | 0.8451  | −0.0031 | ✅             |

→ All three single-split numbers land inside ±1 std of the CV mean. **Single split was representative, not lucky.** This is the diagnostic the CV step exists to provide.

## What surprised me (the spaced-review hooks)

1. **Accuracy hit a ceiling at ~80%, not the 85%+ I expected.** With a linear model on imbalanced data, moving the decision threshold trades precision for recall — it walks along the ROC curve, can't escape it. The only ways to push accuracy meaningfully higher are: (a) class imbalance handling (`class_weight='balanced'`, SMOTE), (b) hyperparameter tuning, or (c) non-linear models (trees / XGBoost). Threshold tuning alone won't do it. **Lock this in: imbalanced + linear = accuracy plateau around the majority-class baseline + a few points.**

2. **Recall on the positive class is 56% — the model misses ~44% of actual churners.** For a churn-*prevention* use case, this is the dominant business problem. Accuracy tells me almost nothing here; recall (or F2 if false alarms are cheap) is what matters. Iterations should optimize for recall first.

3. **`LogisticRegression()` silently uses L2 regularization with C=1.0.** I almost shipped without realizing regularization was active. The `StandardScaler` step I added "for hygiene" turned out to be load-bearing: with L2 active, unequal feature scales would have unfairly penalized small-scale features. **Right answer for the right reason — but the right reason was hidden.** Always make defaults explicit (`max_iter=1000, penalty='l2', C=1.0`) so future-me doesn't re-discover this from scratch.

## Open questions / next iteration (Wks 4-6)

- Will class-weight balancing (`class_weight='balanced'`) lift recall meaningfully without crashing precision? Try first, before SMOTE.
- Hyperparameter sweep on `C` (0.01 → 100) — does optimal C deviate from the default?
- §4 collapse — does it actually help, or do the redundant dummies get absorbed by L2 anyway?
- Tree models (DT, RF, XGBoost) — Sunday's experiment. Pre-fit hypothesis: trees should beat LR because Telco has known non-linear interactions (tenure × Contract type, MonthlyCharges × InternetService).

## Files

- `model/01-eda.ipynb` — full EDA (univariate, bivariate by Churn, hypotheses)
- `model/02-baseline-logistic-regression.ipynb` — single-split baseline
- `model/03-cross-validated-baseline.ipynb` — 5-fold CV + single-split comparison
- `model/04-logistic-regression-from-scratch.ipynb` — TODO Sat (Phase 1 deliverable)
- `model/05-tree-models.ipynb` — TODO Sun (BLOCKED on depth recheck v2 passing)

---

*Created: May 1, 2026 (Friday Wk 3, 4 days after Mon's deliverable date — slipped due to Wk 2 EDA carry-over and Wed's plan-revision day).*

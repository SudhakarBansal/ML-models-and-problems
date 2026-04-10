# Data Quality & Model Evaluation Intuitions
## (Lessons from House Price Prediction)

---

## 1. Always explore your data BEFORE modeling

Don't rush to train. Check for:
- **Data errors**: impossible values (price = 0, negative sqft)
- **Outliers**: extreme but possibly real values ($26.5M mansion)
- **Missing values**: NaN or empty fields
- **Distribution**: is the target skewed? Are features on wildly different scales?

**Lesson learned**: 49 houses had price = $0 and one was $26.5M. These destroyed training RMSE (519k) before we caught them.

---

## 2. Data Errors vs Outliers — different treatment

| | Data Errors | Outliers |
|---|-------------|----------|
| **Example** | Price = $0 | Price = $26.5M |
| **Is it real?** | No, impossible | Maybe — could be a mansion |
| **Remove from** | Entire dataset (before split) | Training data only (after split) |
| **Why?** | Can never be valid | Model should learn from clean data, but test represents real world |

---

## 3. IQR Method for Outlier Detection

```
Q1 = 25th percentile
Q3 = 75th percentile
IQR = Q3 - Q1

Lower bound = Q1 - multiplier * IQR
Upper bound = Q3 + multiplier * IQR
```

- Standard multiplier: **1.5** (aggressive — removes more)
- Less aggressive: **2.0** (keeps more data)

**Why IQR over fixed buffer around mean?**
The mean is pulled by extreme values ($26.5M shifts it). IQR uses percentiles which are **robust to outliers** — the method adapts to your data's actual spread.

**If lower bound is negative** (e.g., -168k for house prices), the effective lower bound is 0 since prices can't be negative.

### The Outlier Removal Tradeoff

| Approach | Train RMSE | Test RMSE |
|----------|-----------|----------|
| IQR × 1.5 (aggressive) | 108k (good) | 276k (bad) |
| IQR × 2.0 (less aggressive) | 117k (ok) | 252k (better) |

More aggressive removal → cleaner training → but test still has outliers the model never saw.

---

## 4. Training RMSE vs Test RMSE

**Always compute both.** The relationship tells you what's wrong:

| Pattern | Meaning | Fix |
|---------|---------|-----|
| Train low, Test high | **Overfitting** — memorized training data | Regularization (Ridge/Lasso), more data, fewer features |
| Train high, Test high | **Underfitting** — model too simple | More features, polynomial features, complex model |
| Train > Test | **Bug in pipeline** — something is wrong | Check data alignment, stale variables, leakage |

---

## 5. Comparing Models Fairly

SGDRegressor is **stochastic** — different runs give different results. To compare "with feature X" vs "without feature X":

- Use `random_state=42` in SGDRegressor — fixes the randomness
- Or use `LinearRegression` — no randomness at all (closed-form solution)

Without fixing randomness, you can't tell if RMSE changed because of your feature or because of random variation.

---

## 6. Regularization

### What it does
Adds a penalty to large weights, preventing the model from relying too heavily on any single feature.

### Types

| Name | sklearn class | SGDRegressor penalty | What it does |
|------|--------------|---------------------|--------------|
| Ridge | `Ridge()` | `penalty='l2'` | Shrinks all weights evenly |
| Lasso | `Lasso()` | `penalty='l1'` | Shrinks some weights to exactly zero (feature selection) |
| ElasticNet | `ElasticNet()` | `penalty='elasticnet'` | Mix of both |

### The alpha knob
`alpha` controls regularization strength:
- Too low → model overfits (ignores the penalty)
- Too high → model underfits (penalty dominates, ignores the data)
- Just right → best test RMSE

**How to find it**: Try multiple values and compare test RMSE:
```python
for alpha in [0.1, 1, 10, 100, 1000, 10000]:
    model = Ridge(alpha=alpha)
```

### When is regularization essential?
When you have **many features relative to rows**. With 136 polynomial features and 3513 rows, the model overfits without regularization. Ridge with alpha=1000 was the sweet spot.

---

## 7. SGDRegressor vs Ridge/LinearRegression

| | SGDRegressor | LinearRegression / Ridge |
|---|---|---|
| **Method** | Iterative (stochastic gradient descent) | Closed-form solution (one-shot) |
| **When to use** | Very large datasets (millions of rows) | Small/medium datasets |
| **Convergence** | Can fail with many features or bad learning rate | Always stable |
| **Randomness** | Yes (need `random_state` for reproducibility) | No |

**Lesson learned**: SGDRegressor exploded with polynomial features (predictions in billions). Ridge handled the same data perfectly because it uses a stable direct solver.

**Rule of thumb**: Use Ridge/LinearRegression unless your data is too large to fit in memory.

---

## 8. The Limits of Linear Regression

After exhaustive experimentation, linear regression hit a ceiling of ~245k RMSE on this dataset:

- Feature engineering (target encoding) helped significantly: 268k → 216k
- Data cleaning helped: caught $0 prices and outliers
- Polynomial features + regularization gave marginal gains: 252k → 245k
- Domain features (age, renovation) added no new signal for a linear model

**Why**: House prices don't follow a straight-line relationship with features. The scatter plot of sqft_living vs price shows a **widening spread** — linear regression can capture the average trend but not the non-linear patterns.

**Next step**: Non-linear models (Decision Trees, Random Forest, XGBoost) that can capture complex relationships without polynomial tricks.

---

## 9. Notebook Hygiene

- **Never experiment in your final notebook.** Create a separate `experiments.ipynb` for quick tests.
- Once something works, move the clean version into your main notebook.
- Delete debug cells (shape checks, print statements) before committing.
- Label your outputs clearly: `"Train RMSE"` not just `"RMSE"`.
- Keep cell outputs meaningful — if a cell prints 4600 rows, you don't need that output saved.

---

## 10. Progress Tracker

| Version | Test RMSE | Train RMSE | What changed |
|---------|-----------|------------|-------------|
| V1: Baseline | 268k | ? | SGDRegressor on numeric features only |
| V2: + Target encoding + data cleaning | 252k | 117k | Location signal + IQR outlier removal |
| V3: + PolynomialFeatures + Ridge | 250k | 116k | 120 blind polynomial features, α=1000 |
| **V4: + Domain features + poly + Ridge** | **245k** | **115k** | age_of_house, is_renovated, years_since_renovation |

**Best model**: V4 with Ridge(alpha=1000) — Test RMSE 245k (44% of avg price)

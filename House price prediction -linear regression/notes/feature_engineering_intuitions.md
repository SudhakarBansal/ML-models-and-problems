# Feature Engineering Intuitions
## (Lessons from House Price Prediction)

---

## 1. What to drop and why

Before dropping a column, always ask: **does this column carry signal for predicting the target?**

| Column | Decision | Reason |
|--------|----------|--------|
| `date` | Drop | All records from same month/year — no variation, no signal |
| `street` | Drop | ~4.5k unique values in 4.6k records — model can't learn any pattern |
| `country` | Drop | All same (USA) — zero variation |
| `statezip` | Encode | 77 unique zip codes — location signal, but needs encoding |
| `city` | Encode | 44 unique cities — strong location signal, needs encoding |

**Rule of thumb**: If a column has nearly as many unique values as rows, it's probably an identifier, not a feature.

---

## 2. One Hot Encoding

Convert a categorical column into multiple binary (0/1) columns — one per unique category.

**Example** — `city` with 3 values:

| sqft | city | → | Seattle | Bellevue | Kent |
|------|------|---|---------|----------|------|
| 1500 | Seattle | → | 1 | 0 | 0 |
| 2000 | Bellevue | → | 0 | 1 | 0 |

**When to use**: When the number of unique categories is small.

**Problem**: If a column has 44 or 77 unique values, you add 44 or 77 new columns — this explodes your feature space. This is related to the **curse of dimensionality**.

---

## 3. Target Encoding

Replace each category with the **average target value** for that category.

**Example**: Replace each city with the average house price in that city.

| city | → | city_encoded |
|------|---|--------------|
| Seattle | → | 650,000 |
| Kent | → | 380,000 |

**When to use**: When you have many unique categories (like 44 cities or 77 zip codes) where One Hot Encoding would be too expensive.

### The Leakage Trap
If you compute averages from the **entire dataset** and then train on it — your model is "seeing the answers" during training. This is called **data leakage**.

**Safe way**:
1. Split data into train/test first
2. Compute averages **only from training data**
3. Apply those same averages to the test data

### Handling Unseen Categories
What if a city appears in test but not in train? Use the **global average price** from the training set as a fallback via `.fillna(global_avg)`.

---

## 4. Data Leakage

**Definition**: When information from outside the training data influences the model, giving it an unfair advantage that won't exist in production.

**Analogy**: Looking at the answer sheet before an exam — you'll score well in training but fail in the real world.

**Most common causes**:
- Computing statistics (mean, std) on the full dataset before splitting
- Target encoding without proper train/test separation
- Using future information to predict the past
- Accidentally including the target (`price`) as a feature — model gets near-zero error but learns nothing

---

## 5. Why not treat zip codes as raw numbers?

Zip code `98002` is not "1 more" than `98001` in any meaningful way. Treating it as a raw number implies a **linear relationship** between zip code digits and price — which is false.

Categories that look like numbers (zip codes, IDs) still need encoding, not raw numeric treatment.

---

## 6. Multicollinearity

When two features encode the **same underlying information** (e.g., `city` and `statezip` both encode location), the model can't decide how to split credit between them.

**Symptoms**: One feature gets a huge weight, the other gets near-zero or negative weight. Weights may flip between runs.

**How to detect**: Look at model weights — if a feature has near-zero weight while a similar feature has a large weight, they may be redundant.

**What to do**: Test with and without the feature (using `random_state` for fair comparison). If removing it doesn't hurt RMSE, it was redundant.

**In our case**: `city_encoded` had weight -59 vs `statezip_encoded` at 162,846. Removing city changed RMSE by only ~110 on a 216k scale — essentially redundant. But we kept both since the cost is minimal.

---

## 7. Blind vs Domain-Driven Feature Engineering

### Blind approach: PolynomialFeatures
`PolynomialFeatures(degree=2)` on 14 features → **120 features** (all possible combinations).

**Problems**:
- Most combinations are meaningless (e.g., `waterfront × yr_renovated`)
- With 120 features and ~3500 rows, the model overfits badly
- Even regularization couldn't fully fix it

### Domain-driven approach (the right way)
Create features based on **real-world understanding** of what drives house prices:

- `age_of_house` = data_year - yr_built
- `is_renovated` = binary 0/1 flag
- `years_since_renovation` = years since last update (use house age if never renovated)

**Important caveat**: Linear transformations of existing features (e.g., flipping `yr_built` to `age_of_house`) do NOT help a linear model — it can learn the same relationship by flipping the weight sign. Domain features only help if they capture **genuinely new patterns** (ratios, interactions, non-linear transforms).

**Lesson**: A few smart features beat hundreds of blind ones. ML engineers think about the **problem**, not just the data.

---

## 8. Using .corr() to guide feature decisions

`train_df.corr()["price"].sort_values()` shows linear correlation of each feature with the target.

**Useful for**:
- Identifying strong predictors (statezip_encoded: 0.69, sqft_living: 0.64)
- Spotting weak features (yr_renovated: -0.06, condition: 0.04)
- Detecting redundancy (age_of_house has same |correlation| as yr_built — just flipped)

**Limitation**: Only captures LINEAR relationships. A feature with low correlation might still be valuable in a non-linear model.

---

## 9. The Correct Pipeline Order

```
Raw Data
   ↓
Remove Data Errors        ← e.g., price = 0 (from ENTIRE dataset)
   ↓
Domain Feature Eng.       ← Pure transforms (no target info) can go here
   ↓
Train / Test Split        ← Before any statistics are computed
   ↓
Remove Outliers           ← From TRAINING data only (IQR method)
   ↓
Compute encoding maps     ← From TRAINING data only
   ↓
Apply encoding            ← To both train and test
   ↓
Feature / Target Split    ← Separate X and y
   ↓
Polynomial Features       ← If using (before scaling)
   ↓
Feature Scaling           ← fit_transform on train, transform on test
   ↓
Model Training
   ↓
Evaluation on Test Set
```

**Why scaling comes AFTER feature engineering**: Scaling uses mean/std of each feature. If you scale first, then add new features, those new features won't be scaled.

**Pure transforms** (like `2014 - yr_built`) can go before the split because they don't use target information. **Target-dependent transforms** (like target encoding) must go after the split.

---

## 10. Always predict before you measure

Before running your model, write down your expected RMSE. When the result differs from your guess, that gap is where your intuition grows.

**Prediction for this model** (with city + statezip encoding): ~150k RMSE
**Actual result**: ~245k RMSE (best) — linear regression has fundamental limits on non-linear data

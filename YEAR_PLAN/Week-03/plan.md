# Week 3: April 27 (Mon) → May 3 (Sun)
## Phase 1 | Project 2 baselines + LR-from-scratch + tree models begin

---

## Status entering Week 3

**Done in Week 2:**
- ✅ Course 2 W4 videos (incl. RF, XGBoost) — depth check passed for 4/5; Q5 (gradient boosting) flagged for re-drill
- ✅ Telco EDA notebook (`01-eda.ipynb`) — schema, data-quality fixes (TotalCharges, customerID, SeniorCitizen), univariate, bivariate by Churn, hypotheses written. Industry-standard quality.
- ✅ DSA: 14 problems (Reverse String done Sun)
- ✅ `notes/00-decision-trees-and-ensembles.md` reference written

**Carry-overs / pending from Week 2:**
- ⏳ **Project 2 — sklearn baseline (Block B)**: `02-baseline-logistic-regression.ipynb` + `03-cross-validated-baseline.ipynb` — NOT STARTED
- ⏳ **Project 2 notes**: `notes/01-eda-and-baseline.md` — NOT STARTED (waiting on baseline numbers)
- ⏳ **DSA pattern scan** (Week 2 item 10) — NOT DONE
- ⏳ **3B1B Calculus Ep 7-8** — slipped from Wed Apr 22
- ⏳ **3B1B Linear Algebra Ep 9** — slipped
- ⏳ **Spaced review system kickoff** — deferred from Week 2 Sunday
- ⏳ **Blog setup (Hashnode + Post 1 skeleton)** — deferred from Week 2 Sunday
- ⏳ **Q5 gradient-boosting re-drill** — flagged Sat for spaced review across next 3 weeks
- ⏳ **5-question depth recheck on trees/ensembles** — must pass before fitting trees on Telco

## Week 3 Theme

**Ship the baseline, then go from scratch.** Block B baseline clears Mon. Saturday is Logistic Regression from scratch — the Phase 1 "I implemented it myself" deliverable. Sunday starts tree models on Telco. Daily drills (DSA + ML) start this week per the plan.

**Friday is the lightest day** — office work has burned Friday two weeks running. Plan accordingly.

---

## Daily drills (NEW this week)

Per `YEAR_PLAN/DSA-patterns.md` and `YEAR_PLAN/ML-drills.md`. Both kick in Monday.

- **DSA daily drill** — 15 min, every day, retrieval-style pattern recall. Curriculum in `DSA-patterns.md`.
- **ML daily drill** — 15 min, **Mon/Wed/Fri/Sun only** (4 days/week), 5-format rotation. Curriculum in `ML-drills.md`.

Both drills are non-negotiable. They are the spaced-repetition backbone for the next 11 months. If any day's main block runs over, **drop the main block, never the drill.**

---

## Monday — ML Theory + Block B carry-over (2.5-3 hrs)
**Topic: Clear Block B from Week 2 — sklearn baseline on Telco**

| Order | What | Time |
|-------|------|------|
| 1 | ML drill (first day — start with Format 1 from `ML-drills.md`) | 15 min |
| 2 | DSA drill (first day — start with Pattern 1 from `DSA-patterns.md`) | 15 min |
| 3 | New notebook `model/02-baseline-logistic-regression.ipynb`. Self-contained: re-load CSV, re-apply §2 EDA fixes (TotalCharges → float, drop customerID, SeniorCitizen → Yes/No), apply the §4 collapse (No internet/phone service → No), `pd.get_dummies` on remaining categoricals, build `X` and `y` (Yes→1, No→0). | 30 min |
| 4 | `train_test_split` with **`stratify=y`** (per §4a class-balance reasoning). Fit `LogisticRegression(max_iter=1000)`. Print accuracy, precision, recall, F1, ROC-AUC, confusion matrix, classification report. | 25 min |
| 5 | New notebook `model/03-cross-validated-baseline.ipynb`. Build a `Pipeline` (`StandardScaler` + `LogisticRegression`). Use `StratifiedKFold(n_splits=5)` + `cross_val_score` for F1 and ROC-AUC. Compare CV mean/std vs single-split numbers from item 4. | 50 min |
| 6 | `notes/01-eda-and-baseline.md`: data shape, cleaning decisions (one bullet each), single-split metrics, CV metrics, what surprised you. 5-6 bullets, terse. | 15 min |

**Done = baseline numbers exist on disk.** The "what surprised you" line is critical — that's the signal you'll mine when you get to interview prep next year.

---

## Tuesday — DSA (1.5-2 hrs)
**Topic: Two Pointers consolidation + Stack pattern intro**

| Order | What | Time |
|-------|------|------|
| 1 | DSA drill (Pattern 2 from `DSA-patterns.md`) | 15 min |
| 2 | **Problem 16**: [Container With Most Water](https://leetcode.com/problems/container-with-most-water/) — medium, two pointers classic. Try 25 min before hint. | 25-35 min |
| 3 | **Problem 17**: [Valid Parentheses](https://leetcode.com/problems/valid-parentheses/) — easy, **first Stack problem**. Pattern intro: "I have to match an open with the most recent unmatched open" → push on open, pop on close. | 20-25 min |
| 4 | **Problem 18**: [Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix/) — easy, strings/scanning. Quick win. | 15-20 min |
| 5 | One-line pattern note for each. Group with prior week's notes by pattern. | 10 min |

**Target: 3 problems. Running total: 18 (Mon's #15 Ransom Note daily-drill + Tue's 3 = 16 easy + 2 medium).**

---

## Wednesday — ML Theory (1.5-2 hrs)
**Topic: 3B1B catch-up + Project 2 prep — depth recheck before tree work**

| Order | What | Time |
|-------|------|------|
| 1 | ML drill (Format 2 from `ML-drills.md`) | 15 min |
| 2 | DSA drill (Pattern 3) | 15 min |
| 3 | 3B1B Calculus **Ep 7** (carry-over) — limits, formal definition of derivative. | 15-20 min |
| 4 | 3B1B Calculus **Ep 8** (carry-over) — integration intro. | 15 min |
| 5 | 3B1B Linear Algebra **Ep 9** (carry-over) — change of basis. | 15 min |
| 6 | **Tree depth re-check** (cold, no peeking): close all tabs, redo the 5 questions from `notes/00-decision-trees-and-ensembles.md`. Compare. **If you pass all 5 → Saturday's tree work is green-lit.** If you fail Q5 (gradient boosting) again → re-watch StatQuest Gradient Boost Part 1 Friday before Sat. | 30 min |

**Hard rule**: do not fit trees on Telco (Sunday) without passing the 5-question recheck. Lesson #1 from Week 2: finished ≠ understood.

---

## Thursday — DSA (1.5-2 hrs)
**Topic: Sliding Window pattern intro + Stack continuation**

| Order | What | Time |
|-------|------|------|
| 1 | DSA drill (Pattern 4) | 15 min |
| 2 | Re-read Tuesday's pattern notes. Recall Container With Most Water approach without code. | 5 min |
| 3 | **Problem 19**: [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/) — medium, **first Sliding Window problem**. The pattern: maintain a window `[l, r]`, expand `r`, shrink `l` when invariant breaks. This is THE classic sliding window. Try 30 min before hint. | 30-40 min |
| 4 | **Problem 20**: [Min Stack](https://leetcode.com/problems/min-stack/) — easy, builds on Tuesday's Valid Parentheses. The trick is keeping `min` available in O(1). | 25-35 min |
| 5 | Pattern notes — "Sliding Window: variable-size windows over arrays/strings, expand-shrink pattern." | 10 min |

**Target: 2 problems. Running total: 20.**

---

## Friday — ML Theory (LIGHT, ~1 hr) — protected for office overflow
**Topic: 3B1B finishers + Sat prep**

Friday has been crushed by office work two weeks running. Per Week 2 lesson #8 — **Friday is now structurally light**. If office burns Friday, only daily drills must hold; everything else can move to Saturday morning.

| Order | What | Time |
|-------|------|------|
| 1 | ML drill (Format 3) | 15 min |
| 2 | DSA drill (Pattern 5) | 15 min |
| 3 | 3B1B LA **Ep 10**: Cross products in light of linear transformations | 15 min |
| 4 | If Wed depth re-check failed Q5 → re-watch [StatQuest Gradient Boost Part 1](https://www.youtube.com/watch?v=3CC4N4z3GJc) (16 min). Otherwise: re-read `00-decision-trees-and-ensembles.md` (10 min refresh). | 15 min |
| 5 | Sat prep mental rehearsal: "Tomorrow I implement logistic regression in numpy. The pieces I need: sigmoid, cost (log loss), gradient, GD loop. The sklearn predictions are my ground truth — they should match within rounding." | 5 min |

**Hard cap: 1 hr planned**. If you finish in 30 min, stop. Don't reach for tomorrow's work today.

---

## Saturday — ML Deep Work (5 hrs) — LR from scratch
**Topic: Logistic Regression from scratch — Phase 1 deliverable**

Per the 1-year plan: this is your second "I implemented it myself" piece, after Project 1's Normal Equation deep-dive. Interview gold: "I didn't just call sklearn — I implemented sigmoid, cost, gradient descent in numpy and verified my predictions match sklearn within rounding."

### Block 1: Setup & implementation (2.5 hrs)

| Order | What | Time |
|-------|------|------|
| 1 | New notebook `model/04-logistic-regression-from-scratch.ipynb`. Re-load Telco data, re-apply §2 EDA fixes + §4 collapse + dummies. Get `X_train, X_test, y_train, y_test` with `stratify=y`. **Standardize X** (MUST for gradient descent — without scaling, learning rate becomes a nightmare). | 30 min |
| 2 | Implement **`sigmoid(z)`** — one-liner, `1 / (1 + np.exp(-z))`. Plot it for `z` in `[-10, 10]` to sanity-check. | 10 min |
| 3 | Implement **`compute_cost(X, y, w, b)`** — log loss / binary cross-entropy. Vectorize. Watch out for `log(0)` — use a small epsilon. | 25 min |
| 4 | Implement **`compute_gradient(X, y, w, b)`** — derive on paper first (chain rule on log loss → ends up clean: `dw = (1/m) * X.T @ (sigmoid(Xw+b) - y)`). Verify shapes. | 35 min |
| 5 | Implement **`gradient_descent(X, y, w_init, b_init, alpha, num_iters)`** — loop, update, log cost every 100 iters. Return final `w, b` and cost history. | 30 min |

### Break (15 min — walk away)

### Block 2: Train, verify, compare (1.5 hrs)

| Order | What | Time |
|-------|------|------|
| 6 | Train on `X_train, y_train`. Try `alpha=0.01, num_iters=1000` first. **Plot cost curve.** It must be monotonically decreasing. If not — bug. Don't proceed. | 25 min |
| 7 | Predict on `X_test`. Threshold at 0.5. Compute accuracy, F1, ROC-AUC. Compare to your sklearn baseline from Monday. | 20 min |
| 8 | Side-by-side: fit `sklearn.linear_model.LogisticRegression(C=1e10, max_iter=1000)` on the **same scaled data** (the `C=1e10` removes regularization so it's an apples-to-apples comparison). Compare predicted probabilities row-by-row — should be within ~1e-3. If they diverge wildly → debug your gradient. | 30 min |
| 9 | Edge cases: try `alpha=0.001` (slow convergence) and `alpha=1.0` (probably diverges). Plot cost curves. Build intuition for what learning rate does. | 15 min |

### Block 3: Reflection (45 min)

| Order | What | Time |
|-------|------|------|
| 10 | Update `notes/01-eda-and-baseline.md` (or split into `02-from-scratch.md`): summary table — sklearn baseline (single-split + CV) vs your-from-scratch implementation. F1 and ROC-AUC numbers. | 15 min |
| 11 | Reflection note: what was hardest about the gradient derivation? What surprised you about the cost curve? When did `alpha=1.0` blow up — and **why** mathematically? Three short paragraphs. | 30 min |

**End of Saturday: you've implemented LR from scratch and matched sklearn predictions.** That's an interview talking point for the rest of your career.

### Fallback ladder

- **Block 1 took >3 hrs**: Skip Block 3 reflection (do it Sun). Block 2 is non-negotiable — without sklearn comparison, you don't know if your code is correct.
- **Cost curve isn't decreasing**: Stop. Don't push forward. Common bugs: (a) gradient sign flipped, (b) `X` not scaled, (c) `y` shape mismatch (column vs row vector). Debug systematically.
- **Out of energy after Block 1+2 (3.5 hrs)**: Stop. Reflection moves to Sunday. The implementation + comparison is the deliverable; the writeup is icing.

---

## Sunday — Mixed Day (~4 hrs) — Trees + spaced review + blog setup
**Topic: Tree models on Telco (kickoff) + first spaced review + blog setup**

### Block A: Telco — tree models kickoff (1.5 hrs)

| Order | What | Time |
|-------|------|------|
| 1 | New notebook `model/05-tree-models.ipynb`. Re-use the same X/y prep from Saturday (you can copy-paste or factor into a small helper at the top of the notebook). | 15 min |
| 2 | Fit `DecisionTreeClassifier(random_state=42)` with default params. Compute F1, ROC-AUC, confusion matrix. **Before fitting, write one line in markdown**: "This model works by [splitting on feature thresholds that maximize information gain]. It should beat LR because [it captures non-linear interactions like tenure × Contract]. If it doesn't, my explanation would be [overfitting on this tabular dataset of moderate size]." (Per Week 2 Lesson #6 — force using `00-decision-trees-and-ensembles.md` as living knowledge.) | 25 min |
| 3 | Fit `RandomForestClassifier(random_state=42, n_estimators=100)`. Same metrics. Same one-line "this should/shouldn't beat the previous because..." preamble. | 25 min |
| 4 | Brief comparison table at the bottom: LR baseline (Mon) / LR-from-scratch (Sat) / DT / RF — F1, ROC-AUC. Don't tune yet. Just observe. | 15 min |

### Break (15 min — real break, walk)

### Block B: First spaced review (30 min)

Per the 1-year plan's spaced repetition system. **First Sunday review session.**

| Order | What | Time |
|-------|------|------|
| 5 | Close all tabs. Re-read `Project 1 — House Price Prediction` notes (your old notes from before this plan started). Then close them. Write 3 bullets from memory: "What were the most important things I learned in this project?" Compare what you wrote vs what's in the notes. Note any gap. | 30 min |

### Block C: Blog setup (1 hr)

Per 1-year plan: Post 1 = "What 4 iterations of linear regression taught me about ML" (from house price notes). Setup + skeleton today; full draft over the next 1-2 weekends.

| Order | What | Time |
|-------|------|------|
| 6 | Sign up for [Hashnode](https://hashnode.com/). Pick blog name (something simple — your name or a 1-2 word handle). | 15 min |
| 7 | Create draft: outline for Post 1. Sections: intro (the problem), iteration 1 (baseline SGDRegressor), iteration 2 (target encoding + outliers), iteration 3 (polynomial + Ridge), iteration 4 (domain features), reflection (what 4 iterations taught me). One paragraph per section — bullets are fine. **Don't write the full post. Just structure + intro.** | 45 min |

### Block D: DSA + drills (45 min)

| Order | What | Time |
|-------|------|------|
| 8 | DSA drill (Pattern 6) | 15 min |
| 9 | ML drill (Format 4) | 15 min |
| 10 | Pattern recall scan from Week 2 (carry-over): name the pattern for each of the 19 problems without looking at code. | 15 min |

**Total Sunday: ~4 hrs.** No new big topic — this is integration day.

---

## Week 3 Targets

| Category | Target | How to verify | Status |
|----------|--------|---------------|--------|
| Project 2 — sklearn baseline | Single-split + CV done with metrics | `02-baseline-logistic-regression.ipynb` + `03-cross-validated-baseline.ipynb` | ⏳ Mon |
| Project 2 — LR from scratch | Cost curve decreasing, predictions match sklearn within 1e-3 | `04-logistic-regression-from-scratch.ipynb` | ⏳ Sat |
| Project 2 — tree models kickoff | DT + RF fit, F1/ROC-AUC compared to LR | `05-tree-models.ipynb` | ⏳ Sun |
| Project 2 — notes | Comparison table + reflection | `notes/01-eda-and-baseline.md` (or split) | ⏳ Mon + Sat |
| Tree depth re-check | 5/5 cold | Self-check Wed | ⏳ Wed |
| 3B1B Calculus | Ep 7-8 done | Notes | ⏳ Wed |
| 3B1B Linear Algebra | Ep 9-10 done | Notes | ⏳ Wed/Fri |
| DSA | 20 problems total (6 new this week incl. Mon daily drill) | Pattern notes | ⏳ Mon/Tue/Thu/Sun |
| Daily drills | 7/7 DSA, 4/4 ML | Logged daily | ⏳ Daily |
| Spaced review | First session done | Project 1 retrospective bullets | ⏳ Sun |
| Blog setup | Hashnode + Post 1 skeleton | Hashnode draft URL | ⏳ Sun |

---

## Phase 1 progress check (after Week 3)

| Phase 1 deliverable | Total estimate | Done after Wk 3 (target) | Remaining |
|---|---|---|---|
| Course 2 (W2-W4 watched + W4 depth nailed) | 8-12 hrs | DONE | — |
| 3B1B Calculus | 6 hrs | ~5 hrs | ~1 hr |
| 3B1B Linear Algebra | 7 hrs | ~5.5 hrs | ~1.5 hrs |
| Project 2 (EDA + baseline + scratch + tree kickoff) | 35-40 hrs | ~13 hrs | ~22-27 hrs |
| LR from scratch | 3-4 hrs | DONE | — |
| DSA (22-27 remaining) | 22-28 hrs | 20/22-27 problems done | ~2-7 problems |
| Blog post 1 (setup + skeleton) | 5-6 hrs | ~2 hrs | ~3-4 hrs |

**On track.** Weeks 4-7 of Phase 1 = Project 2 deepening (XGBoost, hyperparameter tuning, SHAP, W&B, FastAPI) + DSA continuation + blog post 1 publish + 3B1B finish.

---

## If you're struggling

- **Mon Block B feels rushed**: Drop item 5 (CV notebook) → push to Tue evening or Wed morning. The single-split notebook (item 4) is non-negotiable.
- **Tue/Thu DSA medium too hard**: Drop the medium. Two easies = success. Don't burn 90 min on one problem (Lesson from Week 1).
- **Wed depth recheck fails Q5 again**: Re-watch StatQuest Gradient Boost Part 1 + 2 on Friday. Push the gradient boosting depth-fix into next week — but **do not fit XGBoost on Telco until you can answer Q5 cold**. (Lesson #1: finished ≠ understood.)
- **Saturday LR-from-scratch cost curve won't decrease**: Stop. Common causes — gradient sign, X not scaled, y shape. Debug systematically. Do not "tune the learning rate to make it work" — that papers over a real bug.
- **Burnout signs (dreading sessions, retaining nothing)**: Take a full day off. Don't power through. (Per 1-year plan's burnout protocol.)
- **Friday is crushed by office**: Acceptable. Drills must hold, the rest moves to Saturday morning. Saturday's 5-hr LR-from-scratch block becomes 6-hr with the spillover.

---

## What to bring to next week's planning session

Tell me at the end of the week:
1. Did Mon's Block B ship cleanly? Single-split F1 and ROC-AUC numbers.
2. Did the LR-from-scratch predictions match sklearn within rounding? If not, where did they diverge?
3. Did DT and RF beat LR on Telco? By how much (F1 and ROC-AUC)?
4. Wed depth recheck — 5/5 or did Q5 still fall?
5. Hardest DSA problem this week and what tripped you up.
6. Did the daily drills hold all 7 days? Any drill format that felt useless or unclear (so I can adjust the curriculum)?
7. Blog skeleton — share the Hashnode draft URL.
8. Any surprises from tree-model kickoff that changed your hypothesis from EDA.

I'll plan Week 4 around: (a) hyperparameter tuning + class-imbalance handling, (b) XGBoost, (c) starting SHAP, (d) DSA continuation. **W&B + FastAPI shift to Week 5-6** once the modeling is done.

---

## Lessons from Week 2 — apply this week

These are direct carry-overs. Don't re-read Week 2's lessons section every Monday — internalize once, then apply.

1. **Finished ≠ understood.** Wed depth recheck is the hard gate before Sat tree work.
2. **Reflection is not optional.** If Sat runs over, drop Block 2's edge-case exploration before dropping Block 3's reflection.
3. **Don't front-load ML.** If Mon's Block B starts going 3+ hrs on one item, stop and move on.
4. **Protect math.** 3B1B Calc Ep 7-8 are scheduled Wed. They've slipped twice — do not slip a third time. Cut ML theory before cutting math.
5. **Friday is light.** Office burned Friday two weeks running. Plan for it.
6. **Pre-fit mental check** for every model on Telco (DT, RF Sun; XGBoost next week): "This model works by [mechanism]. It should beat the previous because [reason]. If it doesn't, my explanation would be [reason]." Before `.fit()` is called.
7. **5-question depth check** before marking ANY chapter/course/topic done. Including Sat's LR-from-scratch — finish Sat by writing 5 questions for yourself and answering them cold.
8. **Daily drills are non-negotiable.** They hold even on the day office crushes you. 15 min × 2.

---

*Plan created: April 26, 2026 (Sunday evening, Week 2 close)*
*Carries forward: Block B baseline, blog setup, spaced review kickoff, 3B1B catch-up, DSA pattern scan*
*Next review: End of Week 3 (Sunday May 3, 2026)*

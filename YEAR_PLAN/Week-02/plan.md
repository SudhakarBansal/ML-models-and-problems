# Week 2: April 20 (Mon) → April 26 (Sun)
## Phase 1 | Project 2 ignition + Course 2 Week 4

---

## Status entering Week 2

- **Course 2**: Weeks 1, 2, 3 DONE. Week 4 (Decision Trees, Random Forest, XGBoost) — NOT STARTED
- **3B1B Calculus**: Episodes 1-6 done (~4 episodes left in essence series)
- **3B1B Linear Algebra**: Episodes 1-6 done (10 episodes left, Ep 7-16)
- **3B1B Neural Networks**: Ch 1, 2, 3 done
- **DSA**: 7/8 problems done. **Maximum Subarray (Kadane's) — PENDING carry-over**
- **Project 2 dataset**: Telco Customer Churn — selected, CSV downloaded, EDA gotchas already noted (TotalCharges-as-string, customerID drop, SeniorCitizen 0/1 inconsistency, class balance check)
- **Logistic regression from scratch**: NOT STARTED
- **Blog**: NOT setup
- **Normal Equation deep dive**: DONE

## Week 2 Theme

**Pivot from theory-heavy to project-heavy.** This is the week Project 2 starts. Course 2 Week 4 (trees) runs alongside but takes second priority — the goal is to have an EDA + working logistic regression baseline on Telco churn by Sunday night.

---

## Progress Update — Wed Apr 22 evening

**Done:**
- Mon: Course 2 W4 first videos + 3B1B LA Ep 7-8 ✅
- Tue: Maximum Subarray (Kadane) + Valid Palindrome + Move Zeroes (10 problems total) ✅
- Wed: **Finished ALL of Course 2 Week 4** in one day (including RF, XGBoost videos originally planned for Fri)

**Not done Wed (deferred):**
- 3B1B Calculus Ep 7-8 → carry to Fri
- Reflection writeup (trees vs NN optimization) → absorb into Sat Block 1

**Depth check result (5 questions on trees/ensembles):** 2 shaky, 3 failed. Rushed Course 2 W4 ≠ understood it. You described AdaBoost when asked about gradient boosting, missed feature sampling in RF, and have a Gini blind spot. **Friday is now revision day.** Project 2 modeling cannot proceed on this foundation.

---

## Monday ✅ DONE — ML Theory (1.5-2 hrs)
**Topic: Course 2 Week 4 START + Linear Algebra**

| Order | What | Time |
|-------|------|------|
| 1 | ~~Course 2 Week 4 — first 3-4 videos (Decision Tree intuition, splitting on features).~~ DONE | 50-60 min |
| 2 | ~~Reflect: tree prediction vs regression. Mental model shift.~~ DONE | 10 min |
| 3 | ~~3B1B Linear Algebra Ep 7: Dot products and duality~~ DONE | 15 min |
| 4 | ~~3B1B Linear Algebra Ep 8: Cross products~~ DONE | 10-15 min |

---

## Tuesday ✅ DONE — DSA (1.5-2 hrs)
**Topic: Clear carry-over + Two Pointers pattern intro**

| Order | What | Time |
|-------|------|------|
| 1 | ~~**Carry-over: [Maximum Subarray](https://leetcode.com/problems/maximum-subarray/)** — Kadane's algorithm.~~ DONE | 30-40 min |
| 2 | ~~Pattern note for Kadane.~~ DONE | 5 min |
| 3 | ~~**Problem 9**: [Valid Palindrome](https://leetcode.com/problems/valid-palindrome/)~~ DONE | 20-25 min |
| 4 | ~~**Problem 10**: [Move Zeroes](https://leetcode.com/problems/move-zeroes/)~~ DONE | 20-25 min |
| 5 | ~~Pattern notes grouped.~~ DONE | 10 min |

**Target hit: 10 problems total.**

---

## Wednesday ⚠️ PARTIAL — ML Theory
**Topic: Course 2 Week 4 — splitting criteria + Calculus**

| Order | What | Status |
|-------|------|--------|
| 1 | ~~Course 2 Week 4 — all remaining videos (RF, XGBoost, ensembles).~~ **DONE — finished entire Course 2 W4 today, exceeding plan.** | ✅ DONE |
| 2 | Reflect: why trees prefer splits that reduce entropy. | ⏭️ SKIPPED (out of energy) — rolled into Sat Block 1 |
| 3 | 3B1B Calculus Ep 7 + Ep 8 (limits, integration intro) | ⏭️ SKIPPED — carry to Fri |
| 4 | Tree optimization vs NN optimization note. | ⏭️ SKIPPED — rolled into Sat Block 1 |

**Flag:** Finishing the videos ≠ understanding the material. Depth check failed 3/5. Revision ordered for Fri.

---

## Thursday — DSA (1.5-2 hrs)
**Topic: Two Pointers continues + 1 stretch problem**

| Order | What | Time |
|-------|------|------|
| 1 | Re-read Tuesday's pattern notes. Recall Kadane without looking. | 5 min |
| 2 | **Problem 11**: [Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/) — Two Pointers, classic. | 20-25 min |
| 3 | **Problem 12**: [Squares of a Sorted Array](https://leetcode.com/problems/squares-of-a-sorted-array/) — Two Pointers but the trick is non-obvious. Try 25 min before hint. | 25-35 min |
| 4 | **Problem 13 (stretch — medium)**: [Two Sum II — Input Array Is Sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/) — your first "real" Two Pointers medium. You already know Two Sum from Day 1; now solve it in O(1) space using the sorted property. | 25-35 min |
| 5 | One-line pattern notes. | 5 min |

**Target: 3 problems. Running total: 13 problems (12 easy + 1 medium).**

---

## Friday — ENSEMBLE REVISION DAY (1.5-2 hrs)
**Topic: Fix the tree/ensemble depth gap via StatQuest**

Why Friday is now revision day: your 5-question self-check revealed that (a) you described AdaBoost when asked about gradient boosting, (b) you missed feature sampling in Random Forest, (c) Gini is a blind spot. Course 2 "done" is meaningless if you can't 3-level-deep it in an interview. Fix it NOW — before Project 2 starts. [Josh Starmer's StatQuest](https://www.youtube.com/c/joshstarmer) is the clearest ensemble material online. Watch in order:

| Order | What | Time |
|-------|------|------|
| 1 | StatQuest: **Gini Impurity** — fills the Gini gap | 10 min |
| 2 | StatQuest: **Random Forests Part 1 — Building, Using, Evaluating** — pay attention to what RF randomizes *at each split*, not just per tree | 15 min |
| 3 | StatQuest: **AdaBoost, Clearly Explained** — this is what you described when asked about XGBoost. Watch to cement the contrast. | 20 min |
| 4 | StatQuest: **Gradient Boost Part 1 — Regression Main Ideas** — THE video that fixes Q5. Pay attention to what each new tree is trained to predict. | 15 min |
| 5 | StatQuest: **XGBoost Part 1 — Regression** (if time) | 20 min |
| 6 | 3B1B Calculus Ep 7 (carry-over from Wed) — limits | 15 min |

**Do NOT take written notes during the videos — watch cleanly first. Notes happen Saturday Block 1, from memory.**

---

## Saturday — Project 2 IGNITION (compressed, 5 hrs)
**Block 1 is non-negotiable. This is where Course 2 W4 actually becomes yours.**

### Block 1: Rewrite the 5 Depth-Check Answers from Memory (1 hr)

After Friday's StatQuest watch, close all tabs. Create new file: `Telco-churn-classification/notes/00-decision-trees-and-ensembles.md`. Answer the 5 questions **without peeking at any resource**, in your own words, with concrete examples:

1. Why do tree models not need feature scaling? (Think: what arithmetic operation does a tree do at a split?)
2. Bagging vs boosting — mechanism AND which reduces variance vs bias. What does RF randomize beyond bootstrap?
3. How do Random Forest trees become *different* enough to benefit the ensemble?
4. Gini vs entropy — do they produce different trees in practice? Entropy shape for binary vs 3-class.
5. In gradient boosting, what is each new tree trained to predict? How does this differ from AdaBoost?

Then open StatQuest + Course 2 notes and fact-check yourself. Correct anything wrong. **This file becomes your permanent tree/ensemble reference — you'll re-read it every Sunday spaced-review cycle.**

### Block 2: Telco Churn EDA (1.5 hrs)

Set up: `Telco-churn-classification/data/`, `model/`, `notes/`.

| Order | What | Time |
|-------|------|------|
| 1 | New notebook `01-eda.ipynb`. Load CSV. `.info()`, `.describe()`, `.head()`. | 15 min |
| 2 | Investigate the gotchas: (a) `TotalCharges` blank rows — which ones? Why? (Hint: look at their `tenure`.) Decide handling. (b) `Churn` class balance — % positive? (c) Drop `customerID`. | 30 min |
| 3 | Visualize 4-5 plots that tell a story: `tenure`, `MonthlyCharges`, `Contract`, `PaymentMethod` split by `Churn`. Don't make 30 random plots. | 30 min |
| 4 | Markdown summary in the notebook: "What did EDA reveal? Feature hypotheses?" 5-6 bullets. | 15 min |

### Break (15 min — walk away)

### Block 3: Logistic Regression from scratch (2 hrs)

| Order | What | Time |
|-------|------|------|
| 5 | New notebook `02-logistic-regression-from-scratch.ipynb`. Implement sigmoid in numpy. Test on a vector. | 15 min |
| 6 | Implement BCE cost function. Sanity check with known inputs. | 25 min |
| 7 | Implement gradient computation (derivative of BCE w.r.t. weights). Write down shapes before coding. | 30 min |
| 8 | Training loop: init weights, loop N iterations, gradient descent updates, plot cost curve. Cost MUST decrease. | 30 min |
| 9 | Test on `make_classification` synthetic data. Compare to sklearn `LogisticRegression` — predictions should agree on most points. | 20 min |

**sklearn baseline on Telco — MOVED to Sunday** (Saturday is full).

**End of Saturday: You have tree/ensemble depth notes + EDA notebook + from-scratch LR. This is real progress.**

---

## Sunday — Mixed Day (4-5 hrs)

### ML Block (2.5 hrs) — absorbs the sklearn baseline from Saturday

| Order | What | Time |
|-------|------|------|
| 1 | New notebook `03-baseline-logistic-regression.ipynb`. Load cleaned data from EDA. Encode categoricals (`pd.get_dummies` is fine). Single 80/20 split. Fit `LogisticRegression`. Print accuracy, precision, recall, F1, ROC-AUC, confusion matrix. | 50 min |
| 2 | New notebook `04-cross-validated-baseline.ipynb`. sklearn `Pipeline` (imputer → scaler → LogisticRegression) + `StratifiedKFold` + `cross_val_score`. Compare CV numbers to the single-split number. | 60 min |
| 3 | Write project notes file: `notes/01-eda-and-baseline.md`. Document: data shape, cleaning decisions, baseline AUC-ROC, what surprised you. Intuition-driven, like House Price notes. | 20 min |
| 4 | 3B1B Calc Ep 8 + 3B1B LA Ep 9 (if not done) | 30 min |

### DSA Block (45 min)

| Order | What | Time |
|-------|------|------|
| 4 | **Problem 14**: [Reverse String](https://leetcode.com/problems/reverse-string/) — Two Pointers, very quick. Should take 10 min. | 10-15 min |
| 5 | Review all 14 problems' pattern notes. Can you name the pattern for each without looking? | 15-20 min |

### Spaced Review (30 min) — FIRST one of the program

| Order | What | Time |
|-------|------|------|
| 6 | Close all notes. Write from memory: "What were the 3 most important things I learned in the House Price project?" Don't peek. | 10 min |
| 7 | Open House Price notes. Compare. What did you miss? | 10 min |
| 8 | Re-read your new `00-decision-trees-and-ensembles.md` from Saturday. Tighten any answer that reads fuzzy. | 10 min |

### Blog Setup (30-45 min) — light, just unblock for next week

| Order | What | Time |
|-------|------|------|
| 9 | Sign up on [Hashnode](https://hashnode.com/) (recommended — better SEO, dev audience). Pick a username. Set up profile photo + 1-line bio. | 20 min |
| 10 | Create a draft post titled "What 4 iterations of linear regression taught me about ML". Paste in raw content from your House Price notes. **Do NOT polish yet — just get the skeleton.** Editing happens in Week 3. | 15-20 min |

---

## Week 2 Targets (revised)

| Category | Target | How to verify |
|----------|--------|---------------|
| Course 2 | ✅ Week 4 videos done | — |
| Trees/ensembles depth | **Rewritten 5-Q&A file passes self-check** | `notes/00-decision-trees-and-ensembles.md` exists with correct answers |
| 3B1B Calculus | Ep 7-8 done (1-8 total) | Notes |
| 3B1B Linear Algebra | Ep 7-9 done (Ep 7-8 ✅, Ep 9 on Sun) | Notes |
| Project 2 — EDA | Notebook done with findings | `01-eda.ipynb` |
| Project 2 — LR from scratch | Cost curve decreasing, matches sklearn | `02-*.ipynb` |
| Project 2 — sklearn baseline | Single-split + CV metrics | `03` + `04` notebooks |
| Project 2 — notes | First project note written | `notes/01-eda-and-baseline.md` |
| DSA | 14 problems total (Thu target: Problems 11-13) | Pattern notes grouped |
| Blog | Hashnode account + draft skeleton | — |
| Spaced Review | First session done | Recall + comparison |

---

## Phase 1 progress check

After Week 2, here's where you should be vs the original plan:

| Phase 1 deliverable | Total estimate | Done so far | Remaining |
|---|---|---|---|
| Course 2 (50% remaining at start) | 8-12 hrs | **DONE** (W2-W4 all watched; depth revision on Fri) | 0 hrs (videos) + 2 hrs (revision Fri) |
| 3B1B Calculus | 6 hrs | ~4 hrs | ~2 hrs |
| 3B1B Linear Algebra | 7 hrs | ~4.5 hrs | ~2.5 hrs |
| Project 2 (EDA → models → SHAP → W&B → FastAPI) | 35-40 hrs | ~5 hrs | ~30-35 hrs |
| LR from scratch | 3-4 hrs | ~2-3 hrs | 0-1 hr |
| DSA (22-27 remaining) | 22-28 hrs | ~6 hrs (8-9 problems) | ~16-22 hrs |
| Blog post 1 + setup | 5-6 hrs | ~1 hr | ~4-5 hrs |

**You're on track.** After Week 2, the remaining ~5 weeks of Phase 1 are 100% Project 2 deep work + DSA + 3B1B finish + blog publish.

---

## If you're struggling

- **Saturday Project 2 block feels overwhelming**: Skip Block 2 (LR from scratch). Move it to next Saturday. Don't skip EDA or sklearn baseline — those unblock everything else.
- **Course 2 Week 4 is dense**: Trees + ensembles is a LOT in one week. If you only get 60% done, that's fine. Finish in Week 3. Don't sacrifice Project 2 for Course 2.
- **DSA medium (Two Sum II) feels too hard**: Skip it. 5 easies is fine. Don't burn 90 min on one problem.
- **Telco EDA reveals something weird you don't understand**: Note it down, ask in the next session. Don't stall the whole project waiting for an answer.

---

## What to bring to next week's planning session

Tell me:
1. What did you complete vs what you skipped
2. Project 2 baseline AUC-ROC number
3. Any surprises from EDA (TotalCharges story, class imbalance %, anything else)
4. Whether LR-from-scratch matched sklearn predictions (or where it diverged)
5. Hardest DSA problem and what tripped you up
6. **Redo the 5 tree/ensemble questions cold (no peeking). If you pass all 5, Project 2 modeling is green-lit for Week 3.**

I'll adjust Week 3 based on that — Week 3 is where Project 2 goes deep (decision trees → RF → XGBoost on Telco, class imbalance handling, hyperparameter tuning).

---

## Lessons from Week 2 — things to watch in future

These are the patterns that almost derailed you this week. Internalize them now; they'll repeat throughout the year.

### 1. Finished ≠ understood
You finished Course 2 W4 three days ahead of schedule and failed the depth check immediately after. Speed through content is worthless if you can't 3-level-deep it in an interview. **New rule for every future course/chapter/video series: before marking it "done," run a written self-check with 5 cold questions.** If you can't answer them without peeking, it's not done — regardless of whether the videos are watched.

### 2. Don't treat reflection items as optional
Every time you "ran out of energy" this week, the thing you dropped was the reflection/writing task — not the video. That's backwards. **The videos are input; the notes are the actual learning.** If you have 45 min left and a choice between (a) one more video or (b) writing the reflection for the video you just watched — choose (b) every single time.

### 3. Energy budgeting — don't front-load ML
You finished Course 2 today but had zero energy left for the rest of Wed's list. That means you over-invested in one task. **When a weekday ML session starts going 2.5 hrs on one topic, stop and move to the next item.** The plan has 3 items per ML day for a reason — breadth keeps retention higher than cramming one topic.

### 4. AdaBoost vs gradient boosting (specific — carry this forward)
This confusion will come back. Every time you encounter an "ensemble" or "boosting" concept in later projects or interviews, pause and ask: *is this reweighting examples (AdaBoost) or fitting residuals (gradient boosting)?* They look similar from far away. They're fundamentally different. Keep your `00-decision-trees-and-ensembles.md` open when you touch Project 2's tree models.

### 5. Math arc is fragile — don't let it slip
3B1B Calculus Ep 7-8 were scheduled for Wed. You skipped them. That's a one-day slip but compounds: if you skip every time ML feels heavier, by Phase 3 (DL) you'll hit calculus/linalg walls you can't push through. **Protect the math minutes. If ML theory goes over budget, cut the ML theory — not the math.**

### 6. Watch for the "I already know this" trap with ensembles in Project 2
When you implement RF and XGBoost on Telco next week, the muscle memory of "sklearn.fit(X, y)" will feel easy. That's deceptive. **For each model, before fitting, write one sentence in your notebook: "This model works by [mechanism]. It should beat LR because [reason]. If it doesn't, my explanation would be [reason]."** This forces you to use the Saturday ensemble notes as living knowledge, not dead pages.

### 7. The self-check pattern is now a permanent ritual
From now on, at the end of every course week, every project phase, every book chapter — before moving to the next thing, do a 5-question cold self-check. If you pass, move on. If you fail, revise before advancing. This is your single biggest interview-depth insurance policy for the next 11 months.

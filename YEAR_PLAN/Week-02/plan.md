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

## Friday ❌ SKIPPED — heavy office work
**Topic was: Ensemble revision via StatQuest (Gini, RF, AdaBoost, Gradient Boost, XGBoost Part 1) + 3B1B Calc Ep 7**

**Carry-over to Saturday morning** (mandatory — cannot start Project 2 modeling without this).

---

## Saturday — Salvage Day (compressed, 5 hrs)
**Friday was lost to office work. Saturday absorbs the depth revision + EDA. LR-from-scratch and baselines push to Sunday. This is a controlled re-shuffle, not a panic.**

### Block 1: Friday's Revision (carry-over) — ~90 min

Watch in order. Verified links below.

| Order | What | Link | Runtime |
|-------|------|------|---------|
| 1 | StatQuest: **Decision and Classification Trees** (covers Gini Impurity inside — there's no standalone Gini video) | [youtu.be/_L39rN6gz7Y](https://www.youtube.com/watch?v=_L39rN6gz7Y) | 18 min |
| 2 | StatQuest: **Random Forests Part 1 — Building, Using, Evaluating** | [youtu.be/J4Wdy0Wc_xQ](https://www.youtube.com/watch?v=J4Wdy0Wc_xQ) | 10 min |
| 3 | StatQuest: **AdaBoost, Clearly Explained** | [youtu.be/LsK-xG1cLYA](https://www.youtube.com/watch?v=LsK-xG1cLYA) | 21 min |
| 4 | StatQuest: **Gradient Boost Part 1 — Regression Main Ideas** | [youtu.be/3CC4N4z3GJc](https://www.youtube.com/watch?v=3CC4N4z3GJc) | 16 min |
| 5 | StatQuest: **XGBoost Part 1 — Regression** (drop if running over) | [youtu.be/OtD8wVaFm6E](https://www.youtube.com/watch?v=OtD8wVaFm6E) | 26 min |
| 6 | 3B1B Calculus Ep 7 (carry-over from Wed, if time — else move to Sun) | — | 15 min |

**Watch focus per video:**
- Decision Trees: **the Gini Impurity calculation step** — that's your blind spot. Skip ahead if Josh covers basics you already know.
- Random Forests Part 1: pay attention to what RF randomizes **at each split**, not just bootstrap sampling per tree.
- AdaBoost: this is what you incorrectly described when asked about gradient boosting — watch to cement the contrast.
- Gradient Boost Part 1: THE video that fixes your Q5 — what each new tree is trained to predict (residuals, not "wrong examples").
- XGBoost Part 1: optional but useful — extends gradient boost with regularization.

**Do NOT take written notes during videos. Watch cleanly first; notes come in Block 2 from memory.**

### Block 2: Rewrite the 5 Depth-Check Answers from Memory — 1 hr

Close all tabs. Create `Telco-churn-classification/notes/00-decision-trees-and-ensembles.md`. Answer the 5 questions **without peeking** in your own words with concrete examples:

1. Why do tree models not need feature scaling? (What arithmetic operation does a tree do at a split?)
2. Bagging vs boosting — mechanism AND which reduces variance vs bias. What does RF randomize beyond bootstrap?
3. How do Random Forest trees become *different* enough to benefit the ensemble?
4. Gini vs entropy — do they produce different trees in practice? Entropy shape for binary vs 3-class.
5. In gradient boosting, what is each new tree trained to predict? How does this differ from AdaBoost?

Then open StatQuest + Course 2 notes and fact-check yourself. Correct anything wrong. **Permanent reference — you'll re-read it every Sunday spaced-review cycle.**

### Break (15 min — walk away)

### Block 3: Telco Churn EDA — DEFERRED to Sunday

Block 1 + Block 2 took the full Saturday session (depth-check work ran longer than planned — *correctly so*, since that was the actual blocker). EDA pushes to Sunday per the fallback ladder.

**End of Saturday actual:** project structure created (`Telco-churn-classification/{data,model,notes}/`), full tree/ensemble reference document written (`notes/00-decision-trees-and-ensembles.md`, all 5 Q&A). Q5 (gradient boosting) flagged as still shaky — re-drill in Sunday spaced review for the next 3 weeks.

**Why this is OK**: depth gap was the real Project 2 blocker. EDA is straightforward data exploration that doesn't require deep theory. Slipping it 1 day costs nothing structural.

### If you run out of energy mid-Saturday (fallback ladder)

If Block 1 + 2 done but no time for Block 3 → **EDA pushes to Sunday morning, LR-from-scratch pushes to Week 3 Saturday**. Acceptable.

If only Block 1 done → **Block 2 (rewrite 5 Q&A) goes Sunday morning, EDA pushes to Week 3 Monday evening**. Less ideal but not fatal.

If Block 1 not done → revision becomes Sunday morning, everything else slides one day. You'd start Week 3 with EDA still pending. **Tell me if it goes here so I can re-plan Week 3 properly.**

---

## Sunday — Mixed Day (~4-4.5 hrs) — EDA + sklearn baselines

LR-from-scratch shifts to Week 3 Saturday (next big block of focused time). Sunday gets EDA back from Saturday + the original Sunday baseline work.

### Block A: Telco Churn EDA — 1.5 hrs

| Order | What | Time |
|-------|------|------|
| 1 | Move `WA_Fn-UseC_-Telco-Customer-Churn.csv` from repo root into `Telco-churn-classification/data/`. New notebook `model/01-eda.ipynb`. Load CSV. `.info()`, `.describe()`, `.head()`. | 15 min |
| 2 | Gotchas: (a) `TotalCharges` blank rows — which ones? Why? (Hint: look at their `tenure`.) Decide handling. (b) `Churn` class balance — % positive? (c) Drop `customerID`. | 30 min |
| 3 | Visualize 4-5 plots that tell a story: `tenure`, `MonthlyCharges`, `Contract`, `PaymentMethod` split by `Churn`. Don't make 30 random plots. | 30 min |
| 4 | Markdown summary in the notebook: "What did EDA reveal? Feature hypotheses?" 5-6 bullets. | 15 min |

### Break (15 min)

### Block B: sklearn baselines on Telco — 2 hrs

| Order | What | Time |
|-------|------|------|
| 5 | New notebook `model/02-baseline-logistic-regression.ipynb`. Load cleaned data from EDA. `pd.get_dummies` for categoricals. Single 80/20 split. Fit `LogisticRegression`. Print accuracy, precision, recall, F1, ROC-AUC, confusion matrix. | 50 min |
| 6 | New notebook `model/03-cross-validated-baseline.ipynb`. sklearn `Pipeline` (imputer → scaler → LogisticRegression) + `StratifiedKFold` + `cross_val_score`. Compare CV numbers to single-split. | 60 min |
| 7 | Project notes: `notes/01-eda-and-baseline.md`. Data shape, cleaning decisions, baseline AUC-ROC, what surprised you. | 15 min |

### DSA Block (30 min)

| Order | What | Time |
|-------|------|------|
| 9 | **Problem 14**: [Reverse String](https://leetcode.com/problems/reverse-string/) — Two Pointers, very quick. | 10-15 min |
| 10 | Quick scan: name the pattern for each of the 14 problems without looking at code. | 10-15 min |

### Spaced Review — DEFERRED to Week 3

Originally planned for today. Cut to make room for Saturday's slipped work. Re-scheduled to Week 3 Sunday — by then your `00-decision-trees-and-ensembles.md` will have a week of distance, making the review more useful anyway.

### Blog Setup — DEFERRED to Week 3

Cut for the same reason. Hashnode signup + post 1 skeleton moves to Week 3 Sunday (15-20 min cost — fits easily once the LR-from-scratch and baselines are done).

### 3B1B catch-up — only if you have leftover time

If Sunday lands under 5 hrs and you still have steam: 3B1B Calc Ep 7-8 + 3B1B LA Ep 9. Otherwise punt to Week 3 weekday slots.

---

## Week 2 Targets (revised after Sat depth-check overrun)

| Category | Target | How to verify | Status |
|----------|--------|---------------|--------|
| Course 2 | Week 4 videos done | — | ✅ |
| Trees/ensembles depth | StatQuest watched + 5-Q&A file | `notes/00-decision-trees-and-ensembles.md` | ✅ done Sat — Q5 flagged for re-drill |
| 3B1B Calculus | Ep 7-8 done | Notes | ⚠️ slipped — flexes to Week 3 weekdays |
| 3B1B Linear Algebra | Ep 7-9 done | Notes | ⚠️ Ep 7-8 ✅, Ep 9 → Week 3 |
| Project 2 — EDA | Notebook with findings | `01-eda.ipynb` | ⏳ Sun (was Sat) |
| Project 2 — LR from scratch | Cost curve decreasing, matches sklearn | `02-*.ipynb` | ⏭️ DEFERRED to Week 3 Saturday |
| Project 2 — sklearn baseline | Single-split + CV | baseline + cv notebooks | ⏳ Sun |
| Project 2 — notes | First project note | `notes/01-eda-and-baseline.md` | ⏳ Sun |
| DSA | 14 problems total | Pattern notes grouped | ✅ 13 done, #14 (Reverse String) Sun |
| Blog | Hashnode + skeleton | — | ⏭️ DEFERRED to Week 3 |
| Spaced Review | First session | Recall + comparison | ⏭️ DEFERRED to Week 3 |

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

### 8. Office work is killing Friday — protect it structurally
This week, **office work cost you both Wed reflection items AND all of Friday**. That's not bad luck, that's a pattern. Friday is the *last* weekday and your work backlog is highest then. Two structural fixes for Week 3 onward:
- **Front-load critical ML on Mon/Wed.** If something is non-negotiable for the week (e.g. course completion, project blocker), schedule it Mon or Wed — never Fri.
- **Friday becomes the lightest planned day.** Treat anything on Friday as "nice to have." If office crushes it, the weekend doesn't catch fire.
- **Saturday is the safety net.** Use it knowingly: if Friday slips, Sat absorbs. But don't *plan* for Friday slips — just stop being surprised by them.

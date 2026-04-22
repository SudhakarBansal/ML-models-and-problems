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

## Monday — ML Theory (1.5-2 hrs)
**Topic: Course 2 Week 4 START + Linear Algebra**

| Order | What | Time |
|-------|------|------|
| 1 | Course 2 Week 4 — first 3-4 videos (Decision Tree intuition, splitting on features, what makes a "good" split). | 50-60 min |
| 2 | Pause and reflect: in your house price project, you used regression with continuous predictions. How does a tree handle prediction differently? Write 3 sentences on the mental model shift from "fit a line" to "ask yes/no questions." | 10 min |
| 3 | Watch 3B1B Linear Algebra Ep 7: Dot products and duality | 15 min |
| 4 | Watch 3B1B Linear Algebra Ep 8: Cross products (skim — less critical for ML, 10 min OK) | 10-15 min |

**Done. Don't push into Project 2 today — Saturday is the right block for that.**

---

## Tuesday — DSA (1.5-2 hrs)
**Topic: Clear carry-over + Two Pointers pattern intro**

| Order | What | Time |
|-------|------|------|
| 1 | **Carry-over: [Maximum Subarray](https://leetcode.com/problems/maximum-subarray/)** — Kadane's algorithm. Try 25 min on your own first. Hint if stuck: "what does the answer look like if you process left-to-right?" Then NeetCode if needed. | 30-40 min |
| 2 | Write the Kadane pattern in one line ("running sum, reset when negative"). | 5 min |
| 3 | **Problem 9**: [Valid Palindrome](https://leetcode.com/problems/valid-palindrome/) — first Two Pointers problem. The pattern: two indices moving toward each other. | 20-25 min |
| 4 | **Problem 10**: [Move Zeroes](https://leetcode.com/problems/move-zeroes/) — Two Pointers, in-place modification. | 20-25 min |
| 5 | One-line pattern note for each. Group your notes by pattern (Arrays/Hashing vs Two Pointers) — start a real reference doc. | 10 min |

**Target: 3 problems. Running total: 10 problems.**

---

## Wednesday — ML Theory (1.5-2 hrs)
**Topic: Course 2 Week 4 — splitting criteria + Calculus**

| Order | What | Time |
|-------|------|------|
| 1 | Course 2 Week 4 — next videos (information gain, entropy, Gini impurity). This is the math behind "what makes a good split." | 45-60 min |
| 2 | Reflect: entropy is high when classes are mixed, low when pure. Why does the tree prefer splits that REDUCE entropy? Write 2-3 sentences. | 10 min |
| 3 | Watch 3B1B Calculus Ep 7 + Ep 8 (limits, integration intro) | 25-30 min |
| 4 | Quick connection note: gradient descent (Course 2 Week 2) and "find best split" (Week 4) are both optimization. What's different about how trees optimize vs how NN optimize? One paragraph. | 10 min |

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

## Friday — ML Theory (1.5-2 hrs)
**Topic: Course 2 Week 4 wrap-up + Code-from-scratch LR planning**

| Order | What | Time |
|-------|------|------|
| 1 | Course 2 Week 4 — finish remaining videos (Random Forest, ensembles, XGBoost intro). | 50-60 min |
| 2 | If lab is included, do the practice lab (decision tree on a small dataset). | 20-30 min |
| 3 | **Plan tomorrow's code-from-scratch LR**: Open a new notebook. Write a TODO list (cell with markdown): (1) sigmoid function (2) BCE cost function (3) gradient computation (4) training loop with gradient descent (5) test on toy synthetic data (6) compare to sklearn. Do NOT start coding — just plan. | 15 min |
| 4 | Watch 3B1B Linear Algebra Ep 9: Cramer's rule (geometric intuition) | 15 min |

**Course 2 Week 4 should be DONE or 90% done by end of Friday.**

---

## Saturday — Project 2 IGNITION (5 hrs)
**The big day. EDA + LR from scratch + sklearn baseline.**

### Block 1: Telco Churn EDA (1.5 hrs)

Set up your project directory like House Price project: `Telco-churn-classification/data/`, `model/`, `notes/`.

| Order | What | Time |
|-------|------|------|
| 1 | Create new notebook `01-eda.ipynb`. Load CSV. Run `.info()`, `.describe()`, `.head()`. | 15 min |
| 2 | Investigate the gotchas you already know about: (a) `TotalCharges` — which rows are blank? Why? (Hint: look at their `tenure`.) Decide handling. (b) `Churn` class balance — what % positive? (c) `customerID` — drop. | 30 min |
| 3 | Visualize: distribution of `tenure`, `MonthlyCharges`, `Contract`, `PaymentMethod` split by `Churn`. Pick 4-5 plots that tell a story. Don't make 30 random plots. | 30 min |
| 4 | Write a markdown summary in the notebook: "What did EDA reveal? What are my hypotheses about which features will matter most?" 5-6 bullet points. | 15 min |

### Break (15 min — actually walk away from the laptop)

### Block 2: Logistic Regression from scratch (2 hrs)

| Order | What | Time |
|-------|------|------|
| 5 | New notebook `02-logistic-regression-from-scratch.ipynb`. Implement sigmoid in numpy. Test on a vector. | 15 min |
| 6 | Implement BCE cost function. Sanity check: compute cost on known inputs (e.g., y=1, y_pred=0.9 should give small cost; y=1, y_pred=0.1 should give large cost). | 25 min |
| 7 | Implement gradient computation (derivative of BCE w.r.t. weights). Be careful with the dimensions — write down shapes before coding. | 30 min |
| 8 | Training loop: initialize weights, loop N iterations, update via gradient descent, track cost over iterations. Plot the cost curve — it MUST decrease monotonically (ish). If not, something's broken. | 30 min |
| 9 | Test on synthetic data (e.g., `make_classification` with 2 features). Compare your weights to sklearn `LogisticRegression`. They won't match exactly (different solvers) but predictions should agree on most points. | 20 min |

### Block 3: sklearn LR baseline on Telco (1 hr 15 min)

| Order | What | Time |
|-------|------|------|
| 10 | New notebook `03-baseline-logistic-regression.ipynb`. Load cleaned data from EDA. Encode categoricals (start simple — `pd.get_dummies` is fine for now). | 30 min |
| 11 | Single train/test split (80/20). Fit `LogisticRegression`. Print accuracy, precision, recall, F1, ROC-AUC, confusion matrix. | 20 min |
| 12 | Write a note: what's your baseline number? Is the accuracy misleading given class imbalance? (Hint: what would a "predict everyone stays" model score?) | 15 min |

**End of Saturday: You have an EDA notebook, a from-scratch LR notebook, and a sklearn baseline with metrics. This is real progress.**

---

## Sunday — Mixed Day (4-5 hrs)

### ML Block (2 hrs)

| Order | What | Time |
|-------|------|------|
| 1 | Project 2: Notebook `04-cross-validated-baseline.ipynb`. Set up sklearn `Pipeline` (imputer → scaler → LogisticRegression). Use `StratifiedKFold` with `cross_val_score` for proper CV-backed metrics. Compare to Saturday's single-split number. | 60 min |
| 2 | If Course 2 Week 4 isn't 100% done from Friday, finish it now. | 30-45 min |
| 3 | Write project notes file: `notes/01-eda-and-baseline.md`. Document: what the data looked like, what cleaning you did, what your baseline AUC-ROC is, what surprised you. Keep it intuition-driven like your House Price notes. | 15-20 min |

### DSA Block (45 min)

| Order | What | Time |
|-------|------|------|
| 4 | **Problem 14**: [Reverse String](https://leetcode.com/problems/reverse-string/) — Two Pointers, very quick. Should take 10 min. | 10-15 min |
| 5 | Review all 14 problems' pattern notes. Can you name the pattern for each without looking? | 15-20 min |

### Spaced Review (30 min) — FIRST one of the program

| Order | What | Time |
|-------|------|------|
| 6 | Close all notes. Write from memory: "What were the 3 most important things I learned in the House Price project?" Don't peek. | 10 min |
| 7 | Open House Price notes. Compare. What did you miss? What did you remember wrong? | 10 min |
| 8 | Re-read your Week 1 note `03-linear_transformations_and_computation_graphs.md`. Does the chain rule ↔ backprop connection still feel solid? If not, re-watch 3B1B NN Ch 3 (it's only 13 min). | 10 min |

### Blog Setup (30-45 min) — light, just unblock for next week

| Order | What | Time |
|-------|------|------|
| 9 | Sign up on [Hashnode](https://hashnode.com/) (recommended — better SEO, dev audience). Pick a username. Set up profile photo + 1-line bio. | 20 min |
| 10 | Create a draft post titled "What 4 iterations of linear regression taught me about ML". Paste in raw content from your House Price notes. **Do NOT polish yet — just get the skeleton.** Editing happens in Week 3. | 15-20 min |

---

## Week 2 Targets

| Category | Target | How to verify |
|----------|--------|---------------|
| Course 2 | Week 4 complete | Decision Tree, RF, XGBoost lectures + lab done |
| 3B1B Calculus | Episodes 7-8 done (1-8 total) | Notes |
| 3B1B Linear Algebra | Episodes 7-9 done (1-9 total) | Notes |
| Project 2 — EDA | Notebook done with documented findings | `01-eda.ipynb` + summary in markdown cell |
| Project 2 — LR from scratch | Working implementation, cost curve decreasing | `02-logistic-regression-from-scratch.ipynb` |
| Project 2 — sklearn baseline | Single-split + CV-backed metrics | `03` + `04` notebooks with AUC-ROC documented |
| Project 2 — notes | First project note written | `notes/01-eda-and-baseline.md` |
| DSA | 6 more problems (Kadane + 4 easy + 1 medium) | 14 total problems with pattern notes grouped |
| Blog | Hashnode account + draft skeleton of Post 1 | Account exists, draft saved (not published) |
| Spaced Review | First review session done | Recall exercise + comparison written |

---

## Phase 1 progress check

After Week 2, here's where you should be vs the original plan:

| Phase 1 deliverable | Total estimate | Done so far | Remaining |
|---|---|---|---|
| Course 2 (50% remaining at start) | 8-12 hrs | 8-10 hrs (W2-W4 done) | 0-2 hrs |
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

I'll adjust Week 3 based on that — Week 3 is where Project 2 goes deep (decision trees → RF → XGBoost on Telco, class imbalance handling, hyperparameter tuning).

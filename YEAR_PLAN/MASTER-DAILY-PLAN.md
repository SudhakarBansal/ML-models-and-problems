# ML Engineer — Master Daily Plan (3 hrs/day, day-wise)

> **This is the single source of truth.** Follow Day 1, Day 2, … in order. It is **day-wise, not date-wise** — if exams or life stop you for a week, you resume at the same Day number. No re-planning.
>
> Combines: **DSA drills** (continues `./DSA-interview-plan.md`) + **tooling fluency** (numpy/pandas/matplotlib) + **ML theory & intuition** + **hands-on implementation** (math of algorithms in numpy, including ones you've never done like Naive Bayes) + **4 portfolio projects**.
> Knowledge reference for every ML topic: `../youtube-ml-notes/INTERVIEW-PREP-PLAN.md` (cited as **§3A**, **§3B**, etc.).

---

## How long will this take?

**~4 months to interview-ready, ~4.5–5 months to fully polished** (4 deployed projects + mock interviews), at **3 hrs/day, ~7 days/week**.

- ~**120 study-days ≈ 17 weeks ≈ 4 months**, broken into 5 phases (below). (+~1 week for working through the reference resources below → call it **~4–4.5 months**.)
- Because it's day-wise, the calendar end-date floats with your exam breaks — but the *work* is fixed. Miss 10 days → you finish 10 days later, nothing is lost.
- This is realistic, not padded. You're learning ML theory + math + implementation **from scratch** while keeping DSA warm and shipping projects. Going faster means cutting projects or depth.

---

## Reference resources (read alongside the daily plan)

These are the **primary source materials** behind the CampusX/Krish Naik transcripts — the actual notebooks and question docs the videos were teaching from. All GitHub links below are **verified to exist** (the odd spellings are the real repo names). Use them *with* the daily plan: read the notebook's interview points in your **Theory block**, then still implement from scratch in your **Hands-on block** (the notebooks are mostly sklearn — your from-scratch numpy work is what builds the math intuition you're after).

### Tier 1 — high signal (use constantly)

| Resource | What it is | Where it maps in this plan |
|---|---|---|
| **Krish Naik — [Interview-Prepartion-Data-Science](https://github.com/krishnaik06/Interview-Prepartion-Data-Science)** | The canonical companion repo. 8 notebooks, one per algorithm: Day1 **Naive Bayes**, Day2 **Linear Regression**, Day3 **SVM**, Day4 **Decision Trees**, Day5 **Logistic Regression**, **Random Forest/Bagging**, **Boosting** (XGB/GBM/AdaBoost). | **Phase 2** — each algorithm day pairs with its notebook (see map below). Your #1 ML companion. |
| **"100 Most Common ML Interview Questions w/ Solutions" (Google Doc)** | CampusX's structured Q&A doc, linked from their first video. Complements §3A + the §5 Question Bank. | **Theory blocks** (Phase 1–2) as you hit each topic; **systematic passes** on the dedicated 100Q days (Days 24b, 35b) and **Phase 5** concept mocks. |
| **[learnwith.campusx.in](https://learnwith.campusx.in)** | CampusX's full site — slides/notes for every video in the playlist. | General reference whenever a transcript topic is fuzzy. |

### Tier 2 — useful (targeted depth + breadth)

| Resource | What it is | Where it maps |
|---|---|---|
| **Krish Naik — [Post_Pruning_DecisionTre](https://github.com/krishnaik06/Post_Pruning_DecisionTre)** | Deep-dive notebook on decision-tree cost-complexity post-pruning (`ccp_alpha`). | **Day 18** (U6 Decision Tree pruning). |
| **[iNeuron — interview-question-data-science-](https://github.com/iNeuronai/interview-question-data-science-)** | iNeuron's interview-question repo (2.1k★) — a *different* question set than Krish Naik's. Good for breadth. | **Phase 5** mock prep (broaden beyond the §5 bank). |
| **[sandipanpaul21 — DS Interview Question Bank Day1–Day30 (iNeuron)](https://github.com/sandipanpaul21/Data-Science-Interview-Question-Bank-Day1-Day30-iNeuron)** | The iNeuron 30-day question bank as clean per-day PDFs. | **Phase 5** — one "day" PDF per mock session. |
| **Krish Naik — sample DS resume (Google Drive)** | Reference resume from the "Resume for Freshers" video. | **Days 93–95** (resume rewrite, §3E). |

> **Phase-2 notebook map** (read the notebook's interview points in your Theory block on that day):
> Day 9–10 → Day2 Linear Regression · Day 11–12 → Day5 Logistic Regression · Day 15 → (KNN: no notebook, use §3B) · **Day 16–17 → Day1 Naive Bayes** · Day 18 → Day4 Decision Trees **+ Post_Pruning repo** · Day 19 → Random Forest/Bagging notebook · Day 20–21 → Boosting notebook · Day 22 → Day3 SVM.
>
> The Google Docs / Drive items have no public stable URL I can verify — open them from the matching video's description on YouTube (or the CampusX site). Everything with a link above is confirmed live.

---

## The daily 3-hour template (default day)

| Block | Time | What |
|---|---|---|
| **1. DSA** | 45 min | 1 problem from the DSA track (continues your existing curriculum). Solve cold, 45-min cap. If stuck → NeetCode video, **type** the solution yourself, log it `failed`, move on. |
| **2. Tooling drill** | 25 min | numpy / pandas / matplotlib reps (§3F). Goal: idioms *without Google*. |
| **3. ML theory + intuition** | 40 min | Read the day's topic in §3A, **rewrite it in your own words**, answer its Question-Bank items **out loud**, and add a row to your **Intuition Log** (see below). |
| **4. ML hands-on / project** | 70 min | Implement the day's algorithm from scratch in numpy **and** run the sklearn version — OR project work on project days. |

**On project-heavy days**, merge blocks 3+4 into one 110-min project block; keep DSA (45) + tooling (25) every single day — those are muscle memory and must not pause.

**Logging (non-negotiable, 2 min/day):** keep one running log file. For DSA reuse the format in `DSA-interview-plan.md`. For ML add: `Day N | topic | implemented? | could explain aloud? (y/n) | shaky points`.

**The Intuition Log** — your "when to use what" weapon. A single growing table you fill one row per algorithm as you reach it:

| Algorithm | One-line intuition | Use when… | Avoid when… | Needs scaling? | Sensitive to outliers? | Key hyperparams |
|---|---|---|---|---|---|---|

By the time it's full, *that table is your conceptual-interview cheat sheet.* Re-read it daily in Block 3's last 5 min.

---

## The ML hands-on curriculum (what Block 4 builds, in order)

You'll hit every interview algorithm at implementation level. "From scratch" = numpy, no sklearn for the core loop; then you run sklearn to compare and learn the API.

| Unit | Topic | From scratch? | Dataset |
|---|---|---|---|
| U0 | numpy fundamentals + pandas EDA | — (drills) | Titanic / Iris |
| U1 | Linear Regression (MSE, gradient descent) | ✅ numpy GD | California Housing |
| U2 | Logistic Regression (sigmoid, log-loss, GD) | ✅ numpy GD | Breast Cancer |
| U3 | Classification metrics (confusion matrix, P/R/F1, ROC-AUC) | ✅ numpy | reuse U2 (imbalanced slice) |
| U4 | KNN | ✅ numpy | Iris |
| U5 | **Naive Bayes** (Gaussian + Multinomial) — *new for you* | ✅ numpy Gaussian | SMS Spam |
| U6 | Decision Tree (entropy/gini, pruning) | sklearn + visualize | Titanic |
| U7 | Random Forest (bagging, OOB, importances) | sklearn | Titanic |
| U8 | Boosting (AdaBoost/GBM → XGBoost) | sklearn + xgboost | Titanic |
| U9 | SVM (margins, kernels) | sklearn | Breast Cancer |
| U10 | K-Means (+ elbow/silhouette) & PCA | ✅ numpy K-Means | Mall Customers / digits |
| U11 | Feature pipelines: scaling, encoding, `Pipeline`, `GridSearchCV`, cross-val | sklearn mastery | reuse |
| U12 | Gradient descent variants (batch/mini/SGD) + convergence plots | ✅ numpy | reuse U1 |
| U13 | Neural net: forward + **backprop by hand** in numpy (1 hidden layer) | ✅ numpy | moons / MNIST-small |
| U14 | PyTorch basics → MLP → small CNN; 2D conv from scratch | ✅ numpy conv + PyTorch | MNIST |
| U15 | System design drills (the 8-step framework, §3C) | written | — |
| U16 | RAG (chunking, embeddings, vector DB, eval) → becomes Project 3 | build | your docs |

---

## PHASE 1 — Finish drowsiness + ML foundations (Days 1–14)

*Goal: ship Project 1; make numpy/pandas reflexive; nail Linear/Logistic Regression + metrics with from-scratch code; keep DSA moving through Trees → Heap.*

### Day 1
- **DSA (45):** #100 Same Tree (Easy). Warm back into Trees recursion.
- **Tooling (25):** numpy-100, exercises 1–10 (array creation, dtypes, reshape).
- **Theory (40):** §3A *Core framing* — supervised/unsupervised, classification vs regression, parametric vs non-parametric. Start the Intuition Log.
- **Project (70):** **Drowsiness** — write down exactly what's left (the "still pending" list). Get it running end-to-end even if rough. Re-establish the pipeline: video frame → face/eye landmarks (dlib/mediapipe) → EAR (eye-aspect-ratio) or classifier → alert.

### Day 2
- **DSA (45):** #543 Diameter of Binary Tree (Easy) — "return something useful from each subtree."
- **Tooling (25):** numpy-100, 11–20 (indexing, slicing, boolean masks).
- **Theory (40):** §3A *Bias/variance/error* — overfitting vs underfitting, reducible vs irreducible. Answer aloud: "what fixes overfitting?"
- **Project (70):** Drowsiness — fix the top pending bug. Decide your detection metric (EAR threshold vs trained classifier) and *why* (this is interview gold later).

### Day 3
- **DSA (45):** #112 Path Sum (Easy).
- **Tooling (25):** numpy-100, 21–30 (broadcasting — spend real time here, it's the #1 numpy idea).
- **Theory (40):** §3A *Evaluation metrics* — confusion matrix, precision, recall. The FP-costly vs FN-costly examples (cancer vs spam).
- **Project (70):** Drowsiness — handle edge cases (no face detected, multiple faces, low light). Add the alert logic (sound/visual) with a debounce so it doesn't flicker.

### Day 4
- **DSA (45):** #98 Validate BST (Medium) — first Tree medium; mind the min/max bounds.
- **Tooling (25):** pandas — Kaggle "Pandas" micro-course lessons 1–2 (creating, reading, indexing/selecting).
- **Theory (40):** §3A metrics cont. — F1, ROC/AUC, why accuracy lies on imbalanced data.
- **Project (70):** Drowsiness — measure it: record a few clips (eyes open / drowsy / blinking) and check false alarms. Tune the threshold. *Note the precision/recall trade-off you just lived.*

### Day 5
- **DSA (45):** #235 Lowest Common Ancestor of a BST (Medium).
- **Tooling (25):** pandas micro-course 3 (summary functions, `map`/`apply`).
- **Theory (40):** §3A *Statistics* — mean vs median, normal dist (68/95/99.7), z-score, CLT.
- **Project (70):** Drowsiness — write the README: problem, approach, *why EAR/why this model*, results, limitations. This README is your interview script.

### Day 6 (lighter DSA day — recursion reset)
- **DSA (30):** *Trees felt shaky because recursion itself is shaky — fix the root cause first.* (a) Warm up with **pure recursion, no trees** — write `sum_list`, `reverse_string`, `fib` and **hand-trace one small input each** (draw the call stack going down, the returns coming up — see the *Recursion primer* below). (b) Then solve **#104 Maximum Depth of Binary Tree (Easy)** cold — the cleanest "return something useful from each subtree." Hand-trace it on a 3-node tree.
- **Tooling (25):** pandas micro-course 4 (grouping & sorting — `groupby`, `agg`).
- **Theory (40):** §3A *Probability vs likelihood*, *convex vs non-convex*. (Sets up gradient descent.)
- **Project (85):** Drowsiness — package it: clean repo, requirements.txt, a short demo GIF/video. Push to GitHub.

> **Recursion primer (re-read whenever a tree/recursion problem feels shaky):**
> Recursion has **two phases** — *going down* (calls pause and stack up as the input shrinks toward the base case) and *coming back up* (the base case returns, then each paused call resumes and combines the result). That stack of paused calls **is** "the flow beneath" — not magic, just frozen functions waiting on the one below.
> - **Trace it once, by hand.** Pick a tiny input, draw calls stacking down and values returning up (e.g. `factorial(3)` → `3*(2*(1))` → unwinds to 6). Seeing it bottom out correctly is what earns trust.
> - **Then use the leap of faith.** When *writing* the function, don't re-trace the whole stack — assume the recursive call already returns the right answer and reason about **one level** via 3 questions: **(1) Base case** — simplest input I can answer instantly? **(2) Ask the children** — recurse, trust the result. **(3) Combine** — turn their answers into mine.
> - For trees: base = empty node; ask = recurse left & right; combine = merge the two sub-answers (e.g. `max(left, right) + 1` for depth).
> - **Warm-up ladder** when shaky: `sum_list` → `reverse_string` → `fib` (two calls = closest to a tree) → then the tree problem. When the tree stops feeling different from `sum_list`, the shaky is gone.

### Day 7 (project finish)
- **DSA (30):** Pick weakest pattern of the week, 1 cold problem.
- **Tooling (25):** numpy-100, 31–40.
- **Project (125):** **Ship Drowsiness (P1).** Final polish, record demo, finalize README. Write 3 likely interview questions about it + your answers (e.g., "why EAR over a CNN?", "how would you reduce false alarms?", "how would you deploy this on-device?").

> **Milestone: Project 1 shipped.** From Day 8 you shift to the ML hands-on track; projects from here are built *while* you learn.

### Day 8
- **DSA (45):** #703 Kth Largest Element in a Stream (Easy) — **Heap intro.** Learn `heapq`.
- **Tooling (25):** numpy-100, 41–50.
- **Theory (40):** §3A *Gradient descent variants* + *feature scaling* (why GD needs it).
- **Hands-on (70):** **U0** — load Titanic in pandas, full EDA: `info`, `describe`, `value_counts`, missing values, a couple of `groupby`s, 2 matplotlib plots (hist + bar). No modeling yet — pure data fluency.

### Day 9
- **DSA (45):** #1046 Last Stone Weight (Easy, Heap).
- **Tooling (25):** matplotlib — build your one-page cheat-sheet (line/scatter/hist/bar/subplots/labels). Done once, reuse forever.
- **Theory (40):** §3A *Linear Regression* — the 5 assumptions, Ridge/Lasso.
- **Hands-on (70):** **U1 part 1** — implement linear regression in numpy: hypothesis `Xw+b`, MSE loss, gradients, the GD loop. Get loss to decrease.

### Day 10
- **DSA (45):** #215 Kth Largest in an Array (Medium, Heap) — then note the Quickselect alternative.
- **Tooling (25):** pandas — LeetCode "Introduction to Pandas" problems 1–3.
- **Theory (40):** Re-derive the linear-regression gradient on paper. Explain aloud why scaling helps convergence.
- **Hands-on (70):** **U1 part 2** — run `sklearn.LinearRegression` + `Ridge`/`Lasso` on California Housing; compare to your numpy version; plot predictions vs actual. Fill Intuition Log row.

### Day 11
- **DSA (45):** #347 Top K Frequent Elements (Medium, Heap + hashmap).
- **Tooling (25):** numpy-100, 51–60.
- **Theory (40):** §3A *Logistic Regression* — why "regression", log-odds, sigmoid, decision boundary.
- **Hands-on (70):** **U2 part 1** — implement logistic regression in numpy: sigmoid, binary cross-entropy, gradients, GD. Train on Breast Cancer.

### Day 12
- **DSA (45):** #295 Find Median from Data Stream (Hard — attempt; two-heap trick. Fallback: re-do #347 cleanly).
- **Tooling (25):** pandas — LeetCode Intro problems 4–6 (filtering, `apply`).
- **Theory (40):** §3A *Train/val/test*, cross-validation, time-based split & leakage.
- **Hands-on (70):** **U2 part 2** — sklearn `LogisticRegression`; plot the decision boundary; compare to your numpy version. Intuition Log row.

### Day 13
- **DSA (45):** #200 Number of Islands (Medium) — **Graph BFS/DFS intro.**
- **Tooling (25):** numpy-100, 61–70.
- **Theory (40):** §3A metrics recap — precision/recall/F1/ROC for the model you just built.
- **Hands-on (70):** **U3** — implement confusion matrix, precision, recall, F1 from scratch in numpy; verify against `sklearn.metrics`; plot an ROC curve. Make an imbalanced slice and watch accuracy lie.

### Day 14 (review + consolidate)
- **DSA (45):** #994 Rotting Oranges (Medium, multi-source BFS).
- **Tooling (25):** Free-recall test — open a blank file, write 15 numpy + 15 pandas idioms from memory. Whatever you blank on → tomorrow's drill focus.
- **Theory (40):** Self-quiz the entire §3A *Concepts/stats* + *Algorithms* Question Bank aloud. Mark every shaky one.
- **Hands-on (70):** Re-implement linear **or** logistic regression from a blank file, no reference. If you can't, that's your signal — redo it until you can.

> **Milestone (end of Day 14):** P1 shipped; numpy/pandas fluent enough to model; you can derive + implement linear & logistic regression and compute metrics by hand. This is the hard part — it's mostly downhill from here.

---

## PHASE 2 — All classical ML algorithms + Project 2 (Days 15–45)

*Goal: hands-on every classical algorithm (incl. Naive Bayes) with when-to-use intuition; build Project 2 (end-to-end imbalanced classification, deployed); DSA through Graphs → Backtracking → DP 1D.*

Daily structure = the standard template. DSA column continues one problem/day; ML column is the unit; tooling continues (numpy-100 → finish, then LeetCode Pandas track, then SQL basics on DataLemur).

### Days 15–24 — remaining algorithms

| Day | DSA | ML hands-on (Block 4) + theory (Block 3) |
|---|---|---|
| 15 | #133 Clone Graph (M) | **U4 KNN** from scratch in numpy (you already have the pieces from §3B); sklearn KNN; show scaling changes results. Intuition row. |
| 16 | #417 Pacific Atlantic Water Flow (M) | **U5 Naive Bayes pt1** — *the one you've never done.* Derive Bayes + the "naive" independence assumption. Implement **Gaussian NB** in numpy (class priors, per-feature mean/var, log-likelihood). |
| 17 | #207 Course Schedule (M, topo sort) | **U5 Naive Bayes pt2** — **Multinomial NB** for text: SMS Spam dataset, `CountVectorizer`/TF-IDF + sklearn `MultinomialNB`. Explain why NB shines on sparse text. Intuition row. |
| 18 | #78 Subsets (M) — **Backtracking intro** | **U6 Decision Tree** — entropy vs gini intuition; sklearn on Titanic; `plot_tree`; overfit full-depth then **prune** with `ccp_alpha`. Intuition row. |
| 19 | #46 Permutations (M) | **U7 Random Forest** — bagging intuition, OOB score, `feature_importances_`. Compare to single tree. Intuition row. |
| 20 | #77 Combinations (M) | **U8 Boosting pt1** — AdaBoost & Gradient Boosting intuition (sequential, fit residuals); sklearn. Bagging vs boosting aloud. |
| 21 | #39 Combination Sum (M) | **U8 Boosting pt2** — XGBoost hands-on; tune a couple params; compare RF vs XGB on Titanic. Intuition row. |
| 22 | (lighter) re-solve a shaky Backtracking problem | **U9 SVM** — margin/support-vectors/kernel intuition; sklearn linear vs RBF; show scaling matters. Intuition row. |
| 23 | #70 Climbing Stairs (E) — **DP intro** | **U10 K-Means pt1** — implement in numpy from scratch (§3B): init → assign → update → repeat. |
| 24 | #198 House Robber (M, DP 1D) | **U10 K-Means pt2** — elbow + silhouette to pick K; sklearn `KMeans`; **PCA** to 2D and plot clusters. Intuition row. |

### Day 24b (stretch — consolidation)
- **DSA (45):** timed medium, weakest pattern.
- **Tooling (25):** numpy/pandas free-recall test.
- **100-Questions pass (110):** systematic pass through the **"100 Most Common ML Questions" doc**, *algorithms + stats sections*. For every question: answer aloud first, then read the solution; anything you missed → add to your Intuition Log / a "shaky" list. Cross-check against the Krish Naik notebooks where an algorithm is fuzzy.

> *(The `b` days are inserted stretch days — they don't renumber the rest, so your alignment to Day 25, 26, … is unchanged.)*

> **Milestone (Day 24): Intuition Log has every classical algorithm.** Re-read it daily now. You can answer "which algorithm and why?" for any scenario.

### Days 25–35 — sklearn mastery + Project 2 build + DP

Project 2 = **end-to-end imbalanced binary classification, deployed.** Suggested: telco churn or credit-card fraud (Kaggle) — *imbalanced on purpose* so it exercises §3C lessons (resampling/class weights, precision/recall, leakage). This becomes a flagship resume project + your ML-system-design talking point.

| Day | DSA | ML / Project (Block 4) + theory |
|---|---|---|
| 25 | #213 House Robber II (M) | **U11** — sklearn `Pipeline`, `ColumnTransformer` (scaling + one-hot), `cross_val_score`, `GridSearchCV`. The professional workflow. |
| 26 | #300 Longest Increasing Subsequence (M) | **U12** — implement batch vs mini-batch vs SGD on your linreg; plot the three convergence curves. Now you *feel* the difference. |
| 27 | #322 Coin Change (M) | **P2 kickoff** — pick dataset, frame the problem (§3C step 1–2), EDA, quantify the imbalance. |
| 28 | #139 Word Break (M) | **P2** — features: encoding, scaling, train/val/test with **no leakage** (fit transforms on train only). |
| 29 | #91 Decode Ways (M) | **P2** — baseline (logistic regression), then RF/XGBoost. Handle imbalance (class weights + try SMOTE). Compare. |
| 30 | (lighter) re-solve weak DP problem | **P2** — evaluate with precision/recall/F1/ROC-AUC + confusion matrix; pick threshold deliberately; sliced metrics. |
| 31 | #62 Unique Paths (M) — **DP 2D** | **P2** — `GridSearchCV` tune the best model; feature importance / SHAP for explainability. |
| 32 | #1143 Longest Common Subsequence (M) | **P2** — wrap the model in a **FastAPI** endpoint (`/predict`); test with curl/Postman. (Your SDE skills shine.) |
| 33 | #72 Edit Distance (M/H) | **P2** — Dockerize; write README (problem → data → imbalance handling → models → metrics → API → limitations). |
| 34 | Mixed medium (pick weak pattern, timed) | **P2** — deploy free tier (Render/Railway/HF Spaces) **or** a clean local Docker demo. Record a short demo. |
| 35 | Mixed medium, timed <35 min | **P2 polish + ship.** Write 4 interview Qs about it (why this model? how handle imbalance? what's your precision/recall and why that threshold? how would it drift in production?). |

### Day 35b (stretch — consolidation)
- **DSA (45):** timed medium.
- **Tooling (25):** SQL warm-up (DataLemur, 2 easy).
- **100-Questions pass (110):** second systematic pass through the **"100 Most Common ML Questions" doc**, *remaining sections* (metrics, ensembles, feature engineering, deployment). Same drill: answer aloud → check → log gaps. By end of today you've seen all 100.

> **Milestone (Day 35): Project 2 shipped.** You now have a deployed, defensible ML system — the strongest single line on your resume.

### Days 36–45 — DSA → mock mode + ML consolidation + start NN

DSA new-pattern coverage is essentially complete (you've hit every Tier-1/2 pattern). Switch DSA to **mock mode**: 1 timed medium/day, rotate patterns, re-attempt anything you logged `failed`. (Mirrors `DSA-interview-plan.md` Phase C weeks 19–20.)

| Day | DSA (mock mode) | ML hands-on + theory |
|---|---|---|
| 36 | Timed medium — Arrays/Hashing | §3A *Deep learning* read: ANN building blocks, activations, loss, optimizers. |
| 37 | Timed medium — Trees | **U13 pt1** — forward pass of a 1-hidden-layer net in numpy (the linear-algebra you're weak on: shapes, matmuls). |
| 38 | Timed medium — Graphs | **U13 pt2** — **backprop by hand** in numpy (chain rule, gradients per layer). Train on the `make_moons` dataset. *This kills your "math of algorithms" weakness.* |
| 39 | Timed medium — DP | **U13 pt3** — vanishing/exploding gradients, Xavier/He init, batch norm intuition (§3A). |
| 40 | Timed medium — Heap | **U14 pt1** — PyTorch "60 Minute Blitz": tensors, autograd, `nn.Module`. |
| 41 | Timed medium — Backtracking | **U14 pt2** — rebuild your MLP in PyTorch; the canonical training loop from memory (forward→loss→`zero_grad`→`backward`→`step`). |
| 42 | (lighter) re-attempt a `failed` problem | **U14 pt3** — 2D convolution from scratch in numpy (§3B); verify against `torch.nn.Conv2d`. |
| 43 | Timed medium — Sliding Window | **U14 pt4** — small **CNN** on MNIST in PyTorch; train, eval, confusion matrix. |
| 44 | Timed medium — Binary Search | §3A *CNN* read: pooling, padding, stride, output-size formula, transfer learning, object detection (R-CNN→YOLO). Tie back to your drowsiness project. |
| 45 | Timed medium — Linked Lists | **Review day:** re-run the full §3A *Algorithms* + deep-learning Question Bank aloud. Update Intuition Log with NN/CNN rows. |

> **Milestone (Day 45):** every classical + basic deep-learning algorithm implemented and explainable; 2 projects shipped; DSA in confident mock mode.

---

## PHASE 3 — ML system design + GenAI/RAG (Project 3) (Days 46–70)

*Goal: master the §3C design framework on real prompts; build a production-flavored RAG app (Project 3) covering all of §3D; DSA stays in mock mode (1 timed problem/day).*

DSA from here: **1 timed medium/day, rotating patterns + re-attempting weak ones.** I'll stop listing specific DSA numbers — pull from `DSA-interview-plan.md` Phase B/C lists and any NeetCode-150 you haven't done. Tooling block shifts to **SQL** (DataLemur/StrataScratch) since DS/ML interviews test it, ~15 min/day, plus weekly numpy/pandas free-recall.

### Days 46–52 — ML system design drills (§3C, **U15**)
One "design X" written exercise per day in Block 4 (90 min with theory merged). Use the **8-step framework** every time; write it out, then read the matching worked pattern in §3C.

| Day | Design prompt |
|---|---|
| 46 | Re-read §3C framework; design **toxic-tweet classifier** (text, imbalance). |
| 47 | Design **Instagram-style feed ranking** (candidate-gen → rank → re-rank, two-tower). |
| 48 | Design a **recommendation system** (collaborative filtering, cold start) — Spotify/Netflix style. |
| 49 | Design **bot / fraud detection** (extreme imbalance, leakage, adversarial drift). |
| 50 | Design **ETA prediction** (baseline-first lookup table; features over time). |
| 51 | Design **deploy + monitor** an existing model (drift, A/B, safeguard metrics, rollback). |
| 52 | **Mock:** pick a random domain, design it in 40 min out loud / on paper, self-grade vs the framework. |

### Days 53–70 — Project 3: RAG document-Q&A app (covers all §3D)
Build incrementally; each day = a §3D concept turned into code. This ties directly to your mentor-track applied-AI work. Block 4 becomes a ~90-min build block (DSA + tooling stay).

| Day | RAG build step (concept → code) |
|---|---|
| 53 | Pick a corpus (your own docs / a manual). Naive pipeline: fixed-size chunk → embed (sentence-transformers) → FAISS → retrieve top-k → stuff into an LLM prompt. Get end-to-end working. |
| 54 | **Chunking levels** (§3D): implement structure-aware chunking; compare retrieval quality vs fixed-size. |
| 55 | Add **metadata** (source/section/page) + metadata filtering. |
| 56 | **Hybrid search** (semantic + keyword/BM25); observe better retrieval. |
| 57 | **Re-ranking** with a cross-encoder; measure the lift. |
| 58 | **Prompt engineering** (§3D): role/task/context/format/constraints; "answer only from context, else say I don't know." |
| 59 | **Evaluation loop**: build a small golden Q&A set; measure faithfulness / answer-relevance / context-precision (RAGAS or hand-rolled). |
| 60 | **Hallucination tiers** (§3D): add retrieval-score threshold + abstention; test it. |
| 61 | **Guardrails**: input PII masking + output checks (Guardrails-style, even simple regex + a check-LLM). |
| 62 | **API + UI**: FastAPI `/chat` with **streaming** (SSE/WebSocket); minimal frontend or Streamlit. |
| 63 | **Cost & latency**: instrument token counts; do the cost-estimation arithmetic (§3D) out loud. |
| 64 | **RAG vs fine-tuning** writeup (§3D): when you'd fine-tune instead; put it in the README. |
| 65 | Dockerize + deploy (HF Spaces / Render) or clean local demo. |
| 66 | README as interview script: architecture diagram, every design decision + alternative, eval numbers, limits. |
| 67 | Write 5 interview Qs about it (chunking choice? how reduced hallucination? cost at 10k users? how evaluate? failure modes?). |
| 68 | **Mock**: explain the whole RAG system in 10 min out loud, record yourself, watch it back. |
| 69 | Buffer / fix anything broken. |
| 70 | **Ship Project 3.** Push, demo, link on LinkedIn. |

> **Milestone (Day 70): 3 projects shipped** (CV, tabular ML, GenAI/RAG); you can run any §3C design and any §3D GenAI question with depth.

---

## PHASE 4 — Project 4 + deepening + DSA mocks (Days 71–95)

*Goal: a 4th project that leverages your existing assets; deepen weak spots; DSA daily timed mediums.*

**Project 4 — pick ONE** (build Days 71–88, same incremental style as P3):
- **(a) Recommendation system** — you already have `recommendation-system/` with MovieLens data. Turn it into a clean, evaluated, deployed recommender (collaborative filtering + content-based + cold-start handling). Directly demonstrates §3C recsys.
- **(b) NLP classifier, deployed** — e.g., a fine-tuned sentiment/intent/toxicity model served via API, with an eval suite. Shows model-training + serving.
- **(c) A mentor-track problem productionized** — turn detection / ASR-correction into a polished, documented, deployed artifact.

Pick the one closest to the **jobs you're targeting** (recsys = product cos; NLP/serving = ML eng; mentor-track = aligns with your current depth bar).

| Days | DSA | Focus |
|---|---|---|
| 71–88 | 1 timed medium/day, rotate patterns; re-do any `failed` | **Build Project 4** in Block 4 (~90 min). Same rigor: frame → data → model → eval → deploy → README → interview Qs. |
| 89–92 | 1 timed medium/day | **Deepen your 3 weakest topics** (from your logs) — re-implement or re-explain until solid. Likely candidates: backprop math, SVM kernels, system-design monitoring, RAG eval. |
| 93–95 | Timed mediums + 1 hard | **Resume** (§3E): rewrite impact-first, tailored; 4 projects as defendable bullets. Get it ATS-clean. Use **Krish Naik's sample DS resume** (Drive link in Resources) as a structure reference. |

> **Milestone (Day 88): Project 4 shipped — 4 solid, deployed, defensible projects.**

---

## PHASE 5 — Mock interviews + applications (Days 96–120)

*Goal: convert knowledge into confident performance; start applying.*

| Days | What (each day, 3 hrs) |
|---|---|
| 96–100 | **Concept mocks:** daily, rapid-fire the §5 Question Bank out loud (record), then one **iNeuron 30-day bank** PDF (sandipanpaul repo) + a slice of the **iNeuron interview-question repo** for fresh questions you haven't rehearsed. + 1 DSA timed medium. + apply to 3–5 roles/day. |
| 101–105 | **Coding mocks:** implement a from-scratch algorithm (K-means/KNN/conv/NB) under 45-min timer, narrating. + DSA medium. + applications. |
| 106–110 | **System-design mocks:** 1 §3C design + 1 §3D GenAI design per day, out loud, timed. + applications. |
| 111–115 | **Project deep-dive mocks:** have someone (or self-record) grill you on each of the 4 projects — defend every line (§3E #1 killer is failing this). + applications. |
| 116–120 | **Full mock loops** (mix all rounds) + behavioral ("why SDE→ML?", a failure story) + iterate resume from feedback + keep applying. |

> **Milestone (Day 120 ≈ Month 4): interview-ready.** Continue applying + mocking until offers; loop weak areas surfaced in real interviews.

---

## Weekly rhythm & rules (so it stays consistent)

- **Every day, no matter what:** DSA (45) + tooling (25). These are muscle memory; pausing them is the only true setback.
- **One lighter DSA day per ~week** (re-solve, don't push new) to avoid burnout — already baked in.
- **End of each week (Sunday, last 15 min):** scan your logs. Any ML topic you couldn't explain aloud, or DSA pattern with 2+ `failed` → it gets a slot next week. This is the *only* adjustment you make — the plan itself doesn't change.
- **Exams / life:** just stop. Resume at the same Day number. Keep the 25-min tooling drill alive even on exam days if at all possible (it's small and decays fast).
- **Don't chase new shiny topics.** This plan is complete. Finishing it > optimizing it.

---

## Quick map: this plan → your other files

- **DSA problems & pattern notes:** `./DSA-interview-plan.md` (this plan continues it from #102; from ~Day 36 it's mock mode).
- **All ML/GenAI knowledge (the "what to learn"):** `../youtube-ml-notes/INTERVIEW-PREP-PLAN.md` — §3A concepts, §3B coding, §3C system design, §3D GenAI, §3E behavioral, §3F tooling, §5 question bank.
- **This file = the "when/how", day by day.** Follow it. Log daily. Adjust only via the weekly scan.

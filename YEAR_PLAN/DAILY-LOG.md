# Daily Log — ML Eng Master Plan

> Companion tracker for `./MASTER-DAILY-PLAN.md`. **Zero-friction:** each day's plan is pre-filled — you just fill the **Log** cell.
> Log shorthand: DSA verdict = `clean / hesitated / failed / gaveup` + time · `aloud?` = could you explain the ML topic out loud (y/n) · `impl?` = did the code run / from-scratch worked (y/n). Jot shaky points to revisit.

---

## Phase 1 — Finish drowsiness + ML foundations (Days 1–14)

| Day | DSA | ML theory (explain aloud) | Hands-on / Project | Log (verdict · aloud? · impl? · shaky) |
|---|---|---|---|---|
| 1 | #100 Same Tree | Core framing (sup/unsup, class/reg, parametric) | Drowsiness: list what's left; run end-to-end | |
| 2 | #543 Diameter | Bias/variance, over/underfit | Drowsiness: top bug; choose EAR vs classifier + why | |
| 3 | #112 Path Sum | Metrics: confusion, precision, recall | Drowsiness: edge cases + alert debounce | |
| 4 | #98 Validate BST | Metrics: F1, ROC/AUC, accuracy lies | Drowsiness: record clips, tune threshold | |
| 5 | #235 LCA of BST | Stats: mean/median, normal, z, CLT | Drowsiness: write README (why this approach) | |
| 6 | recursion reset: warm-ups (sum_list/reverse/fib, hand-traced) → #104 Max Depth cold | Probability vs likelihood, convex | Drowsiness: package, requirements, demo GIF | |
| 7 | weakest pattern | — | **Ship Drowsiness (P1)** + 3 interview Qs | |
| 8 | #703 Kth Largest Stream (Heap intro) | GD variants + feature scaling | U0: Titanic EDA in pandas | |
| 9 | #1046 Last Stone Weight | Linear Reg: 5 assumptions, Ridge/Lasso | U1.1: numpy linreg GD (loss↓) | |
| 10 | #215 Kth Largest Array | Re-derive linreg gradient on paper | U1.2: sklearn LinearReg/Ridge/Lasso vs yours | |
| 11 | #347 Top K Frequent | Logistic Reg: log-odds, sigmoid | U2.1: numpy logreg (sigmoid, BCE, GD) | |
| 12 | #295 Median from Stream (try) | Train/val/test, CV, leakage | U2.2: sklearn LogReg + decision boundary | |
| 13 | #200 Number of Islands (Graph intro) | Metrics recap on your model | U3: confusion/P/R/F1 from scratch + ROC | |
| 14 | #994 Rotting Oranges | Self-quiz all §3A concepts/algos aloud | Re-implement lin/log reg from blank file | |

---

## Phase 2 — All classical algorithms + Project 2 (Days 15–45)

*Each algorithm day: read the matching Krish Naik notebook's interview points (Theory block), then implement (Hands-on). Notebook map is in the plan's Resources section.*

| Day | DSA | ML theory | Hands-on / Project | Log |
|---|---|---|---|---|
| 15 | #133 Clone Graph | KNN | U4: KNN from scratch (numpy) + sklearn | |
| 16 | #417 Pacific Atlantic | **Naive Bayes** derive (Bayes + naive) | U5.1: Gaussian NB from scratch (notebook Day1) | |
| 17 | #207 Course Schedule | NB for text (why sparse-text) | U5.2: Multinomial NB on SMS Spam | |
| 18 | #78 Subsets (Backtracking intro) | Decision Tree entropy/gini | U6: DT + prune `ccp_alpha` (Day4 + Post_Pruning repo) | |
| 19 | #46 Permutations | Random Forest: bagging, OOB | U7: RF, OOB, feature importance (RF/Bagging nb) | |
| 20 | #77 Combinations | Boosting: Ada/GBM intuition | U8.1: AdaBoost/GBM (Boosting nb) | |
| 21 | #39 Combination Sum | Bagging vs boosting aloud | U8.2: XGBoost; RF vs XGB compare | |
| 22 | re-solve backtracking | SVM: margin, kernels | U9: SVM linear vs RBF (Day3 nb) | |
| 23 | #70 Climbing Stairs (DP intro) | K-Means | U10.1: K-Means from scratch (numpy) | |
| 24 | #198 House Robber | K-Means: elbow/silhouette | U10.2: elbow + silhouette + PCA plot | |
| **24b** | timed medium | **100Q doc pass: algorithms + stats** | (numpy/pandas free-recall) | |
| 25 | #213 House Robber II | sklearn pro workflow | U11: Pipeline, ColumnTransformer, GridSearchCV | |
| 26 | #300 Longest Incr. Subseq. | GD variants felt | U12: batch/mini/SGD + 3 convergence curves | |
| 27 | #322 Coin Change | P2 framing | **P2 kickoff:** dataset, frame, EDA, imbalance | |
| 28 | #139 Word Break | leakage discipline | P2: features, encode/scale, no-leak split | |
| 29 | #91 Decode Ways | imbalance handling | P2: baseline → RF/XGB; class weights + SMOTE | |
| 30 | re-solve weak DP | threshold choice | P2: P/R/F1/ROC + confusion + pick threshold | |
| 31 | #62 Unique Paths (DP 2D) | explainability | P2: GridSearch tune + SHAP/importances | |
| 32 | #1143 LCS | — | P2: wrap in FastAPI `/predict`, test | |
| 33 | #72 Edit Distance | — | P2: Dockerize + README | |
| 34 | mixed medium (timed) | — | P2: deploy (Render/HF) or local Docker demo | |
| 35 | mixed medium <35 min | — | **Ship P2** + 4 interview Qs | |
| **35b** | timed medium | **100Q doc pass: metrics/ensembles/deploy** | (SQL: DataLemur ×2) | |
| 36 | timed medium (Arrays) | §3A deep-learning read | (consolidate) | |
| 37 | timed medium (Trees) | NN forward intuition | U13.1: forward pass in numpy (shapes/matmul) | |
| 38 | timed medium (Graphs) | backprop = chain rule | U13.2: **backprop by hand** (numpy, moons) | |
| 39 | timed medium (DP) | vanish/explode, Xavier/He | U13.3: init + batch-norm intuition | |
| 40 | timed medium (Heap) | PyTorch model anatomy | U14.1: PyTorch 60-min blitz | |
| 41 | timed medium (Backtracking) | training loop from memory | U14.2: rebuild MLP in PyTorch | |
| 42 | re-attempt a `failed` | — | U14.3: 2D conv from scratch vs `Conv2d` | |
| 43 | timed medium (Sliding Window) | — | U14.4: small CNN on MNIST | |
| 44 | timed medium (Binary Search) | §3A CNN read (pool/pad/stride/transfer) | tie back to drowsiness | |
| 45 | timed medium (Linked Lists) | re-run §3A algo + DL question bank aloud | update Intuition Log (NN/CNN rows) | |

---

## Phase 3 — System design + RAG (Project 3) (Days 46–70)

*DSA = 1 timed medium/day (rotate + re-do `failed`). Tooling block → SQL ~15 min/day + weekly numpy/pandas recall.*

| Day | DSA (timed medium) | Focus (Block 4, ~90 min) | Log |
|---|---|---|---|
| 46 | ✔ | SD: re-read §3C; design toxic-tweet classifier | |
| 47 | ✔ | SD: Instagram feed ranking (two-tower) | |
| 48 | ✔ | SD: recommendation system (collab filtering, cold start) | |
| 49 | ✔ | SD: bot/fraud detection (imbalance, leakage, drift) | |
| 50 | ✔ | SD: ETA prediction (baseline-first) | |
| 51 | ✔ | SD: deploy + monitor (drift, A/B, safeguard, rollback) | |
| 52 | ✔ | SD mock: random domain in 40 min, self-grade | |
| 53 | ✔ | RAG: naive pipeline end-to-end (chunk→embed→FAISS→LLM) | |
| 54 | ✔ | RAG: structure-aware chunking vs fixed | |
| 55 | ✔ | RAG: metadata + filtering | |
| 56 | ✔ | RAG: hybrid search (semantic + BM25) | |
| 57 | ✔ | RAG: cross-encoder re-ranking | |
| 58 | ✔ | RAG: prompt engineering (role/task/context/format/constraints) | |
| 59 | ✔ | RAG: eval loop (golden set, faithfulness/relevance/precision) | |
| 60 | ✔ | RAG: hallucination threshold + abstention | |
| 61 | ✔ | RAG: guardrails (PII mask, output checks) | |
| 62 | ✔ | RAG: FastAPI `/chat` + streaming (SSE) + UI | |
| 63 | ✔ | RAG: cost + latency instrumentation | |
| 64 | ✔ | RAG: RAG-vs-fine-tuning writeup | |
| 65 | ✔ | RAG: Dockerize + deploy | |
| 66 | ✔ | RAG: README as interview script + diagram | |
| 67 | ✔ | RAG: write 5 interview Qs | |
| 68 | ✔ | RAG: explain whole system in 10 min (record) | |
| 69 | ✔ | RAG: buffer / fix | |
| 70 | ✔ | **Ship P3** + LinkedIn post | |

---

## Phase 4 — Project 4 + deepen + resume (Days 71–95)

| Day | DSA | Focus | Log |
|---|---|---|---|
| 71–88 | 1 timed medium/day | **Build P4** (recsys / NLP-served / mentor-track productionized) — frame→data→model→eval→deploy→README→interview-Qs | |
| 89–92 | 1 timed medium/day | Deepen 3 weakest topics (from logs) | |
| 93–95 | timed mediums + 1 hard | **Resume** impact-first (§3E) + Krish Naik sample as reference | |

*(Expand 71–88 into one row per day here as you go — copy the row format.)*

---

## Phase 5 — Mock interviews + applications (Days 96–120)

| Day | Focus (each day, 3 hrs) | Log |
|---|---|---|
| 96–100 | Concept mocks (§5 bank + iNeuron banks) + 1 DSA medium + apply 3–5/day | |
| 101–105 | Coding mocks (from-scratch algo, 45-min timer) + DSA + apply | |
| 106–110 | System-design mocks (1 §3C + 1 §3D/day) + apply | |
| 111–115 | Project deep-dive mocks (defend every line) + apply | |
| 116–120 | Full mock loops + behavioral + iterate resume + apply | |

---

## Tooling drill checklist (Block 2 — tick as you go)

**numpy** — `rougier/numpy-100`
- [ ] 1–10  [ ] 11–20  [ ] 21–30 (broadcasting)  [ ] 31–40  [ ] 41–50  [ ] 51–60  [ ] 61–70  [ ] 71–80  [ ] 81–90  [ ] 91–100

**pandas** — Kaggle micro-course → LeetCode Pandas track
- [ ] Kaggle 1–2  [ ] Kaggle 3  [ ] Kaggle 4 (groupby)
- [ ] LC Intro 1–3  [ ] LC Intro 4–6  [ ] LC "30 Days of Pandas" (tick weekly) ▢▢▢▢

**matplotlib** — one-page cheat-sheet (line/scatter/hist/bar/subplots/labels)  [ ] built

**SQL** (Phase 3+) — DataLemur / StrataScratch easy→medium  ▢▢▢▢▢ (tick per session)

**Weekly free-recall test** (Sunday): write 15 numpy + 15 pandas idioms blank.
- Wk1 ▢  Wk2 ▢  Wk3 ▢  Wk4 ▢  Wk5 ▢  Wk6 ▢  Wk7 ▢  Wk8 ▢  …

---

## Intuition Log — *"when to use what"* (fill one row per algorithm as you reach it)

| Algorithm | One-line intuition | Use when… | Avoid when… | Scaling? | Outlier-sensitive? | Key hyperparams |
|---|---|---|---|---|---|---|
| Linear Regression | | | | | | |
| Logistic Regression | | | | | | |
| KNN | | | | | | |
| Naive Bayes | | | | | | |
| Decision Tree | | | | | | |
| Random Forest | | | | | | |
| AdaBoost / GBM / XGBoost | | | | | | |
| SVM | | | | | | |
| K-Means | | | | | | |
| Neural Net (MLP) | | | | | | |
| CNN | | | | | | |

---

## Project tracker

| # | Project | Status | Deployed? | README + interview-Qs? | Link |
|---|---|---|---|---|---|
| P1 | Drowsiness detection | in progress | | | |
| P2 | Imbalanced tabular ML + FastAPI | not started | | | |
| P3 | RAG document-Q&A app | not started | | | |
| P4 | (recsys / NLP / mentor-track) | not started | | | |

---

## Weekly review (every Sunday, 15 min)

Scan the week's Log. Then:
- ML topics marked `aloud? n` → schedule into next week's Theory blocks.
- DSA patterns with 2+ `failed`/`gaveup` → add an extra problem next weekend.
- Tooling idioms you blanked on the free-recall test → next week's drill focus.

**Running shaky list (carry forward until cleared):**
- 
- 
- 

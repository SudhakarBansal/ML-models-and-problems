# ML Drills — Daily Retrieval Practice

> **Purpose**: 15-min daily ML drill to keep Course 1 + Course 2 + Project 1 content "in the skin." Retrieval practice > re-reading. Answer cold, self-check against notes afterwards.
>
> **Starts**: Mon Apr 27, 2026 (Week 3).

---

## Protocol

- **15-min hard cap.** At the start of each ML study session.
- **One drill per day** on Mon/Wed/Fri/Sun. Tue/Thu are DSA drill days — don't stack.
- **Pen + paper** for derivations; **blank notebook cell** for coding. No peeking at notes, videos, or internet during the 15 min.
- After the timer ends: open your references (Course notes, 3B1B videos, StatQuest for trees/ensembles, Project 1 notes) and **self-check**. Where did you stumble? Fix the note or the understanding.
- Log in the table at the bottom: date, topic, question keyword, self-grade (`strong` / `shaky` / `failed`).
- Any `failed` → next Sunday's slot becomes "re-attempt this drill."

## Rotation

| Day | Topic area | Coverage base |
|---|---|---|
| Mon | Classical ML fundamentals | Course 1 + Course 2 W3 + Project 1 |
| Tue | *(DSA drill day — no ML drill)* | — |
| Wed | Trees & Ensembles (over-drill, shaky area) | Course 2 W4 + Friday revision (StatQuest) |
| Thu | *(DSA drill day — no ML drill)* | — |
| Fri | Neural Networks | Course 2 W1-W2 + 3B1B NN series |
| Sat | *(Project 2 day — no drills)* | — |
| Sun | Math / Evaluation / Project 1 — user's call; default = weakest from the week | 3B1B + Project 1 notes |

> The 5 daily topic areas (Classical ML / Math / Trees / Evaluation / NN) don't all fit into 4 drill days per week. Tue and Thu's topics (Math, Evaluation) rotate into **Sunday's flex slot** when not recently covered. The week's format rotation below surfaces all 5.

## Format variety

Each drill uses one of 5 formats, rotating so no muscle atrophies:

| Format | What it trains |
|---|---|
| **Conceptual** | Verbal explanation — the interview-day muscle |
| **Derivation** | Math on paper — foundations |
| **Coding** | Small numpy implementation (~10 lines) — library fluency |
| **Interview** | Whiteboard-style walkthrough — structure + clarity |
| **Trade-off** | "Which would you choose and why" — judgment |

---

## Curriculum — Weeks 3 through 6

### Week 3 (Apr 27 – May 3)

| Day | Topic | Format | Drill |
|---|---|---|---|
| Mon | Classical ML | Conceptual | Why does adding a Ridge penalty `λ·‖w‖²` to MSE prevent overfitting? Explain in 2-3 sentences **without** using the word "shrink". |
| Wed | Trees & Ensembles | Interview | Core difference between AdaBoost and gradient boosting: *what does each new tree fit?* |
| Fri | Neural Networks | Conceptual | Why do we need *non-linear* activation functions? What happens if you stack 5 Dense layers with no activation? |
| Sun | Project 1 | Interview | Record yourself (voice memo) explaining your 4 house-price iterations — what you added each time, why, what it bought you. 5 min target. |

### Week 4 (May 4 – 10)

| Day | Topic | Format | Drill |
|---|---|---|---|
| Mon | Classical ML | Trade-off | 1000 rows × 2 features: Ridge or Lasso? Now 1000 rows × 10,000 features: which and why? |
| Wed | Trees & Ensembles | Derivation | Node with 40 positive, 60 negative samples. Compute entropy *by hand*. Compute Gini. Compare the values. |
| Fri | Neural Networks | Derivation | Derive `σ'(x) = σ(x)(1 − σ(x))` where σ is the sigmoid. Show the chain-rule step explicitly. |
| Sun | Math + Project 1 | Derivation | Re-derive the Normal Equation from scratch on paper. One-sentence: *when does it fail?* |

### Week 5 (May 11 – 17)

| Day | Topic | Format | Drill |
|---|---|---|---|
| Mon | Classical ML | Conceptual | Define *data leakage*. Give 3 concrete examples of how it sneaks into an ML pipeline. |
| Wed | Trees & Ensembles | Interview | RF with 100 trees, all fit on the same 1000 rows. How are the trees *different enough* for the ensemble to help? |
| Fri | Neural Networks | Coding | Implement `softmax(x)` in numpy. Must be **numerically stable** for large inputs (overflow). |
| Sun | Math | Conceptual | What does it mean *geometrically* for two vectors to be orthogonal? Why does this matter for PCA / feature selection? |

### Week 6 (May 18 – 24)

| Day | Topic | Format | Drill |
|---|---|---|---|
| Mon | Classical ML | Derivation | Starting from BCE loss `−[y log(p) + (1−y) log(1−p)]`, derive the gradient w.r.t. logistic regression weights w. |
| Wed | Trees & Ensembles | Trade-off | 2 scenarios where you'd pick RF over XGBoost, 2 where you'd pick XGBoost over RF. |
| Fri | Neural Networks | Interview | Walk through one backprop iteration for a 2-layer NN (input → hidden → output). What's computed, what's updated. |
| Sun | Evaluation | Trade-off | Predicting cancer from medical images. Optimize for precision, recall, or F1? Defend your choice. |

---

## Drill Log

_Log every drill. After 4 weeks, scan for any topic/format that repeatedly shows `shaky` or `failed` — those are your interview risks._

| Date | Topic | Format | Keyword | Self-grade |
|------|-------|--------|---------|------------|
| 2026-04-27 | Classical ML | Conceptual | Ridge / λ‖w‖² | shaky |
| 2026-04-29 | Trees & Ensembles | Interview | AdaBoost vs Gradient Boost — "what does each new tree fit?" | shaky |

---

## Self-check references

When the 15 min is up, verify your answer against:

| Topic area | Go-to reference |
|---|---|
| Classical ML (LR, logistic, regularization) | Andrew Ng Course 1 notes + Course 2 W3 notes + Project 1 notes |
| Math (LA) | 3B1B Essence of Linear Algebra |
| Math (Calc) | 3B1B Essence of Calculus |
| Trees & Ensembles | StatQuest: Gini Impurity / RF Parts 1 & 2 / AdaBoost / Gradient Boost Part 1 / XGBoost Part 1 |
| Evaluation / Metrics / CV | Course 2 W3 (ML advice) + your house-price CV notebook |
| Neural Networks | Course 2 W1-W2 + 3B1B Neural Networks Ch 1-3 |

**Rule**: if the self-check reveals a real gap (not just a wording fumble), spend *one* extra session re-watching or re-reading that reference. Don't let a `failed` drill sit.

# 1-Year ML Engineer Transition Plan (v2 — reviewed & revised)
## April 2026 → May 2027 | Bangalore

---

## Current State

- **Role**: SDE, 2 yrs exp (frontend-heavy, some Node.js/Spring Boot backend)
- **Salary**: 7.5 LPA
- **ML**: Completed Andrew Ng Course 1 (Supervised Learning). Built house price prediction project (4 iterations, cross-validation from scratch).
- **Math**: Good aptitude, needs refresh (linear algebra, calculus, probability)
- **DSA**: Easy level on Leetcode
- **Education**: MCA from IGNOU (in progress, exams Jun-Jul & Dec-Jan)

## Target State

- **Role**: ML Engineer / Applied ML Engineer in Bangalore
- **Skills**: Strong classical ML + working knowledge of DL, unsupervised learning, RL
- **Portfolio**: 5 projects (1 deep area + 4 solid supporting), technical blog, clean GitHub
- **Production ML**: Experiment tracking (W&B/MLflow) + one model served via API
- **DSA**: Consistent Leetcode medium solver
- **Interview-ready**: Can answer 3 levels deep on any project or ML concept, including ML system design basics

## Strategy: Layered Depth

```
Classical ML          ████████████████████  (deep — multiple projects, strong theory)
Unsupervised Learning ████████████          (solid — one strong project, clear understanding)
Neural Networks / DL  ████████████          (solid — one meaningful project, understand internals)
Reinforcement Learning████████              (foundational — one clean project, core concepts)
```

Not equal depth. One deep pillar (classical ML) + solid supporting areas.

---

## Time Budget

| | Weekdays | Weekends | Weekly Total |
|---|---|---|---|
| **ML (theory + projects + math)** | Mon/Wed/Fri: 1.5-2 hrs each | Sat: 5 hrs, Sun: 3 hrs | ~12-14 hrs |
| **DSA** | Tue/Thu: 1.5-2 hrs each | Sun: 1 hr | ~4-5 hrs |
| **Blog / Review** | — | Sun: 1 hr | ~1 hr |
| **Total** | ~7.5-10 hrs | ~10 hrs | ~17-20 hrs |

**Realistic after life/burnout/interruptions: ~14-15 hrs/week**

**Exam weeks**: DSA only (1 easy/day, 30 min). Everything else → MCA.

**Total usable hours over 12 months: ~700-750**

---

## Phase 1: Foundations (Mid-April → End of May 2026)
### ~7 weeks | Full capacity

### ML Learning
- [ ] **Andrew Ng Course 2**: Advanced Learning Algorithms
  - Neural networks (forward prop, backprop, activation functions)
  - Decision trees & tree ensembles (random forest, XGBoost)
  - Bias-variance tradeoff, ML development advice
  - **Time**: ~25-30 hrs
- [ ] **Finish house price prediction loose ends**
  - Task 3: Understand Normal Equation
  - Task 4: Reason about why Ridge regularization works (alpha*I in the equation)
  - Fix the `.copy()` bug in K-fold CV
  - **Time**: ~5 hrs

### Math (alongside ML, not separate)
- [ ] **3Blue1Brown "Essence of Linear Algebra"** (YouTube, 16 episodes)
  - Vectors, linear transformations, matrix multiplication, determinants, eigenvalues
  - Watch 2-3 episodes per week alongside Course 2
  - **Time**: ~8 hrs
- [ ] **3Blue1Brown "Essence of Calculus"** (YouTube)
  - Derivatives, chain rule, gradients — connects directly to backpropagation
  - **Time**: ~6 hrs

### Project
- [ ] **Project 2: Binary Classification** (Logistic Regression → Decision Trees → XGBoost)
  - Dataset: Loan default prediction or customer churn (pick real data from Kaggle/UCI)
  - Must cover: logistic regression, decision trees, random forest, XGBoost comparison
  - Must cover: class imbalance handling, precision/recall/F1, ROC-AUC, confusion matrix
  - Must cover: **SHAP values** for model interpretability — explain WHY the model predicts what it does
  - Must cover: **Experiment tracking** — use [Weights & Biases](https://wandb.ai/) (free tier) or MLflow to log all model runs, metrics, hyperparameters
  - Must cover: **Serve best model via FastAPI** — one POST endpoint that takes features, returns prediction. You already know APIs from SDE work — this takes 3-4 hrs max.
  - Write notes like you did for house price prediction — tradeoffs, failures, intuitions
  - Document your EDA process explicitly: what did raw data look like? What quality issues? What did visualizations reveal?
  - **Interview story**: "I compared 4 models on an imbalanced classification problem. XGBoost won at 0.89 AUC-ROC, outperforming logistic regression by 12%. I used SHAP to explain predictions — income-to-debt ratio was 3x more important than credit score. I tracked all experiments in W&B and served the model via FastAPI."
  - **Time**: ~35-40 hrs

### DSA
- [ ] **Focus areas**: Arrays, Strings, HashMaps, Two Pointers
- [ ] **Target**: 25-30 easy problems
- [ ] **Approach**: Pattern-based (NeetCode.io or Sean Prashad's LeetCode Patterns)
- [ ] **Time**: ~25-30 hrs (1.5 hrs × 2 days/week + 1 hr Sunday)

### Month 1 checkpoint (end of April):
- Course 2: 50% done
- 3Blue1Brown Linear Algebra: 8/16 episodes watched
- DSA: 12-15 easy problems solved
- Normal Equation understood

### Standing Out: First blog post
- [ ] **Set up blog** on Hashnode or Medium
- [ ] **Publish first post**: Convert house price prediction notes into a blog post
  - Title idea: "What 4 iterations of linear regression taught me about ML"
  - Not a tutorial — your thinking process, failures, insights
  - Content already exists in your notes — just format and publish
  - **Time**: ~5-6 hrs
- [ ] Share on LinkedIn

### Month 2 checkpoint (end of May):
- Course 2: Complete
- Classification project: In progress or done
- 3Blue1Brown: Both series done
- DSA: 25-30 easy problems, started first mediums
- Blog post 1: Published

---

## Exam Window 1 (June → Mid-July 2026)
### ~6 weeks | Reduced capacity

### Priority: MCA exams

### Maintenance only:
- [ ] DSA: 1 easy or light medium per day, 30 min (don't lose momentum)
- [ ] ML: Review notes from Phase 1. No new topics.
- [ ] If time permits: Finish classification project if not done

### Month 3 checkpoint (end of June):
- MCA exams: in progress / done
- DSA: 10-15 more problems (maintaining)
- Classification project: Complete (even if finished during exam window gaps)

---

## Phase 2: Intermediate ML + Projects (Mid-July → September 2026)
### ~10 weeks | Full capacity

### ML Learning
- [ ] **Andrew Ng Course 3**: Unsupervised Learning, Recommender Systems, RL
  - Clustering (K-means), anomaly detection, collaborative filtering
  - Reinforcement learning introduction
  - **Time**: ~20-25 hrs
- [ ] **Hands-On ML Book (Aurélien Géron)** — selected chapters, not cover-to-cover:
  - Ch 1-2: ML landscape, end-to-end project (skim — you've done this)
  - Ch 3: Classification (reinforces project 2)
  - **Ch 4: Training Models** — gradient descent math, learning curves, regularization math (Ridge/Lasso). This is the most important chapter for interviews.
  - Ch 5: SVMs (concept level)
  - Ch 6-7: Decision Trees, Ensemble Methods (deepens Course 2)
  - Ch 8: Dimensionality Reduction (PCA — connects to project 3)
  - **Time**: ~25-30 hrs

### Math
- [ ] **Probability & Statistics**: StatQuest YouTube channel (Josh Starmer)
  - Bayes theorem, distributions, hypothesis testing, p-values
  - Watch 2-3 videos per week — they're short (10-15 min each)
  - **Time**: ~8-10 hrs

### Projects
- [ ] **Project 3: Unsupervised Learning — Customer Segmentation**
  - Dataset: E-commerce / retail customer data
  - Must cover: K-means, DBSCAN, hierarchical clustering comparison
  - Must cover: PCA for dimensionality reduction & visualization, elbow method, silhouette score
  - Must cover: **Experiment tracking** with W&B/MLflow (carry forward from Project 2)
  - Key question: how do you evaluate clusters without labels?
  - Document EDA explicitly: what did raw data look like? What cleaning was needed? What did distributions reveal before any modeling?
  - **Interview story**: "I segmented customers into groups using 3 different algorithms. Here's why K-means gave cleaner segments, how I chose K, and what PCA revealed about the feature space."
  - **Time**: ~25-30 hrs

### DSA + SQL
- [ ] **Transition to mediums**
- [ ] **Focus areas**: Sliding Window, Binary Search, Sorting, Stacks/Queues, Basic Trees
- [ ] **Target**: 10 easy + 15 medium problems
- [ ] **SQL start**: Replace 1 DSA session every 2 weeks with SQL practice on HackerRank
  - SELECT, JOIN, GROUP BY basics first. Window functions later.
  - By January you'll have 5 months of passive SQL familiarity.
- [ ] **Time**: ~25-30 hrs (DSA + SQL combined)

### Standing Out: Blog + Networking + Research
- [ ] **Blog post 2**: "Why your train/test split is lying to you" (cross-validation journey)
- [ ] **LinkedIn habit**: Comment thoughtfully on 1-2 ML posts per day while commuting. Not spam — real engagement. 10 min/day, compounds over months.
- [ ] **Online ML events**: Join 1-2 online ML meetups/webinars (MLOps Community, DataTalks.Club, ML India Discord). Watch, learn, network. No travel needed.
- [ ] **Target companies list**: Spend 2 hrs researching 15-20 Bangalore companies with ML teams. Categories:
  - ML-first: Flipkart, Swiggy, Amazon, Google, Microsoft (IDC), Walmart Labs
  - ML teams at product companies: Razorpay, CRED, Meesho, PhonePe
  - ML startups: Sarvam AI, Observe.AI, Yellow.ai
  - ML consulting: Fractal Analytics, Tiger Analytics
- [ ] **Time**: ~8-10 hrs

### Month 4 checkpoint (end of July):
- Course 3: 50% done
- Back to full DSA pace
- Blog platform set up

### Month 5 checkpoint (end of August):
- Course 3: Complete
- Géron book selected chapters: In progress
- Customer segmentation project: Started
- DSA: Solving some mediums with hints
- Probability basics: Comfortable with Bayes, distributions

### Month 6 checkpoint (end of September):
- Unsupervised project: Complete with notes
- First blog post: Published
- DSA: 15+ mediums solved across different patterns
- Math: Probability & statistics solid for interview level

---

## Phase 3: Deep Learning (October → Mid-November 2026)
### ~7 weeks | Full capacity | DL-focused (RL project moved to November)

### ML Learning
- [ ] **Deep Learning**: Pick ONE of these paths:
  - **Option A**: Fast.ai "Practical Deep Learning for Coders" (free, top-down, code-first)
  - **Option B**: Andrew Ng Deep Learning Specialization Course 1 (Neural Networks & Deep Learning) — more theory-first
  - Recommendation: Option A if you want to build fast, Option B if you want to understand math deeply
  - **Time**: ~25-30 hrs
- [ ] **Reinforcement Learning — THEORY ONLY in this phase**: David Silver's RL lectures (first 4-5 lectures)
  - Core concepts: MDP, value functions, Q-learning, policy gradient (concept level)
  - RL project comes in November, not here. Just build the theoretical foundation.
  - **Time**: ~15-20 hrs

### Project
- [ ] **Project 4: Deep Learning — Text Classification or Image Classification**
  - **NLP path**: Sentiment analysis — build simple NN from scratch in PyTorch/Keras, then fine-tune a pretrained model (DistilBERT). Compare performance.
  - **CV path**: Image classification on a non-trivial dataset (not MNIST — something like plant disease detection, X-ray classification)
  - Must cover: data preprocessing for DL, training loops, loss curves, overfitting detection, learning rate tuning
  - Must cover: **Experiment tracking** with W&B/MLflow (carry forward from Projects 2 & 3)
  - Document EDA: what does the raw data look like? Class distribution? Data augmentation decisions?
  - **Interview story**: "I built a [text/image] classifier from scratch, hitting X accuracy. Fine-tuning a pretrained model improved it to Y. Here's why transfer learning helped, and the specific tradeoff between training time and performance. All experiments tracked in W&B."
  - **Time**: ~25-30 hrs

### DSA + SQL
- [ ] **Focus areas**: Dynamic Programming (basic), Graphs (BFS/DFS), Linked Lists, Heaps
- [ ] **Target**: 20-25 mediums
- [ ] **SQL**: Continue bi-weekly SQL sessions (JOINs, subqueries, window functions by now)
- [ ] **Time**: ~25-30 hrs

### Standing Out: Blog + GitHub
- [ ] **Blog post 3**: "Classical ML vs Deep Learning — when to use what" (from project experience)
- [ ] **GitHub cleanup**: Each project repo should have clean README with problem statement, approach, results, learnings
- [ ] **LinkedIn**: Continue daily engagement habit
- [ ] **Time**: ~6-8 hrs

### Month 7 checkpoint (end of October):
- DL course: 60%+ done
- NN project: Started
- RL: First 2-3 lectures watched (theory only)
- DSA: Attempting DP and graph problems
- Blog: 2 posts published

### Month 8 checkpoint (mid-November):
- NN project: Complete
- RL theory: Done (ready to start RL project)
- DSA: 35+ mediums total
- Blog: 3 posts published

---

## RL Project + Exam Window 2 + Interview Prep (Mid-November → February 2027)
### ~14 weeks | Split between RL project, MCA, and interview prep

### November (remaining ~2-3 weeks):
- [ ] **Project 5: Reinforcement Learning — Agent for a control problem** (moved here from Phase 3)
  - Environment: OpenAI Gymnasium (CartPole is minimum, LunarLander or Taxi is better)
  - Algorithm: Q-learning → DQN if time permits
  - Must cover: reward design, exploration vs exploitation, convergence visualization
  - This is LIGHTER than other projects — clean implementation, solid understanding, not cutting-edge
  - **Interview story**: "I trained an RL agent to solve [problem]. Here's how I designed the reward function, why epsilon-greedy exploration was needed, and how I knew when the agent had converged."
  - **Time**: ~15-20 hrs
- [ ] Resume first draft written
- [ ] MCA study begins (light)
- [ ] DSA: Reduced to 3-4 problems/week

### December 2026 (MCA exams):
- [ ] MCA exams: Primary focus
- [ ] DSA: 1 problem/day maintenance
- [ ] ML: Review and revise only — no new topics
  - Re-read all your project notes
  - Practice explaining each project out loud (elevator pitch → 5-min deep dive)

### January 2027 (Interview prep ramp-up):
- [ ] **ML Theory Revision**: Go through common ML interview questions
  - Bias-variance tradeoff, overfitting/underfitting
  - L1 vs L2 regularization (and WHY, not just what)
  - How gradient descent works, learning rate effects
  - Decision tree splitting criteria (Gini, entropy)
  - Ensemble methods (bagging vs boosting)
  - Evaluation metrics (when to use what)
  - Data leakage, train/test contamination
  - Model interpretability (SHAP — revisit your Project 2 work)
  - Resource: [ML Interviews GitHub repo](https://github.com/alirezadir/Machine-Learning-Interviews)
  - **Time**: ~20-25 hrs
- [ ] **ML System Design** (10-12 hrs):
  - Study how to design end-to-end ML systems (not just train models)
  - Common questions: "Design a recommendation system", "Design a fraud detection pipeline"
  - Resource: [Designing Machine Learning Systems — Chip Huyen](https://www.oreilly.com/library/view/designing-machine-learning/9781098107956/) — read Chapters 1-4, 6, 9
  - Resource: [ML System Design GitHub](https://github.com/chiphuyen/machine-learning-systems-design)
  - Practice: Structure answers for 3-4 common ML system design problems
- [ ] **SQL Polish**: By now you have 5 months of SQL practice from Phase 2-3. Spend a few hours on harder problems:
  - Window functions, CTEs, complex JOINs
  - Practice on StrataScratch (ML-focused SQL questions)
  - **Time**: ~5-8 hrs
- [ ] **Resume finalization**
  - Highlight SDE production experience (this is your edge)
  - Each ML project with **quantified results**: not "Built a churn model" but "Built a churn prediction model using XGBoost achieving 0.89 AUC-ROC on 50K records, outperforming logistic regression baseline by 12%"
  - Blog link and GitHub link visible at the top
  - **Time**: ~5 hrs
- [ ] **Mock interview with mentor**: Loop him in. "I'm almost ready. Can you do a mock round?"

### February 2027 (Final interview prep):
- [ ] Fill gaps identified from mock interview
- [ ] Practice coding ML algorithms from scratch (logistic regression, decision tree, k-means)
- [ ] DSA: Focus on weak patterns, 1 problem/day
- [ ] **Blog post 4**: "Lessons from building 5 ML projects in 10 months" (retrospective)
- [ ] Polish all GitHub repos — final cleanup

### Month 9 checkpoint (end of December):
- MCA exams: Done
- RL project: Complete
- All 5 projects done
- Blog: 3+ posts published

### Month 10 checkpoint (end of January):
- ML theory revision: Complete
- ML system design: Practiced 3-4 problems
- SQL: Comfortable with medium-hard queries
- Resume: Final version ready
- Mentor: Mock interview done

### Month 11 checkpoint (end of February):
- GitHub: All repos polished
- Blog: 4 posts published
- Interview gaps: Filled
- Ready to apply

---

## Phase 4: Applications + Interviews (March → May 2027)
### ~12 weeks | Full capacity

- [ ] **Activate mentor referrals**: Tell mentor you're ready. Send resume to target companies.
- [ ] **Apply broadly**: Applied ML Engineer, ML Engineer, ML SDE roles
- [ ] **Continue DSA**: 1 problem/day — focus on weak patterns
- [ ] **After each interview**: Write down what was asked, what you answered well, what you struggled with. Fill gaps immediately.
- [ ] **If you get rejections**: Don't panic. Analyze the feedback. Adjust. Apply to more.
- [ ] **Fallback**: If pure ML roles aren't biting, consider ML-adjacent SDE roles at ML-focused companies. Get in the building, then move internally.

### Month 12 checkpoint (end of March):
- Applications sent via referrals
- Interviews happening
- Gaps identified and being filled

### Month 13 checkpoint (end of April / May):
- Multiple interviews completed
- Offer(s) in hand or strong pipeline
- If not: reassess strategy with mentor, expand search
- MCA results should be out by now — no blockers for offer letters

---

## Project Roadmap Summary

| # | Area | Project | Key Interview Topics | Production ML | Status |
|---|------|---------|---------------------|---------------|--------|
| 1 | Classical ML (Regression) | House Price Prediction | Feature eng, regularization, cross-validation, limits of linear models | — | DONE |
| 2 | Classical ML (Classification) | Loan Default / Churn Prediction | Class imbalance, precision/recall, model comparison (LR → XGBoost), threshold tuning, **SHAP interpretability** | W&B tracking, **FastAPI endpoint** | Phase 1 |
| 3 | Unsupervised Learning | Customer Segmentation | K-means vs DBSCAN, PCA, evaluating clusters without labels, elbow method | W&B tracking | Phase 2 |
| 4 | Deep Learning | Text or Image Classification | NN from scratch vs pretrained, transfer learning tradeoffs, training dynamics | W&B tracking | Phase 3 |
| 5 | Reinforcement Learning | Control Agent (Gymnasium) | Reward design, exploration vs exploitation, Q-learning, convergence | — | Nov 2026 |

**Every project must pass the 3-level-deep interview test:**
1. "What did you build?" (surface)
2. "Why did you make this specific choice?" (reasoning)
3. "What failed, what would you do differently?" (depth)

---

## Standing Out Checklist

### Resume (what makes recruiters call)
- [ ] SDE experience bullet: "2 years shipping production [frontend/fullstack] features at [company]"
- [ ] Each ML project with **quantified results**:
  - Bad: "Built a churn prediction model using XGBoost"
  - Good: "Built a churn prediction model using XGBoost achieving 0.89 AUC-ROC on 50K customer records, outperforming logistic regression baseline by 12%. Used SHAP for interpretability. Served via FastAPI."
- [ ] Blog and GitHub links visible at the top
- [ ] MCA (IGNOU, expected 2027) — list it, don't hide it. Your projects prove your skill.
- [ ] Tailored summary: "SDE with 2 years production experience transitioning to ML Engineering. Strong in classical ML, model interpretability, experiment tracking, and end-to-end model development."

### GitHub (proof of work)
- [ ] Each project in its own clean repo
- [ ] README with: Problem → Approach → Results → Learnings
- [ ] Notes directory (like your house price prediction) — shows thinking depth
- [ ] No Jupyter notebooks with messy outputs — clean cells, clear labels

### Blog (thought leadership)
- [ ] Post 1 (May — Phase 1): "What 4 iterations of linear regression taught me about ML" (from house price notes)
- [ ] Post 2 (Sep — Phase 2): "Why your train/test split is lying to you" (cross-validation journey)
- [ ] Post 3 (Nov — Phase 3): "Classical ML vs Deep Learning — when to use what" (from project experience)
- [ ] Post 4 (Feb — pre-applications): "Lessons from building 5 ML projects in 10 months" (retrospective)
- [ ] Platform: Hashnode or Medium
- [ ] Share every post on LinkedIn — tag relevant ML communities

### Networking (online only — not in Bangalore yet)
- [ ] **LinkedIn**: Comment thoughtfully on 1-2 ML posts daily. 10 min/day. Compounds over months.
- [ ] **Online communities**: Join MLOps Community Slack, DataTalks.Club, ML India Discord
- [ ] **Online events**: Attend 2-3 webinars/virtual meetups during Phase 2-3
- [ ] **Don't**: Spend money on travel for in-person meetups. Wait until you're in Bangalore.

### Interview (what makes interviewers say yes)
- [ ] Can whiteboard/explain any ML algorithm you've used (not memorized — understood)
- [ ] Can walk through any project for 10+ minutes with follow-ups
- [ ] Can code a clean solution to Leetcode medium in 25-30 min
- [ ] Can answer "why not X?" for every choice you made
- [ ] Can discuss production concerns: "How would you serve this model? How would you monitor drift?" (you know APIs and engineering — lean on your SDE background)
- [ ] Can answer basic ML system design: "Design a fraud detection system" (structure: data → features → model → serving → monitoring)
- [ ] Can explain model predictions using SHAP — "why did the model predict this?"

---

## Weekly Structure Template

### Normal Weeks
```
Monday    [1.5-2 hrs]  ML: Course/theory/math
Tuesday   [1.5-2 hrs]  DSA: Pattern practice
Wednesday [1.5-2 hrs]  ML: Course/theory/math
Thursday  [1.5-2 hrs]  DSA: Pattern practice
Friday    [1.5-2 hrs]  ML: Course/theory/math
Saturday  [5 hrs]      ML: Project work (primary focus of the day)
Sunday    [5 hrs]      ML Project (2.5 hrs) + DSA (1 hr) + Spaced Review (30 min) + Blog (1 hr)
```

### MCA Exam Weeks
```
Monday-Friday  [all available time]  MCA study
Saturday-Sunday  [1 hr total]  DSA: 1 easy problem per day (maintain muscle memory)
```

---

## Spaced Repetition System — How to Not Forget

### The Problem
You'll learn cross-validation in April. By October, if you haven't touched it, the details will be fuzzy. You'll feel like you're "starting over." That's not a learning failure — it's a memory failure. Fix the memory system, not the learning.

### The Rule: Sunday Review (30 min, every week)

Every Sunday, before your blog/project time, spend 30 minutes reviewing OLD material. Not current material — you're already studying that. Old material that's drifting away.

### What to Review Each Sunday

**Rotate through your completed project notes on a cycle:**

| Week | What to review |
|------|---------------|
| Week 1 of month | Re-read notes from Project 1 (House Price Prediction) |
| Week 2 of month | Re-read notes from Project 2 (Classification) — once it exists |
| Week 3 of month | Re-read notes from oldest completed project + re-read any math notes |
| Week 4 of month | Pick your WEAKEST topic. The one you'd be least confident explaining in an interview right now. Review that. |

As you complete more projects, extend the rotation. By Month 8, you'll have 4-5 sets of notes rotating through your Sundays.

### How to Review (not just re-read)

Don't passively skim your notes. Do this instead:

1. **Close the notes. Ask yourself**: "What were the 3 most important things I learned in this project?" Write them from memory.
2. **Open the notes. Compare.** What did you miss? What did you remember wrong?
3. **If something feels completely blank**: Spend 10 extra minutes on just that concept. Re-derive it, re-explain it in your own words.
4. **Update your notes** if you now understand something better than when you wrote them.

### Reinforcement Through Projects (built into the plan)

Each new project deliberately reuses skills from previous ones:

```
Project 1 (House Prices)  → cross-validation, feature engineering, regularization
    ↓ reused in
Project 2 (Classification) → cross-validation, feature engineering + adds class imbalance, new metrics
    ↓ reused in
Project 3 (Unsupervised)  → feature engineering, PCA + adds clustering, evaluation without labels
    ↓ reused in
Project 4 (Deep Learning)  → train/test methodology, evaluation metrics + adds NN, backprop, transfer learning
    ↓ reused in
Project 5 (RL)            → training loops, loss/reward tracking + adds MDP, Q-learning
```

This is intentional. Every project reinforces 60-70% old skills + adds 30-40% new skills. You're never fully in "new territory" — you're always partially on familiar ground.

### Library Fluency (pandas, numpy, sklearn, pytorch)

You won't learn libraries from a course. You'll learn them by using them 5 projects in a row. But speed it up with this rule:

**After you Google a syntax and it works — don't copy-paste. Delete it and type it again from memory.** Do this 2-3 times for new patterns. By the 3rd project, you'll type `train_df.groupby("city")["price"].mean()` without thinking.

No separate "learn pandas" course needed. The projects ARE the course.

---



### ML Courses (follow in order)
1. ~~Andrew Ng ML Specialization — Course 1~~ (DONE)
2. Andrew Ng ML Specialization — [Course 2: Advanced Learning Algorithms](https://www.coursera.org/specializations/machine-learning-introduction)
3. Andrew Ng ML Specialization — [Course 3: Unsupervised Learning](https://www.coursera.org/specializations/machine-learning-introduction)
4. [Fast.ai Practical Deep Learning](https://course.fast.ai/) OR Andrew Ng DL Specialization Course 1
5. David Silver RL Lectures (YouTube, first 4-5 lectures)

### Math (watch alongside ML courses)
1. [3Blue1Brown: Essence of Linear Algebra](https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab) — 16 episodes, best visual intuition
2. [3Blue1Brown: Essence of Calculus](https://www.youtube.com/playlist?list=PLZHQObOWTQDMsr9K-rj53DwVRMYO3t5Yr)
3. [StatQuest (Josh Starmer)](https://www.youtube.com/c/joshstarmer) — Probability, statistics, ML explained simply
4. [DeepLearning.AI Math for ML Specialization](https://www.coursera.org/specializations/mathematics-for-machine-learning-and-data-science) — structured course if you want more

### Books (reference, not cover-to-cover)
1. **Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow** (Aurélien Géron) — THE practical ML book. Read selected chapters in Phase 2.
2. **An Introduction to Statistical Learning (ISLR)** — free PDF. Use as reference for theory.
3. **Designing Machine Learning Systems** (Chip Huyen) — Read Ch 1-4, 6, 9 during interview prep (January).
4. **Interpretable Machine Learning** (Christoph Molnar) — [free online](https://christophm.github.io/interpretable-ml-book/). Reference for SHAP/LIME concepts.

### Production ML Tools (learn by using in projects)
1. [Weights & Biases](https://wandb.ai/) — Free tier. Experiment tracking. Use from Project 2 onwards.
2. [FastAPI](https://fastapi.tiangolo.com/) — Model serving. Build one endpoint for Project 2.
3. [SHAP](https://shap.readthedocs.io/) — Model interpretability. Use in Project 2.

### DSA
1. [NeetCode.io](https://neetcode.io/) — Pattern-based problem grouping
2. [Sean Prashad's LeetCode Patterns](https://github.com/seanprashad/leetcode-patterns) — Problems grouped by pattern
3. [LeetCode](https://leetcode.com/) — Practice platform

### Interview Prep
1. [ML Interviews Guide (GitHub)](https://github.com/alirezadir/Machine-Learning-Interviews) — Comprehensive ML interview resource
2. [Top ML Interview Questions (DataCamp)](https://www.datacamp.com/blog/top-machine-learning-interview-questions)
3. SQL practice: HackerRank SQL track or StrataScratch

### Blog
1. [Hashnode](https://hashnode.com/) — Free, developer-focused, good SEO
2. [Medium](https://medium.com/) — Larger audience, paywall can limit reach

---

## Monthly Checkpoint Summary

| Month | Date | ML Progress | DSA + SQL | Standing Out | Other |
|-------|------|-------------|-----------|--------------|-------|
| 1 | Apr 2026 | Course 2: 50%, Linear algebra started | 12-15 easy | — | — |
| 2 | May 2026 | Course 2: Done, Classification project started | 25-30 easy, first mediums | Blog post 1, Blog setup | — |
| 3 | Jun 2026 | Maintenance only | 10-15 (maintaining) | — | MCA exams |
| 4 | Jul 2026 | Course 3: 50% | Back to full pace | — | MCA done |
| 5 | Aug 2026 | Course 3: Done, Géron Ch 1-5 | Medium patterns + SQL started | Target companies researched | — |
| 6 | Sep 2026 | Unsupervised project done, Géron Ch 6-8 | 15+ mediums, SQL basics solid | Blog post 2, LinkedIn active | — |
| 7 | Oct 2026 | DL course 60%, NN project started | DP & graphs, SQL continues | Blog post 3 | — |
| 8 | Nov 2026 | NN project done, RL project started | 35+ mediums total | Resume first draft | MCA prep starts |
| 9 | Dec 2026 | RL project done, revision | Maintenance | GitHub polished | MCA exams |
| 10 | Jan 2027 | ML theory + system design, SQL polish | Maintenance | Resume final, Mentor mock | Interview prep |
| 11 | Feb 2027 | Final interview prep, fill gaps | Weak patterns | Blog post 4, GitHub final | Ready to apply |
| 12 | Mar 2027 | Applications via referrals | Interview-ready | Applications sent | Interviewing |
| 13 | Apr-May 2027 | Fill gaps from interviews | — | — | Offers |

---

## If You're Falling Behind

1. **1-2 weeks behind**: Increase weekend hours temporarily. Cut blog writing, not DSA or ML.
2. **1 month behind**: Reduce project scope (simpler dataset, fewer model comparisons). Don't skip projects entirely.
3. **2+ months behind**: Reassess timeline. Push target to July 2027. Better to be ready late than to interview unprepared.
4. **Burnout signals**: Dreading study sessions, retaining nothing, zero motivation for >1 week. Take 3-4 days completely off. Then restart at 50% pace for a week. Don't power through burnout — it makes everything worse.

## When to Loop In Your Mentor

- **Month 6-7**: Share your GitHub and blog. Ask: "Am I on the right track for the roles you have in mind?"
- **Month 9-10**: Ask for a mock interview or mock project review.
- **Month 10-11**: "I'm ready. Here's my resume, here's my GitHub. Can you start referring me?"
- **After any interview**: If you got feedback, share it with mentor for calibration.

---

*Plan created: April 12, 2026*
*Plan v2 revised: April 12, 2026 (after external review)*
*Changes in v2: +1 month timeline, +SHAP/interpretability, +experiment tracking (W&B), +FastAPI serving, +ML system design, +SQL moved earlier, +blog post 1 moved earlier, Phase 3 restructured (RL project → November), +networking strategy, +resume quantification, +Géron Ch 4, +target companies research*
*Next review: End of April 2026 (Month 1 checkpoint)*

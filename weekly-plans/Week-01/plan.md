# Week 1: April 13 (Mon) → April 19 (Sun)
## Phase 1 | First week — build momentum, don't sprint

---

## Monday — ML Theory (1.5-2 hrs)
**Topic: Normal Equation (finishing house price prediction Task 3)**

| Order | What | Time |
|-------|------|------|
| 1 | ~~Read the [DataCamp Normal Equation tutorial](https://www.datacamp.com/tutorial/tutorial-normal-equation-for-linear-regression). Don't rush. Take notes.~~ | 45 min | DONE |
| 2 | ~~After reading, close the tab. Write in your own words: what is the Normal Equation doing? How does it find the best weights without iterating?~~ | 15 min | DONE |
| 3 | ~~Watch [3Blue1Brown Essence of Linear Algebra — Ep 1: Vectors](https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab)~~ | 15 min | DONE |
| 4 | ~~Watch Ep 2: Linear combinations, span, and basis vectors~~ | 15 min | DONE |
| 5 | ~~Reflect: how do the vectors in these videos relate to the columns of your feature matrix X? Write 2-3 sentences in your notes.~~ | 10 min | DONE |

**Done for the day. Close laptop.**

---

## Tuesday — DSA (1.5-2 hrs)
**Topic: Arrays — Easy level**

| Order | What | Time |
|-------|------|------|
| 1 | ~~Go to [NeetCode.io](https://neetcode.io/). Bookmark it. Look at the "Arrays & Hashing" section.~~ | 10 min | DONE |
| 2 | ~~**Problem 1**: [Two Sum](https://leetcode.com/problems/two-sum/) — Try for 20 min on your own. If stuck, look at the NeetCode video explanation, then code it yourself.~~ | 30-40 min | DONE |
| 3 | ~~**Problem 2**: [Contains Duplicate](https://leetcode.com/problems/contains-duplicate/) — Same approach: try first, then check if stuck.~~ | 20-30 min | DONE |
| 4 | ~~**Problem 3**: [Valid Anagram](https://leetcode.com/problems/valid-anagram/)~~ | 20-30 min | DONE |
| 5 | ~~After all 3: for each problem, write one line about the pattern used (e.g., "hashmap for O(1) lookup").~~ | 10 min | DONE |

**Target: 3 easy problems solved. Quality > speed.** ✅

---

## Wednesday — ML Theory (1.5-2 hrs)
**Topic: Start Andrew Ng Course 2 — Week 1 (Neural Networks intro)**

| Order | What | Time |
|-------|------|------|
| 1 | Open [Course 2: Advanced Learning Algorithms](https://www.coursera.org/specializations/machine-learning-introduction) on Coursera. Start Week 1. | 5 min |
| 2 | Watch the first 4-5 videos of Week 1 (Neurons and the brain, Neural network model, etc.). Take notes in a new notes file. | 60-70 min |
| 3 | Watch 3Blue1Brown Ep 3: Linear transformations and matrices | 15 min |
| 4 | Pause and think: Andrew Ng talks about weights in neural networks. 3B1B talks about matrices as transformations. Can you see how multiplying inputs by weights IS a linear transformation? Write a note. | 10 min |

**Don't try to finish all of Week 1 today. Just the first chunk.**

---

## Thursday — DSA (1.5-2 hrs)
**Topic: Arrays + HashMaps — Easy level**

| Order | What | Time |
|-------|------|------|
| 1 | Before starting: re-read your one-line pattern notes from Tuesday. Can you recall the approach for Two Sum without looking at code? | 5 min |
| 2 | **Problem 4**: [Group Anagrams](https://leetcode.com/problems/group-anagrams/) — This is medium-tagged but doable. Try for 25 min. Check NeetCode if stuck. | 30-40 min |
| 3 | **Problem 5**: [Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/) | 25-35 min |
| 4 | **Problem 6**: [Maximum Subarray](https://leetcode.com/problems/maximum-subarray/) — Kadane's algorithm. Classic pattern. | 25-35 min |
| 5 | Write one-line pattern notes for each. | 5 min |

**Target: 3 more problems. Running total: 6 problems this week.**

---

## Friday — ML Theory (1.5-2 hrs)
**Topic: Continue Course 2 Week 1 + Linear Algebra**

| Order | What | Time |
|-------|------|------|
| 1 | Continue Andrew Ng Course 2 Week 1 — next 4-5 videos (TensorFlow implementation, forward propagation, etc.) | 60-70 min |
| 2 | Watch 3Blue1Brown Ep 4: Matrix multiplication as composition | 15 min |
| 3 | Think about: in a neural network, you multiply inputs by weight matrix W1, then apply activation, then multiply by W2. Each multiplication is a transformation. What does "stacking layers" mean geometrically? Write a note. | 15 min |

**Course 2 Week 1 should be ~70-80% done by end of Friday.**

---

## Saturday — ML Deep Work (5 hrs)
**Topic: Finish Course 2 Week 1 + House price prediction loose ends**

### Morning block (2.5 hrs)
| Order | What | Time |
|-------|------|------|
| 1 | Finish remaining Course 2 Week 1 videos | 30-40 min |
| 2 | Complete the Week 1 practice lab / programming assignment | 60-70 min |
| 3 | Take a 10 min break. Walk around. | 10 min |
| 4 | Re-read the [Eli Bendersky Normal Equation derivation](https://eli.thegreenplace.net/2014/derivation-of-the-normal-equation-for-linear-regression/) — the deeper resource. You've read the beginner one on Monday, now go one level deeper. Don't worry if the full derivation is fuzzy — focus on the big picture. | 30-40 min |

### Afternoon block (2.5 hrs)
| Order | What | Time |
|-------|------|------|
| 5 | ~~**Task 4**: Ridge regularization reasoning. Ran experiment notebook comparing α=0,1,10,100. Understood: αI increases diagonal → bigger denominator in inverse → smaller weights. Connected to bias-variance tradeoff.~~ | 40-50 min | DONE (pulled forward from Saturday) |
| 6 | ~~**Fix the .copy() bug** in K-fold CV notebook. Added `.copy()` to both `test_df` and `train_df`. Verified outputs unchanged — safety fix, not correctness fix.~~ | 20-30 min | DONE (pulled forward from Saturday) |
| 7 | Watch 3Blue1Brown Ep 5: The determinant (if time permits) | 15 min |

---

## Sunday — Mixed Day (4-4.5 hrs)
**Note: First week, no blog or spaced review yet. Lighter Sunday.**

### ML block (2.5 hrs)
| Order | What | Time |
|-------|------|------|
| 1 | Start Andrew Ng Course 2, Week 2 (Neural network training — backpropagation). Watch first 3-4 videos. | 50-60 min |
| 2 | Watch 3Blue1Brown's [Neural Networks video (Ch 1)](https://www.youtube.com/watch?v=aircAruvnKk) — this is separate from the linear algebra series. It's a 20-min visual explanation of what neural networks actually do. Pairs perfectly with Course 2. | 20 min |
| 3 | Open your house price prediction project. Look at your data, your pipeline, your results. Ask yourself: "Could a neural network do better than Ridge on this data? Why or why not?" Write 3-4 sentences. This is your first "think before you compute" moment for neural networks. | 20 min |
| 4 | Browse Kaggle for classification datasets. Look at 3-4 options for Project 2 (loan default, customer churn, credit card fraud). Don't start the project — just bookmark 2 datasets that interest you. Read their descriptions. Think about what features they have. | 30-40 min |

### DSA block (1 hr)
| Order | What | Time |
|-------|------|------|
| 5 | **Problem 7**: [Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/) — medium. Try 20 min, check NeetCode if stuck. | 25-30 min |
| 6 | **Problem 8**: [Merge Sorted Array](https://leetcode.com/problems/merge-sorted-array/) — easy, two pointers pattern. | 20-25 min |
| 7 | Review all pattern notes from the week. Can you name the pattern for each of the 8 problems without looking at the code? | 5-10 min |

### Buffer (1 hr)
Use this for whatever needs catching up. If everything's done, rest. Don't force it.

---

## Week 1 Targets

| Category | Target | How to verify |
|----------|--------|---------------|
| Course 2 | Week 1 complete, Week 2 started | Assignment submitted, first 3-4 videos of Week 2 watched |
| 3Blue1Brown | Episodes 1-5 of Linear Algebra + 1 Neural Networks video | Notes written connecting videos to ML concepts |
| Normal Equation | ~~Task 3 done — can explain in own words~~ | ~~Written explanation in notes~~ | DONE Day 1 |
| Ridge reasoning | ~~Task 4 done — can reason about αI~~ | ~~Written reasoning in notes + experiment notebook~~ | DONE Day 1 |
| .copy() bug | ~~Fixed and verified~~ | ~~Notebook re-runs with same results~~ | DONE Day 1 |
| DSA | 8 problems solved (6 easy, 2 medium) | Pattern notes for each problem |
| Dataset scouting | 2 classification datasets bookmarked for Project 2 | Links saved |

---

## If you're struggling

- **Can't finish a day's plan**: Do items 1 and 2 only. Skip the rest. Partial progress > zero progress.
- **A DSA problem takes >40 min**: Stop. Watch the NeetCode solution. Understand it. Type it out yourself (don't paste). Move on. You'll revisit patterns later.
- **Course 2 feels too fast**: Pause, rewind, re-watch. It's not a race. Understanding 3 videos deeply > skimming 6.
- **Burnout creeping back**: Take the day off. One rest day won't derail a 12-month plan. Forcing yourself through burnout will.

---

*When this week is done, come back and tell me what you completed, what you struggled with, and what you skipped. I'll adjust Week 2 based on that.*

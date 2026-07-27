# DSA Interview Ramp-up Plan (May 4 → September 1, 2026)

Captured May 3, 2026. Updated May 3, 2026 (added Sorting & Intervals as Week 4).
Replaces the daily drill curriculum in `DSA-patterns.md` (which was foundation-building, 15 min/day). This is the interview ramp-up plan: 30 min/day, aggressive new pattern coverage, ~17 weeks to interview-ready medium level.

## Why this exists

Mentor wants me ready for interviews in the 2-3 month window (ideally July-August 2026, possibly later given MCA exams). The original DSA daily drill (15 min, foundation patterns only) is too slow for that. This plan ramps it up.

## Status entering this plan

- ~18 problems solved (4 weeks of work).
- Patterns covered (mostly easy): Arrays & Hashing, Two Pointers (3 sub-types), Sliding Window basics, Stack basics, Prefix sums, basic strings.
- Patterns NOT covered: Sorting & Intervals, Binary Search, Linked Lists, Trees, Heaps, Graphs, Backtracking, DP.

## Time budget

- **30 min/day, every day.** No rest days. Drill is non-negotiable.
- Weekend bonus: 1 extra problem on Saturday or Sunday if I have energy. Optional.
- Total: ~3.5-5 hrs/week DSA.

## Three phases

### Phase A — Aggressive new pattern intro (May 4 → May 31, 4 weeks)

Pre-MCA. Push hard. Introduce 4 new patterns. Mix new pattern problems with consolidation of existing patterns.

### Phase B — Maintenance (June 1 → July 14, 6 weeks)

MCA primary (exams June 27). DSA drops to maintenance mode: 30 min/day, 1 easy problem/day from any covered pattern, NO new patterns. Goal: don't lose momentum, build speed on covered patterns.

### Phase C — Aggressive ramp + interview prep (July 15 → August 31, 6-7 weeks)

Post-MCA. Push hard again. Cover remaining patterns. Push into mediums consistently. End with mock interview prep.

After September 1: applications + interviews.

## Pattern priority list

| Tier | Patterns | Reason |
|---|---|---|
| 1 (must) | **Sorting & Intervals**, Binary Search, Linked Lists, Trees BFS/DFS, Heap, DP 1D | Asked in nearly every interview. Sorting is the most common opening move ("sort first, then..."). |
| 1 (must, already covered) | Arrays/Hashing, Two Pointers, Sliding Window, Stack | Need mediums, not just easies |
| 2 (should) | Graph BFS/DFS, Backtracking, DP 2D | Common in mid-tier rounds |
| 3 (nice) | Tries, Bit manipulation, Math | Edge of medium territory |

## Phase A — Week-by-week plan (May 4 → May 31)

### Week 4 (May 4-10) — Sorting & Intervals

**Why first**: sorting is the most-used opening move in coding interviews. "Sort first, then..." comes up in dozens of medium problems. Plus interval problems (Meeting Rooms, Merge Intervals) are interview classics on their own. Getting comfortable here pays off across every later pattern (Binary Search, Heap, etc., all relate to sorted data).

| Day | Pattern | Problem | LC# | Difficulty |
|---|---|---|---|---|
| Mon May 4 | Sorting | Sort Colors (Dutch Flag) | #75 | Medium |
| Tue May 5 | Intervals | Merge Intervals | #56 | Medium |
| Wed May 6 | Intervals | Insert Interval | #57 | Medium |
| Thu May 7 | Intervals | Non-overlapping Intervals | #435 | Medium |
| Fri May 8 | Intervals | Meeting Rooms II | #253 | Medium |
| Sat May 9 | (project day, skip drill) | — | — | — |
| Sun May 10 | Cyclic Sort | Find All Numbers Disappeared in an Array | #448 | Easy |

**Pattern note for Intervals**: sort by start time, then sweep through one pass. The trick is what to do when intervals overlap (merge them, count them, schedule another room, etc.). Almost every interval problem starts with "sort by start time."

**Pattern note for Cyclic Sort**: when the array contains numbers in a known range (e.g., 1..n), put each number at its correct index. Used for "find missing/duplicate in 1..n" problems. Constant extra space.

**Pattern note for Sort Colors**: Dutch National Flag — three pointers to partition an array into three sections in one pass. The cleanest example of "in-place sorting with partitioning."

### Week 5 (May 11-17) — Sliding Window mediums + Binary Search intro

**New pattern this week**: Binary Search.

| Day | Pattern | Problem | LC# | Difficulty |
|---|---|---|---|---|
| Mon May 11 | Binary Search (intro) | Binary Search | #704 | Easy |
| Tue May 12 | Two Pointers | 3Sum | #15 | Medium |
| Wed May 13 | Sliding Window | Longest Substring Without Repeating Characters | #3 | Medium |
| Thu May 14 | Binary Search | First Bad Version | #278 | Easy |
| Fri May 15 | Binary Search | Search Insert Position | #35 | Easy |
| Sat May 16 | (project day, skip drill) | — | — | — |
| Sun May 17 | Pick weakest pattern | — | — | — |

**Pattern note for Binary Search**: when the array is sorted (or you can binary search on the answer), you can cut the search space in half each iteration → O(log n). Connects directly to last week's Sorting work — sorted data unlocks log-time search.

### Week 6 (May 18-24) — Binary Search mediums + Linked Lists intro

**New pattern this week**: Linked Lists.

| Day | Pattern | Problem | LC# | Difficulty |
|---|---|---|---|---|
| Mon May 18 | Binary Search | Find Min in Rotated Sorted Array | #153 | Medium |
| Tue May 19 | Binary Search | Search in Rotated Sorted Array | #33 | Medium |
| Wed May 20 | Linked Lists (intro) | Reverse Linked List | #206 | Easy |
| Thu May 21 | Linked Lists | Merge Two Sorted Lists | #21 | Easy |
| Fri May 22 | Linked Lists | Linked List Cycle | #141 | Easy |
| Sat May 23 | (project day, skip drill) | — | — | — |
| Sun May 24 | Pick weakest pattern | — | — | — |

**Pattern note for Linked Lists**: classic tricks — slow/fast pointers (cycle detection), dummy head node (simplifies edge cases), reverse-in-place. "Merge Two Sorted Lists" connects to last week's Intervals merge intuition.

### Week 7 (May 25-31) — Linked Lists mediums + Trees BFS/DFS intro

**New pattern this week**: Trees (BFS + DFS).

| Day | Pattern | Problem | LC# | Difficulty |
|---|---|---|---|---|
| Mon May 25 | Linked Lists | Remove Nth Node From End of List | #19 | Medium |
| Tue May 26 | Linked Lists | Reorder List | #143 | Medium |
| Wed May 27 | Trees (intro) | Maximum Depth of Binary Tree | #104 | Easy |
| Thu May 28 | Trees | Invert Binary Tree | #226 | Easy |
| Fri May 29 | Trees BFS | Binary Tree Level Order Traversal | #102 | Medium |
| Sat May 30 | (project day, skip drill) | — | — | — |
| Sun May 31 | Pick weakest pattern | — | — | — |

**Pattern note for Trees**: recursion is your friend. BFS uses a queue (level-by-level). DFS uses recursion or a stack (depth-first). Most tree problems = "recurse, return something useful from each subtree."

## Phase B — Maintenance (June 1 → July 14)

### Rules during MCA prep

- 30 min/day, 1 problem/day. Easy problems only. Pick from any covered pattern.
- NO new patterns. Don't try to learn Heap if you haven't already by May 31.
- Goal: build SPEED on covered patterns. Each easy problem should be solving < 15 min by end of June.
- During exam window (June 27 - July 14): drop to 1 problem every 2 days. Easy only.

### Suggested rotation during June (each week)

| Day | Pattern |
|---|---|
| Mon | Arrays / Hashing |
| Tue | Two Pointers |
| Wed | Sliding Window |
| Thu | Binary Search |
| Fri | Linked Lists OR Sorting/Intervals |
| Sat | Searching/sorting/intervals |
| Sun | Trees |

**Suggested maintenance problems** (pick any easy from this list, solve cold):

- Sorting/Intervals carry-over: Meeting Rooms (#252, easy version), Minimum Number of Arrows to Burst Balloons (#452, medium but doable).
- Stack mediums (carried over from Phase A): Daily Temperatures (#739), Evaluate Reverse Polish Notation (#150).
- Sliding Window: Maximum Average Subarray I (#643, already done — re-solve if rusty).
- Trees easies: Same Tree (#100), Path Sum (#112), Diameter of Binary Tree (#543).
- Binary Search easies: Sqrt(x) (#69), Valid Perfect Square (#367).

Pick any easy problem you haven't solved before, or a medium you found tough — re-solve it cold to build speed.

## Phase C — Aggressive ramp (July 15 → August 31)

### Week 14 (July 15-21) — Trees mediums + Heap intro

**New pattern**: Heap (priority queue).

| Day | Pattern | Problem | LC# | Difficulty |
|---|---|---|---|---|
| Mon | Trees | Validate Binary Search Tree | #98 | Medium |
| Tue | Trees | Lowest Common Ancestor of BST | #235 | Medium |
| Wed | Heap (intro) | Kth Largest Element in Stream | #703 | Easy |
| Thu | Heap | Last Stone Weight | #1046 | Easy |
| Fri | Heap | Kth Largest Element in Array | #215 | Medium |
| Sat | (project day) | — | — | — |
| Sun | Weakest | — | — | — |

**Sorting connection note**: #215 (Kth largest) has TWO classic solutions — heap (this week) and Quickselect (sorting-based, partition like in Sort Colors). After solving with heap, try the Quickselect version. Both are standard interview answers.

### Week 15 (July 22-28) — Heap mediums + Graph BFS intro

**New pattern**: Graphs (BFS).

| Day | Pattern | Problem | LC# | Difficulty |
|---|---|---|---|---|
| Mon | Heap | Top K Frequent Elements | #347 | Medium |
| Tue | Heap | Find Median from Data Stream | #295 | Hard / try, fallback to medium |
| Wed | Graphs (BFS intro) | Number of Islands | #200 | Medium |
| Thu | Graphs (BFS) | Rotting Oranges | #994 | Medium |
| Fri | Graphs (DFS) | Clone Graph | #133 | Medium |
| Sat | (project day) | — | — | — |
| Sun | Weakest | — | — | — |

### Week 16 (July 29-Aug 4) — Graphs mediums + Backtracking intro

**New pattern**: Backtracking.

| Day | Pattern | Problem | LC# | Difficulty |
|---|---|---|---|---|
| Mon | Graphs | Pacific Atlantic Water Flow | #417 | Medium |
| Tue | Graphs | Course Schedule | #207 | Medium |
| Wed | Backtracking (intro) | Subsets | #78 | Medium |
| Thu | Backtracking | Permutations | #46 | Medium |
| Fri | Backtracking | Combinations | #77 | Medium |
| Sat | (project day) | — | — | — |
| Sun | Weakest | — | — | — |

**Pattern note for Backtracking**: "try a choice, recurse, undo the choice." Used for combinatorial problems — generate all subsets, all permutations, etc.

### Week 17 (Aug 5-11) — DP 1D intro

**New pattern**: Dynamic Programming (1D).

| Day | Pattern | Problem | LC# | Difficulty |
|---|---|---|---|---|
| Mon | DP (intro) | Climbing Stairs | #70 | Easy |
| Tue | DP 1D | House Robber | #198 | Medium |
| Wed | DP 1D | House Robber II | #213 | Medium |
| Thu | DP 1D | Longest Increasing Subsequence | #300 | Medium |
| Fri | DP 1D | Coin Change | #322 | Medium |
| Sat | (project day) | — | — | — |
| Sun | Weakest | — | — | — |

**Pattern note for DP**: "what would I have to know about smaller subproblems to solve this one?" Top-down (memo) is easier to think about; bottom-up (tabulation) is more efficient. Start with top-down.

### Week 18 (Aug 12-18) — DP 1D mediums + DP 2D intro

| Day | Pattern | Problem | LC# | Difficulty |
|---|---|---|---|---|
| Mon | DP 1D | Word Break | #139 | Medium |
| Tue | DP 1D | Decode Ways | #91 | Medium |
| Wed | DP 2D (intro) | Unique Paths | #62 | Medium |
| Thu | DP 2D | Longest Common Subsequence | #1143 | Medium |
| Fri | DP 2D | Edit Distance | #72 | Medium / Hard |
| Sat | (project day) | — | — | — |
| Sun | Weakest | — | — | — |

### Week 19 (Aug 19-25) — Mixed mediums + mock prep

This week is for filling gaps. Pick problems based on patterns where you've felt weakest.

Suggested:
- Mon: Trees medium not solved before
- Tue: Graph medium
- Wed: Heap medium
- Thu: DP 2D medium
- Fri: Sliding Window hard / medium
- Sun: Mock interview style — pick a random medium, time yourself, no hints. Aim < 35 min.

### Week 20 (Aug 26-31) — Mock interview prep

Less new pattern, more mock-style work.

| Day | What |
|---|---|
| Mon | Random medium — time it, simulate "thinking out loud" by writing comments |
| Tue | Random medium, different pattern |
| Wed | Hard problem — even if you don't finish, get the intuition |
| Thu | Random medium |
| Fri | Mock with mentor (or self-record explaining a problem for 5 min) |
| Sat | Rest |
| Sun | Review what came up in mock — 3 weakest patterns |

## How to track

Update the Drill Log at the bottom of `DSA-patterns.md` for each session. Format:

```
| Date | Pattern | Problem (LC#) | Time | Verdict |
| 2026-05-04 | Sorting | #75 Sort Colors | 35 min | hesitated |
```

Verdict: `clean` / `hesitated` / `failed` / `gave up`. After 2 weeks, scan: any pattern with 3+ "failed" or "gave up" — that's your interview risk. Add 1 extra problem in that pattern next weekend.

## Hard rules

- **30 min cap on the daily drill.** If I hit the cap without solving, watch the NeetCode video, type the solution myself (don't paste), move on. Re-attempt that problem on Sunday's weak-pattern slot.
- **Solve cold.** Close the pattern reference, blank cell, start timer. Looking at the pattern reference is fine BEFORE I start, but not during the attempt.
- **Drill on MCA exam days too** (1 problem every 2 days, easy). Skipping risks losing 6 weeks of pattern muscle memory.
- **Sat is project day, drill skipped.** Don't try to do both Sat — project deserves the full block.
- **Don't grind the same problem.** If something is failing 3 attempts in a row across multiple weeks, move on. The pattern matters more than any one problem.

## When to revisit this plan

End of May (May 31): how aggressive was Phase A? Adjust Phase C if I'm ahead/behind.
End of July (post-MCA): assess whether Phase C should compress (if interviews are sooner) or stretch (if MCA pushed harder than expected).
After mock interview: focus on the patterns where the mentor saw weakness.

## Resources

- **NeetCode.io** — pattern-based grouping, video walkthroughs. Primary reference.
- **Sean Prashad's LeetCode Patterns** — alternative grouping, no videos.
- **LeetCode** — practice platform.

When stuck on a problem for >15 min: watch NeetCode video, type the solution yourself, log it as `failed`, move on.

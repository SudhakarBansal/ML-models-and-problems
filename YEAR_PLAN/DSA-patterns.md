# DSA Patterns Reference

> **Purpose**: one-stop, grouped-by-pattern reference for every DSA problem I've solved. Re-read this, not individual notebooks, when I need to recall a pattern. Grows weekly.
>
> **Rule**: when I add a problem here, I write the one-line pattern note *from memory*. If I can't, I haven't understood the pattern yet.

---

## Pattern: Arrays & Hashing

Hashmap/set gives O(1) lookup. Use when "have I seen this before?" or "how many of each?" is the core question.

| # | Problem | LC | File | One-line pattern note |
|---|---------|----|----|------------------------|
| 1 | Two Sum | [#1](https://leetcode.com/problems/two-sum/) | `Week-01/labs/DSA/` | Hashmap of `value → index`; for each `x`, check if `target - x` is in map. |
| 2 | Contains Duplicate | [#217](https://leetcode.com/problems/contains-duplicate/) | `Week-01/labs/DSA/` | Put all in a set; if len differs from list, duplicates exist. |
| 3 | Valid Anagram | [#242](https://leetcode.com/problems/valid-anagram/) | `Week-01/labs/DSA/` | Character counts must match — use `Counter` or length-26 array. |
| 4 | Group Anagrams | [#49](https://leetcode.com/problems/group-anagrams/) | `Week-01/labs/DSA/group_anagram.ipynb` | Key each string by its sorted chars (or char-count tuple); bucket into hashmap. |

---

## Pattern: Two Pointers — Converging (from both ends)

Two indices start at opposite ends and move toward each other based on a decision rule. Requires *sorted* input (usually) or symmetric structure (palindromes). O(n) time, O(1) space.

| # | Problem | LC | File | One-line pattern note |
|---|---------|----|----|------------------------|
| 9 | Valid Palindrome | [#125](https://leetcode.com/problems/valid-palindrome/) | `Week-02/labs/DSA/Valid_Palindrome.ipynb` | Pointers at both ends; skip non-alphanumeric; compare lowercased chars. |
| 12 | Squares of a Sorted Array | [#977](https://leetcode.com/problems/squares-of-a-sorted-array/) | `Week-02/labs/DSA/12-squares-of-a-sorted-array.ipynb` | Largest square is at one of the ends; fill result **from the back**. |
| 13 | Two Sum II (sorted) | [#167](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/) | `Week-02/labs/DSA/13-two-sum-ii-input-array-is-sorted.ipynb` | Sum too big → shrink right; too small → grow left. O(1) space vs Two Sum's hashmap. |
| 16 | Container With Most Water | [#11](https://leetcode.com/problems/container-with-most-water/) | `Week-03/labs/DSA/16-container-with-most-water.ipynb` | Area = min(h_l, h_r) × (r − l). Always move the shorter wall — moving the taller can only shrink area. |
| D-1 | Reverse Vowels of a String *(drill)* | [#345](https://leetcode.com/problems/reverse-vowels-of-a-string/) | `Week-03/labs/DSA/drill-345-reverse-vowels.ipynb` | Two pointers; skip non-vowels on each side, swap when both are vowels. |

---

## Pattern: Two Pointers — Slow/Fast (in-place rewrite)

Slow pointer marks the next write position; fast pointer scans forward for the next valid value. Use for in-place array modification.

| # | Problem | LC | File | One-line pattern note |
|---|---------|----|----|------------------------|
| 10 | Move Zeroes | [#283](https://leetcode.com/problems/move-zeroes/) | `Week-02/labs/DSA/Move_Zeros.ipynb` | Slow = next non-zero slot; fast scans. Swap on non-zero. |
| 11 | Remove Duplicates from Sorted Array | [#26](https://leetcode.com/problems/remove-duplicates-from-sorted-array/) | `Week-02/labs/DSA/11-remove-duplicates-from-sorted-array.ipynb` | Slow tracks last unique; fast scans. Write on mismatch because input is sorted. |

---

## Pattern: Two Pointers — From the Back (in-place merge)

Fill result/merged array from the tail end to avoid overwriting unread data.

| # | Problem | LC | File | One-line pattern note |
|---|---------|----|----|------------------------|
| 8 | Merge Sorted Array | [#88](https://leetcode.com/problems/merge-sorted-array/) | `Week-01/labs/DSA/Merge_Sorted_Array_88L.ipynb` | Three pointers: end of nums1 real data, end of nums2, write position at end. Write the larger. |

---

## Pattern: Sliding Window / Running State

Track a rolling quantity (min, max, sum) as you scan. No explicit window size needed for "best-so-far" variants.

| # | Problem | LC | File | One-line pattern note |
|---|---------|----|----|------------------------|
| 5 | Best Time to Buy and Sell Stock | [#121](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/) | `Week-01/labs/DSA/Best Time to Buy and Sell Stock.ipynb` | Track `min_so_far`; best profit = max of (price − min_so_far) over all prices. |
| 6 | Maximum Subarray (Kadane's) | [#53](https://leetcode.com/problems/maximum-subarray/) | `Week-02/labs/DSA/Maximim_subarray.ipynb` | Running sum; reset to current element when running sum goes negative. |

---

## Pattern: Prefix / Suffix Products

Precompute products/sums from one side, then combine with a scan from the other side. Trades a pass for O(1)-amortized lookups.

| # | Problem | LC | File | One-line pattern note |
|---|---------|----|----|------------------------|
| 7 | Product of Array Except Self | [#238](https://leetcode.com/problems/product-of-array-except-self/) | `Week-01/labs/DSA/` | Two passes: left-products, then multiply by right-product on the return pass. No division. |

---

## Pattern: Stack — LIFO match for nested structures

Use when "I have to match this thing with the **most recent unmatched** thing." Push on open/start, pop on close/end and verify match. Two failure modes to keep separate: pop-from-empty (no opener) and wrong-type-pop (opener mismatched closer). Non-empty stack at end = unclosed openers.

| # | Problem | LC | File | One-line pattern note |
|---|---------|----|----|------------------------|
| 17 | Valid Parentheses | [#20](https://leetcode.com/problems/valid-parentheses/) | `Week-03/labs/DSA/17-valid-parentheses.ipynb` | Map closer→opener; push openers; on closer, fail if stack empty or pop ≠ expected. End: stack must be empty. |

---

## Pattern: Strings — Vertical Scan

Walk character columns across a list of strings. Stop at the first column where any string disagrees or runs out. O(S) total chars in worst case, O(1) extra space.

| # | Problem | LC | File | One-line pattern note |
|---|---------|----|----|------------------------|
| 18 | Longest Common Prefix | [#14](https://leetcode.com/problems/longest-common-prefix/) | `Week-03/labs/DSA/18-longest-common-prefix.ipynb` | For column j of strs[0], check every other string at j; bail on mismatch or string-end and return strs[0][:j]. |

---

## Pending / Next

- **Thu (Week 3)**: #3 Longest Substring Without Repeating Characters (first Sliding Window medium), #155 Min Stack (Stack continuation).
- **Sun spaced review**: pick the shakiest pattern from this week — likely Stack (only one problem solved) or Vertical Scan (single example). Re-solve cold, no peeking.
- **Future mediums in queue**: #15 3Sum (converging pointers nested in fix-one), #42 Trapping Rain Water (converging-pointer template, monotonic invariant).

---

## How to use this doc

1. **Before solving a new problem**: skim the pattern list. Does the new problem resemble any of these? If yes, the pattern note should trigger the right approach.
2. **During Sunday spaced review**: pick 3 random problems from this list. Close the doc. Try to state the one-line pattern note from memory. Compare.
3. **When adding a new entry**: write the pattern note *from memory*. If I can't, the pattern isn't consolidated — re-solve the problem on a blank page before adding it.

---

## Daily Pattern Drill — Curriculum (starts Mon Apr 27, Week 3)

**Protocol**
- **15-min hard cap** per drill. At the start of each study session.
- **One new problem per day** in that day's pattern. Builds pattern fluency through varied exposure (better for interview prep than re-solving the same problem).
- **Solve cold**: close the notebook, blank cell, start timer. No peeking at pattern reference during the 15 min.
- If you hit the cap without solving: watch NeetCode's video, code the solution yourself (don't paste), move on. Revisit in Sunday's weakest-pattern slot.
- Log results at the bottom of this file (date, pattern, problem, time, verdict: `clean` / `hesitated` / `failed`).
- **Skip Saturday drill** — that's Project 2 deep-work day.

> **Coordination with ML drill** (added Apr 23): DSA drill runs on **Tue / Thu / Sun**; ML drill (see `ML-drills.md`) runs on Mon / Wed / Fri / Sun. Don't stack both on the same day — keeps total drill time at 15 min/day within budget. Mon / Wed / Fri assignments in the table below act as "available backup" if you want to swap Sun's slot for a different pattern.

### Rotation

| Day | Pattern |
|---|---|
| Mon | Arrays & Hashing |
| Tue | Two Pointers — Converging |
| Wed | Two Pointers — Slow/Fast |
| Thu | Sliding Window / Running State |
| Fri | Prefix / Suffix / Running Sum |
| Sat | — (Project day) |
| Sun | Weakest pattern of the week (your call) |

### Pre-picked problems (4 weeks)

All EASY unless marked *(stretch M)*. *(stretch M)* entries will likely blow the 15-min cap on first attempt — that's expected in Weeks 5-6 as you transition to mediums.

| Week | Mon (A&H) | Tue (TP-Conv) | Wed (TP-SF) | Thu (SlideWin) | Fri (Prefix) |
|---|---|---|---|---|---|
| **3** (Apr 27–May 3) | [#383 Ransom Note](https://leetcode.com/problems/ransom-note/) | [#345 Reverse Vowels](https://leetcode.com/problems/reverse-vowels-of-a-string/) | [#905 Sort Array by Parity](https://leetcode.com/problems/sort-array-by-parity/) | [#643 Max Avg Subarray I](https://leetcode.com/problems/maximum-average-subarray-i/) | [#1480 Running Sum](https://leetcode.com/problems/running-sum-of-1d-array/) |
| **4** (May 4–10) | [#205 Isomorphic Strings](https://leetcode.com/problems/isomorphic-strings/) | [#680 Valid Palindrome II](https://leetcode.com/problems/valid-palindrome-ii/) | [#268 Missing Number](https://leetcode.com/problems/missing-number/) | [#219 Contains Duplicate II](https://leetcode.com/problems/contains-duplicate-ii/) | [#724 Find Pivot Index](https://leetcode.com/problems/find-pivot-index/) |
| **5** (May 11–17) | [#169 Majority Element](https://leetcode.com/problems/majority-element/) | [#9 Palindrome Number](https://leetcode.com/problems/palindrome-number/) | [#80 Remove Duplicates II](https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/) *(stretch M)* | [#3 Longest Substr w/o Repeat](https://leetcode.com/problems/longest-substring-without-repeating-characters/) *(stretch M)* | [#1732 Highest Altitude](https://leetcode.com/problems/find-the-highest-altitude/) |
| **6** (May 18–24) | [#350 Intersection of 2 Arrays II](https://leetcode.com/problems/intersection-of-two-arrays-ii/) | [#1768 Merge Strings Alternately](https://leetcode.com/problems/merge-strings-alternately/) | [#287 Find Duplicate](https://leetcode.com/problems/find-the-duplicate-number/) *(stretch M)* | [#209 Min Size Subarray Sum](https://leetcode.com/problems/minimum-size-subarray-sum/) *(stretch M)* | [#560 Subarray Sum = K](https://leetcode.com/problems/subarray-sum-equals-k/) *(stretch M)* |

**Sun slot**: no pre-assignment. Pick the pattern that felt shakiest or revisit a problem you failed during the week.

### Drill Log

_Add one row per drill session. After a month, scan for patterns that repeatedly show `hesitated` or `failed` — that's your interview risk._

| Date | Pattern | Problem (LC #) | Time | Verdict |
|------|---------|----------------|------|---------|
| 2026-04-27 | Arrays & Hashing | #383 Ransom Note | ~15 min | clean |
| 2026-04-28 | Two Pointers — Converging | #345 Reverse Vowels | ≤15 min | clean |
| 2026-04-29 | Two Pointers — Slow/Fast | #905 Sort Array by Parity | ~15 min | clean |
| 2026-04-30 | Sliding Window (fixed-size) | #643 Max Avg Subarray I | ~15 min | clean |
| 2026-05-01 | Prefix / Running Sum | #1480 Running Sum of 1d Array | ~15 min | clean |

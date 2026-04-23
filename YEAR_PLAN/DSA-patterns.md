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

## Pending / Next

- **14. Reverse String** [#344](https://leetcode.com/problems/reverse-string/) — Two Pointers converging, planned for Sunday.
- **15+**: 3Sum, Container With Most Water — first real medium-level Two Pointers. After Week 2 confidence check.

---

## How to use this doc

1. **Before solving a new problem**: skim the pattern list. Does the new problem resemble any of these? If yes, the pattern note should trigger the right approach.
2. **During Sunday spaced review**: pick 3 random problems from this list. Close the doc. Try to state the one-line pattern note from memory. Compare.
3. **When adding a new entry**: write the pattern note *from memory*. If I can't, the pattern isn't consolidated — re-solve the problem on a blank page before adding it.

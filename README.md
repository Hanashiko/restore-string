# Restore String

A solution to the [Restore the String](https://leetcode.com/problems/shuffle-string/) problem (LeetCode #1528).

## Problem

Given a string `s` and an integer array `indices` of the same length, rearrange the characters of `s` so that the character at the `i`-th position moves to `indices[i]`.

## Example

```
Input:  s = "codeleet", indices = [4,5,6,7,0,2,1,3]
Output: "leetcode"
```

## Usage

```bash
python main.py
```

## Complexity

- Time: O(n²) — due to `indices.index(i)` inside the loop
- Space: O(n)

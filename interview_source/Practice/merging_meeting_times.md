# Merging Meeting Times

## Problem Statement

Your company built an in-house calendar tool called HiCal. You want to add a feature to see the times in a day when everyone is available.

To do this, you'll need to know when any team is having a meeting.

In HiCal, a meeting is stored as a tuple of integers `(start_time, end_time)`. These integers represent the number of 30-minute blocks past 9:00 am.

For example:
```python
(2, 3)  # Meeting from 10:00 – 10:30 am
(6, 9)  # Meeting from 12:00 – 1:30 pm
```

---

## The Task

Write a function `merge_ranges()` that takes a list of multiple meeting time ranges and returns a list of condensed ranges.

### Example

**Input:**
```python
[(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]
```

**Output:**
```python
[(0, 1), (3, 8), (9, 12)]
```

---

## Constraints

1. **Do not assume meetings are in order** - The meeting times are coming from multiple teams and may be randomly ordered
2. **No upper bound** - The function should work even for very large numbers (like Unix timestamps)
3. **Efficiency matters** - Your solution should be efficient even without knowing the upper bound

---

## Gotchas: Edge Cases to Consider

### Case 1: Adjacent Meetings
```python
[(1, 2), (2, 3)]
```

These meetings should be merged into `[(1, 3)]` even though they don't overlap—they just "touch" at time 2.

**Does your function handle this?**

### Case 2: Subsumed Meetings
```python
[(1, 5), (2, 3)]
```

The second meeting starts later but ends before the first meeting ends. Your function should correctly keep the merged range as `[(1, 5)]`.

**Does your function handle this?**

### Case 3: Multiple Merges
```python
[(1, 10), (2, 6), (3, 5), (7, 9)]
```

All of these meetings should merge together into `[(1, 10)]`.

After merging the first two, the result may need to be merged with other meetings. Don't stop too early!

**Does your function handle this?**

### Case 4: Don't Lose the Last Meeting
Make sure your function includes the last meeting in the output!

---

## Approach: Breakdown

### Two Meetings Example

Let's start simple with two meetings:
```python
[(1, 3), (2, 4)]
```

These clearly overlap, so we should merge to get:
```python
[(1, 4)]
```

**How do we know they overlap?**

The end time of the first meeting (3) is at or after the start time of the second meeting (2).

### The Catch: Ordering Matters

This only works if we know which meeting is "first." We need to handle these cases:

1. **End time equals start time**: `[(1, 2), (2, 3)]` → should merge
2. **Second meeting ends first**: `[(1, 5), (2, 3)]` → merge but keep outer bounds

### The Algorithm

1. **Sort meetings by start time** - Then any meetings that could merge are adjacent
2. **Walk through sorted list** - Check if each meeting can merge with the previous one
3. **Merge or add** - Either merge with previous, or add as a new separate meeting

---

## Solution

```python
def merge_ranges(meetings):
    # Sort by start time
    sorted_meetings = sorted(meetings)

    # Initialize merged_meetings with the earliest meeting
    merged_meetings = [sorted_meetings[0]]

    for current_meeting_start, current_meeting_end in sorted_meetings[1:]:
        last_merged_meeting_start, last_merged_meeting_end = merged_meetings[-1]

        # If the current meeting overlaps with the last merged meeting, use the
        # later end time of the two
        if current_meeting_start <= last_merged_meeting_end:
            merged_meetings[-1] = (last_merged_meeting_start,
                                   max(last_merged_meeting_end,
                                       current_meeting_end))
        else:
            # Add the current meeting since it doesn't overlap
            merged_meetings.append((current_meeting_start, current_meeting_end))

    return merged_meetings
```

### How It Works Step-by-Step

**Input:** `[(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]`

**Step 1: Sort by start time**
```python
sorted_meetings = [(0, 1), (3, 5), (4, 8), (9, 10), (10, 12)]
```

**Step 2: Initialize with first meeting**
```python
merged_meetings = [(0, 1)]
```

**Step 3: Process each subsequent meeting**

- **(3, 5)**: 3 > 1, so no overlap. Add it: `[(0, 1), (3, 5)]`
- **(4, 8)**: 4 ≤ 5, so overlap! Merge: `[(0, 1), (3, 8)]`
- **(9, 10)**: 9 > 8, so no overlap. Add it: `[(0, 1), (3, 8), (9, 10)]`
- **(10, 12)**: 10 ≤ 10, so overlap! Merge: `[(0, 1), (3, 8), (9, 12)]`

**Output:** `[(0, 1), (3, 8), (9, 12)]` ✓

---

## Complexity Analysis

### Time Complexity: O(n log n)

- **Sorting:** O(n log n) - The most expensive operation
- **Merging:** O(n) - Single pass through the sorted list
- **Overall:** O(n log n) + O(n) = O(n log n)

**Note:** If the input were already sorted, we could do this in O(n) time!

### Space Complexity: O(n)

- In the worst case, no meetings overlap, so the output list is the same size as the input
- We create a new list with O(n) space

---

## Algorithm Insight: Greedy + Sorting

This problem uses a **greedy approach** combined with **sorting**.

### Why Sorting Was Key

We initially tried to solve this in one pass, but it didn't work. Why?

To see if a meeting can be merged with another, we'd have to check all other meetings. But since the meetings are in random order, we can't do this efficiently in one pass.

The insight: **If we sort first, then meetings that can be merged will be adjacent!**

This transforms the problem from O(n²) comparisons to O(n) comparisons (after sorting).

---

## Bonus Questions

### Bonus 1: Upper Bound
What if we did have an upper bound on the input values? Could we improve our runtime? Would it cost us memory?

**Hint:** Think about counting sort or radix sort...

### Bonus 2: In-Place Solution
Could we do this "in place" on the input list and save some space? What are the pros and cons?

**Hint:** We could modify the list directly instead of creating a new one...

### Bonus 3: Already Sorted Input
The solution would be O(n) if the input were already sorted. How would you modify it?

---

## Key Takeaways

1. **Sorting can transform complexity** - O(n²) brute force → O(n log n) with sorting
2. **Greedy works after sorting** - Once sorted, we can greedily merge adjacent ranges
3. **Check edge cases carefully** - Adjacent meetings, subsumed meetings, multiple merges
4. **Consider amortized costs** - The input's structure (sorted vs unsorted) matters
5. **Think about in-place tradeoffs** - Space savings vs code clarity

---

## Testing Your Solution

Test your implementation with these cases:

```python
# Basic case from problem
assert merge_ranges([(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]) == [(0, 1), (3, 8), (9, 12)]

# Adjacent meetings
assert merge_ranges([(1, 2), (2, 3)]) == [(1, 3)]

# Subsumed meeting
assert merge_ranges([(1, 5), (2, 3)]) == [(1, 5)]

# All meetings merge
assert merge_ranges([(1, 10), (2, 6), (3, 5), (7, 9)]) == [(1, 10)]

# No overlaps
assert merge_ranges([(1, 2), (3, 4), (5, 6)]) == [(1, 2), (3, 4), (5, 6)]

# Single meeting
assert merge_ranges([(1, 5)]) == [(1, 5)]

# Unsorted input
assert merge_ranges([(5, 7), (1, 3), (4, 5)]) == [(1, 3), (4, 7)]
```

---

## Next Steps

1. **Implement the solution yourself** - Try it without looking at the solution
2. **Test the edge cases** - Make sure you handle all gotchas
3. **Optimize if possible** - Can you improve the space complexity?
4. **Answer the bonus questions** - Think deeply about alternative approaches
5. **Practice explaining** - Be ready to walk an interviewer through your approach


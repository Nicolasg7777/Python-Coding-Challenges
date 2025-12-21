# Merge Sorted Arrays

## Problem Statement

In order to win the prize for most cookies sold, you and your friend Alice are going to merge your Girl Scout Cookies orders and enter as one unit.

Each order is represented by an "order id" (an integer).

You have your lists of orders sorted numerically already, in lists. Write a function to **merge your lists of orders into one sorted list**.

### Example

**Input:**
```python
my_list = [3, 4, 6, 10, 11, 15]
alices_list = [1, 5, 8, 12, 14, 19]

merge_lists(my_list, alices_list)
```

**Output:**
```python
[1, 3, 4, 5, 6, 8, 10, 11, 12, 14, 15, 19]
```

---

## Gotchas

### Gotcha 1: Don't Just Sort!
We can do this in **O(n) time** and **O(n) space**.

If you're running a built-in sorting function, you're probably taking **O(n log n)** time. That's slower than necessary!

### Gotcha 2: Use the Sorted Property!
The key insight: the input lists are **already sorted**. This fact should help us solve the problem faster.

### Gotcha 3: Handle Exhausted Lists
When we've merged in all elements from one list but still have elements in the other, we need to handle this correctly. This is the trickiest part!

---

## Why Not Just Sort?

### The Naive Approach
```python
def merge_lists_naive(my_list, alices_list):
    return sorted(my_list + alices_list)
```

**Time Complexity:** O(n log n), where n is the total length

**Why it's inefficient:** We're completely ignoring the fact that the inputs are already sorted!

---

## The Insight: Two-Pointer Approach

### Key Observation

Since both lists are sorted:
- The smallest element overall is at index 0 of one of the lists
- The next smallest is either at index 0 of one list, or index 1 of the other
- And so on...

We can use **two pointers** to track the current position in each list and build the merged list by always picking the smaller of the two "current" elements.

### The Algorithm in Concept

1. Create a new list to hold the merged result
2. Start at the beginning of both input lists
3. Compare the current elements from each list
4. Add the smaller one to the merged list
5. Move forward in whichever list we took from
6. Repeat until one list is exhausted
7. Copy remaining elements from the non-empty list

---

## Building the Solution Step-by-Step

### Step 1: Start Simple

Let's just find the first element:

```python
def merge_lists_v1(my_list, alices_list):
    merged_list_size = len(my_list) + len(alices_list)
    merged_list = [None] * merged_list_size

    head_of_my_list = my_list[0]
    head_of_alices_list = alices_list[0]

    if head_of_my_list < head_of_alices_list:
        merged_list[0] = head_of_my_list
    else:
        merged_list[0] = head_of_alices_list

    return merged_list
```

This works for finding the first element, but we need to generalize it for all elements.

### Step 2: Add Indices to Track Progress

Now let's merge multiple elements:

```python
def merge_lists_v2(my_list, alices_list):
    merged_list_size = len(my_list) + len(alices_list)
    merged_list = [None] * merged_list_size

    current_index_alices = 0
    current_index_mine = 0
    current_index_merged = 0

    while current_index_merged < merged_list_size:
        first_unmerged_alices = alices_list[current_index_alices]
        first_unmerged_mine = my_list[current_index_mine]

        if first_unmerged_mine < first_unmerged_alices:
            merged_list[current_index_merged] = first_unmerged_mine
            current_index_mine += 1
        else:
            merged_list[current_index_merged] = first_unmerged_alices
            current_index_alices += 1

        current_index_merged += 1

    return merged_list
```

This works when both lists have elements, but crashes with IndexError when one runs out!

### Step 3: Handle Edge Cases (4 Cases)

Now we need to handle when one list is exhausted:

```python
def merge_lists_v3(my_list, alices_list):
    merged_list_size = len(my_list) + len(alices_list)
    merged_list = [None] * merged_list_size

    current_index_alices = 0
    current_index_mine = 0
    current_index_merged = 0

    while current_index_merged < merged_list_size:
        if current_index_mine >= len(my_list):
            # Case 1: my list is exhausted
            merged_list[current_index_merged] = alices_list[current_index_alices]
            current_index_alices += 1
        elif current_index_alices >= len(alices_list):
            # Case 2: Alice's list is exhausted
            merged_list[current_index_merged] = my_list[current_index_mine]
            current_index_mine += 1
        elif my_list[current_index_mine] < alices_list[current_index_alices]:
            # Case 3: my item is next
            merged_list[current_index_merged] = my_list[current_index_mine]
            current_index_mine += 1
        else:
            # Case 4: Alice's item is next
            merged_list[current_index_merged] = alices_list[current_index_alices]
            current_index_alices += 1

        current_index_merged += 1

    return merged_list
```

This works but has repeated code!

### Step 4: Refactor to 2 Cases (Clean Version)

We can combine cases using logic and **short-circuit evaluation**:

```python
def merge_lists(my_list, alices_list):
    merged_list_size = len(my_list) + len(alices_list)
    merged_list = [None] * merged_list_size

    current_index_alices = 0
    current_index_mine = 0
    current_index_merged = 0

    while current_index_merged < merged_list_size:
        is_my_list_exhausted = current_index_mine >= len(my_list)
        is_alices_list_exhausted = current_index_alices >= len(alices_list)

        if (not is_my_list_exhausted and
                (is_alices_list_exhausted or
                 my_list[current_index_mine] < alices_list[current_index_alices])):
            # Take from my list if:
            # - My list is NOT exhausted, AND
            # - EITHER Alice's list IS exhausted, OR
            # - my current element is smaller
            merged_list[current_index_merged] = my_list[current_index_mine]
            current_index_mine += 1
        else:
            # Otherwise take from Alice's list
            merged_list[current_index_merged] = alices_list[current_index_alices]
            current_index_alices += 1

        current_index_merged += 1

    return merged_list
```

---

## How It Works: Step-by-Step Example

**Input:**
```python
my_list = [3, 4, 6, 10, 11, 15]
alices_list = [1, 5, 8, 12, 14, 19]
```

**Execution:**

```
Step 1: Compare 3 and 1 → 1 is smaller
  merged_list = [1, None, None, None, None, None]
  alices_list index: 1

Step 2: Compare 3 and 5 → 3 is smaller
  merged_list = [1, 3, None, None, None, None]
  my_list index: 1

Step 3: Compare 4 and 5 → 4 is smaller
  merged_list = [1, 3, 4, None, None, None]
  my_list index: 2

Step 4: Compare 6 and 5 → 5 is smaller
  merged_list = [1, 3, 4, 5, None, None]
  alices_list index: 2

Step 5: Compare 6 and 8 → 6 is smaller
  merged_list = [1, 3, 4, 5, 6, None]
  my_list index: 3

Step 6: Compare 10 and 8 → 8 is smaller
  merged_list = [1, 3, 4, 5, 6, 8]
  alices_list index: 3

(Continue until done...)

Final: [1, 3, 4, 5, 6, 8, 10, 11, 12, 14, 15, 19]
```

---

## Understanding the Complex Condition

The final solution uses a complex if statement. Let's break it down:

```python
if (not is_my_list_exhausted and
        (is_alices_list_exhausted or
         my_list[current_index_mine] < alices_list[current_index_alices])):
```

### Why This Works: Short-Circuit Evaluation

Python evaluates conditions from left to right and stops early if it knows the answer:

1. **`not is_my_list_exhausted`** - checked first
   - If False: Stop immediately (my list is exhausted, so take from Alice's)
   - If True: Continue to next condition

2. **`is_alices_list_exhausted`** - checked second
   - If True: Stop and take from my list (Alice's is empty)
   - If False: Continue to comparison

3. **`my_list[current_index_mine] < alices_list[current_index_alices]`** - checked last
   - Only evaluated if both lists have elements
   - Safe from IndexError because we checked first!

This clever ordering prevents IndexError while handling all cases.

---

## Complexity Analysis

### Time Complexity: O(n)

- We iterate through the merged list once: O(merged_list_size)
- merged_list_size = len(my_list) + len(alices_list)
- Each element is visited exactly once
- Each iteration does constant work (comparisons, assignments)
- Total: O(n)

### Space Complexity: O(n)

- We allocate a new merged_list of size O(n)
- We use a few index variables: O(1)
- Total additional space: O(n)

**Note:** We can't do this in-place because our input lists aren't big enough to hold the merged result. With linked lists, we could do this by just adjusting pointers (O(1) space).

---

## Edge Cases

### Edge Case 1: One List Is Empty
```python
merge_lists([], [1, 2, 3])
# Result: [1, 2, 3]
```
- my_list is exhausted immediately
- All elements come from alices_list

### Edge Case 2: Both Lists Are Empty
```python
merge_lists([], [])
# Result: []
```
- Loop doesn't run, returns empty list

### Edge Case 3: One Element in Each
```python
merge_lists([3], [1])
# Result: [1, 3]
```

### Edge Case 4: Identical Elements
```python
merge_lists([1, 3], [1, 3])
# Result: [1, 1, 3, 3]
```
- When equal, we take from Alice's list (else clause)

### Edge Case 5: Different Length Lists
```python
merge_lists([1, 2, 3, 4, 5], [6])
# Result: [1, 2, 3, 4, 5, 6]
```
- Longer list elements are copied at the end

---

## Common Mistakes

### Mistake 1: Forgetting to Update Indices
```python
# WRONG: forgot to increment current_index_mine
if my_list[current_index_mine] < alices_list[current_index_alices]:
    merged_list[current_index_merged] = my_list[current_index_mine]
    # Missing: current_index_mine += 1
```

This causes an infinite loop!

### Mistake 2: Accessing Out-of-Bounds Elements
```python
# WRONG: doesn't check if indices are valid
if my_list[current_index_mine] < alices_list[current_index_alices]:
```

Crashes with IndexError when a list is exhausted.

### Mistake 3: Short-Circuit Evaluation Mistake
```python
# WRONG: checks comparison first
if (my_list[current_index_mine] < alices_list[current_index_alices] and
        not is_my_list_exhausted):
```

Will crash if my_list is exhausted (tries to access invalid index before checking).

### Mistake 4: Forgetting to Increment merged Index
```python
# WRONG: forgot to increment current_index_merged
while current_index_merged < merged_list_size:
    # ... add element ...
    # Missing: current_index_merged += 1
```

Infinite loop!

---

## Real-World Applications

This merge operation is used in:
1. **Merge Sort** - The merge step of merge sort uses this exact algorithm
2. **Database operations** - Merging sorted query results
3. **Stream processing** - Combining sorted data streams
4. **External sorting** - Merging chunks of sorted data that don't fit in memory
5. **Version control** - Merging sorted commit histories

---

## Bonus Questions

### Bonus 1: Merge Multiple Sorted Lists

Write a function that takes a list of sorted lists and outputs a single sorted list:

```python
def merge_multiple_lists(list_of_lists):
    # Input: [[1, 5, 8], [2, 4, 6], [3, 7, 9]]
    # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]
    pass
```

**Hint:** You could use a heap/priority queue...

### Bonus 2: In-Place Merge

What if you wanted to merge into the first list instead of creating a new list? How would your approach change?

```python
def merge_into_first(my_list, alices_list):
    # Merge into my_list instead of creating new
    # What would be different?
    pass
```

**Hint:** You might need to resize my_list first...

### Bonus 3: Merge Linked Lists

If these were linked lists instead of arrays, how would your solution change?

```python
def merge_linked_lists(my_list, alices_list):
    # Merge two sorted linked lists
    # Could do this in O(1) space by adjusting pointers!
    pass
```

---

## Testing Your Solution

```python
def test_merge_lists():
    # Basic case from problem
    assert merge_lists([3, 4, 6, 10, 11, 15],
                       [1, 5, 8, 12, 14, 19]) == \
           [1, 3, 4, 5, 6, 8, 10, 11, 12, 14, 15, 19]

    # Empty lists
    assert merge_lists([], [1, 2, 3]) == [1, 2, 3]
    assert merge_lists([1, 2, 3], []) == [1, 2, 3]
    assert merge_lists([], []) == []

    # Single elements
    assert merge_lists([3], [1]) == [1, 3]
    assert merge_lists([1], [3]) == [1, 3]

    # Different lengths
    assert merge_lists([1, 2, 3, 4, 5], [6]) == [1, 2, 3, 4, 5, 6]
    assert merge_lists([6], [1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5, 6]

    # Duplicates
    assert merge_lists([1, 3], [1, 3]) == [1, 1, 3, 3]

    # All elements from one list are smaller
    assert merge_lists([1, 2, 3], [4, 5, 6]) == [1, 2, 3, 4, 5, 6]

    # All elements from one list are larger
    assert merge_lists([4, 5, 6], [1, 2, 3]) == [1, 2, 3, 4, 5, 6]

    print("All tests passed!")

test_merge_lists()
```

---

## Key Insights

1. **Use the input's properties** - The lists are sorted; use that!
2. **Two pointers are powerful** - For sorted arrays, two pointers solve many problems
3. **Edge cases matter** - Handling exhausted lists correctly is critical
4. **Short-circuit evaluation** - Use it to avoid crashes and reduce cases
5. **Complexity** - O(n) time is much better than O(n log n)!

---

## Interview Tips

### What Interviewers Care About
- ✓ Recognizing you can do better than sorting
- ✓ Understanding the two-pointer technique
- ✓ Handling edge cases (exhausted lists)
- ✓ Avoiding IndexError through careful condition ordering
- ✓ Explaining the algorithm clearly

### How to Explain Your Solution

1. **Start naive** - "I could just concatenate and sort for O(n log n)"
2. **Identify better approach** - "But the inputs are already sorted!"
3. **Explain the technique** - "I'll use two pointers from the start"
4. **Walk through example** - Show a few steps of merging
5. **Address edge cases** - "When one list runs out..."
6. **Discuss complexity** - "O(n) time, O(n) space"
7. **Mention alternatives** - "With linked lists, we could do O(1) space"

### Common Interview Questions
- "Can you do better than O(n log n)?"
- "What if the lists were linked lists?"
- "How would you merge k sorted lists?"
- "Can you do this in-place?"
- "What about streaming data?"


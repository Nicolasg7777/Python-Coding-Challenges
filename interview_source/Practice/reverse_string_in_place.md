# Reverse String in Place

## Problem Statement

Write a function that takes a list of characters and reverses the letters **in place**.

### Why a List of Characters?

The goal of this question is to practice manipulating strings in place. Since we're modifying the input, we need a **mutable type** like a list, instead of Python's immutable strings.

In Python 2/3:
- Strings are immutable (can't change them in place)
- Lists are mutable (can modify them)

For interview purposes, this simulates how languages like Java work with character arrays.

---

## Example

**Input:**
```python
['h', 'e', 'l', 'l', 'o']
```

**Output (modified in place):**
```python
['o', 'l', 'l', 'e', 'h']
```

### More Examples

```python
# Single character
['a'] → ['a']

# Two characters
['a', 'b'] → ['b', 'a']

# Empty list
[] → []

# Already reversed
['z', 'y', 'x'] → ['x', 'y', 'z']
```

---

## Approach: Two-Pointer Technique

### The Key Insight

In-place reversal requires **swapping elements**. We can't create a new list—we must modify the original.

The simplest approach: use **two pointers** moving from the outside in.

### Algorithm Breakdown

1. **Initialize pointers:**
   - `left_index` = 0 (start of list)
   - `right_index` = len(list) - 1 (end of list)

2. **While pointers haven't crossed:**
   - Swap characters at `left_index` and `right_index`
   - Move `left_index` forward
   - Move `right_index` backward

3. **Stop when pointers meet in the middle**

### Step-by-Step Example

**Input:** `['h', 'e', 'l', 'l', 'o']`

```
Step 0: [h, e, l, l, o]
        ↑           ↑
        L           R

Swap 'h' and 'o':
[o, e, l, l, h]
  L         R (after move)

Step 1: [o, e, l, l, h]
         ↑        ↑
         L        R

Swap 'e' and 'l':
[o, l, l, e, h]
    L     R (after move)

Step 2: [o, l, l, e, h]
          ↑  ↑
          L  R (crossed!)

Stop - we're done!
```

---

## Solution

```python
def reverse(list_of_chars):
    left_index = 0
    right_index = len(list_of_chars) - 1

    while left_index < right_index:
        # Swap characters
        list_of_chars[left_index], list_of_chars[right_index] = \
            list_of_chars[right_index], list_of_chars[left_index]

        # Move towards middle
        left_index += 1
        right_index -= 1

    # No return needed - modified in place!
```

### How Python Tuple Unpacking Works

```python
list_of_chars[left_index], list_of_chars[right_index] = \
    list_of_chars[right_index], list_of_chars[left_index]
```

This is Python's elegant way to swap:

1. Right side creates a tuple: `(list_of_chars[right_index], list_of_chars[left_index])`
2. Left side unpacks and assigns to both positions
3. No temporary variable needed!

**In other languages:**
```python
# Without tuple unpacking (more verbose):
temp = list_of_chars[left_index]
list_of_chars[left_index] = list_of_chars[right_index]
list_of_chars[right_index] = temp
```

---

## Complexity Analysis

### Time Complexity: O(n)

We visit each character exactly once:
- We make n/2 swaps (each swap involves 2 characters)
- Each swap is O(1)
- Total: n/2 swaps × O(1) = O(n)

Example with n=5:
- We make 2 swaps (h↔o, e↔l)
- That's 5/2 = 2.5 → 2 swaps
- O(2) = O(n)

### Space Complexity: O(1)

We only use a constant amount of extra space:
- Two index variables: `left_index`, `right_index`
- No additional data structures
- No matter how big n gets, we use the same amount of space

**This is the beauty of in-place algorithms!**

---

## Why This is Optimal

### Can we do better than O(n)?

**No.** We have to visit and potentially modify every character, which takes at least O(n) time.

### Can we use less space?

**No.** O(1) is the minimum—you need at least the input itself!

This solution is **optimal** for time and space.

---

## Common Mistakes

### Mistake 1: Comparing to the Middle Wrong

```python
# WRONG: stops too early
while left_index < right_index - 1:  # Wrong!
    swap...

# CORRECT
while left_index < right_index:
```

The middle element doesn't need to be swapped (it's already in place).

### Mistake 2: Modifying the List While Iterating

```python
# WRONG: modifying list length during iteration
for char in list_of_chars:
    # Don't modify list_of_chars here!

# CORRECT: use indices
while left_index < right_index:
    swap...
```

### Mistake 3: Forgetting to Return

```python
# Wait, do we need to return?
def reverse(list_of_chars):
    ...
    return list_of_chars  # This is optional!

# Since we modify in place, returning isn't necessary
# But it's often good practice for clarity
```

---

## Edge Cases

### Empty List
```python
reverse([])
# No swaps needed, returns immediately
# Correct! ✓
```

### Single Character
```python
reverse(['a'])
# left_index = 0, right_index = 0
# 0 < 0 is False, so loop doesn't run
# Correct! ✓
```

### Two Characters
```python
reverse(['a', 'b'])
# left_index = 0, right_index = 1
# 0 < 1 is True, swap 'a' and 'b'
# left_index = 1, right_index = 0
# 1 < 0 is False, exit loop
# Result: ['b', 'a']
# Correct! ✓
```

### Odd Length (5 characters)
```python
reverse(['a', 'b', 'c', 'd', 'e'])
# Swaps: (a,e) then (b,d)
# Middle (c) stays in place
# Result: ['e', 'd', 'c', 'b', 'a']
# Correct! ✓
```

### Even Length (4 characters)
```python
reverse(['a', 'b', 'c', 'd'])
# Swaps: (a,d) then (b,c)
# Result: ['d', 'c', 'b', 'a']
# Correct! ✓
```

---

## Real-World Applications

This two-pointer technique is used in:

1. **String manipulation** - Reversing text
2. **Array manipulation** - Rotating arrays, partitioning
3. **Palindrome checking** - Comparing opposite ends
4. **Container with most water** - LeetCode classic problem
5. **Two sum problems** - Finding pairs in sorted arrays

Learning this pattern opens doors to many problems!

---

## Bonus Questions

### Bonus 1: Return a New Reversed List

Modify the function to **not** modify in place, but return a new reversed list:

```python
def reverse_not_in_place(list_of_chars):
    # What's the time and space complexity?
    # Hint: You could use Python's list reversal
    pass
```

**Hint:** This would use O(n) space but might be clearer in production code.

### Bonus 2: Reverse a String (Not List)

Since strings are immutable in Python, how would you reverse a string?

```python
def reverse_string(string):
    # Convert to list, reverse, convert back
    pass
```

**Hint:** Convert string → list → reverse → convert back to string

### Bonus 3: Reverse Only Certain Characters

What if you wanted to reverse only the vowels in place?

```python
def reverse_vowels_in_place(list_of_chars):
    # Reverse only vowels, keep consonants in place
    pass

# Example: ['h', 'e', 'l', 'o'] → ['h', 'o', 'l', 'e']
```

**Hint:** Use three pointers or a different approach...

---

## Testing Your Solution

```python
def test_reverse():
    # Basic case
    chars = ['h', 'e', 'l', 'l', 'o']
    reverse(chars)
    assert chars == ['o', 'l', 'l', 'e', 'h']

    # Single character
    chars = ['a']
    reverse(chars)
    assert chars == ['a']

    # Two characters
    chars = ['a', 'b']
    reverse(chars)
    assert chars == ['b', 'a']

    # Empty list
    chars = []
    reverse(chars)
    assert chars == []

    # Odd length
    chars = ['a', 'b', 'c', 'd', 'e']
    reverse(chars)
    assert chars == ['e', 'd', 'c', 'b', 'a']

    # Even length
    chars = ['a', 'b', 'c', 'd']
    reverse(chars)
    assert chars == ['d', 'c', 'b', 'a']

    # All same character
    chars = ['x', 'x', 'x']
    reverse(chars)
    assert chars == ['x', 'x', 'x']

    print("All tests passed!")

test_reverse()
```

---

## Key Insights

1. **Two-pointer technique is powerful** - For many in-place problems
2. **In-place saves space** - O(1) vs O(n) for creating a new list
3. **Trade-offs exist** - In-place is less readable in some cases
4. **Edge cases matter** - Empty, single element, even/odd length
5. **Pattern recognition** - This technique appears in many problems

---

## Interview Tips

### What the Interviewer Cares About
- ✓ Understanding in-place algorithms
- ✓ Recognizing the two-pointer pattern
- ✓ Handling edge cases correctly
- ✓ Explaining your approach clearly
- ✓ Writing clean, readable code

### What They Don't Care About
- ✗ Speed of implementation (clarity > speed)
- ✗ Fancy Python tricks (unless asked)
- ✗ Micro-optimizations

### How to Explain Your Solution

1. **Clarify the problem** - "So we're reversing in place with no extra space?"
2. **Explain the approach** - "I'll use two pointers from the outside in"
3. **Walk through an example** - Use a small input and show the steps
4. **Discuss complexity** - "O(n) time, O(1) space"
5. **Handle edge cases** - "For empty or single element lists..."
6. **Code confidently** - Don't rush; write clear code


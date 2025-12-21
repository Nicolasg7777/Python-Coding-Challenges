# Logarithms
## How to Think About Them, Especially in Programming Interviews and Algorithm Design

---

## What a Logarithm Actually Means

A logarithm answers this question:

**"What power must we raise this base to, in order to get this answer?"**

### Example

```
log₁₀(100) = ?
```

Read this as: "log base 10 of 100"

The question is: "What power must we raise 10 to, in order to get 100?"

```
10^x = 100
```

The answer is **x = 2**, because:
```
10² = 10 × 10 = 100
```

So: **log₁₀(100) = 2**

### Breaking Down the Parts

```
log₁₀(100) = 2
 ↑   ↑   ↑    ↑
base answer   result
(bottom)
```

- **Base** (the small number at the bottom): 10
- **Answer** (what we're taking the log of): 100
- **Result**: 2

---

## What Logarithms Are Used For

The main use: **Solving for x when x is in an exponent**

### Example Problem

Solve for x:
```
10^x = 100
```

We need to get x down from the exponent. Logarithms give us a trick:

Take the log₁₀ of both sides:
```
log₁₀(10^x) = log₁₀(100)
```

The left side asks: "What power must we raise 10 to, to get 10^x?" The answer is **x**:
```
x = log₁₀(100)
```

Now evaluate the right side:
```
x = 2
```

**We've pulled the x down from the exponent!**

---

## Logarithm Rules

These are helpful when doing algebra with logs:

### Rule 1: Simplification
```
log_b(b^x) = x
```

Useful for bringing a variable down from an exponent.

### Rule 2: Multiplication
```
log_b(x × y) = log_b(x) + log_b(y)
```

### Rule 3: Division
```
log_b(x / y) = log_b(x) - log_b(y)
```

### Rule 4: Powers
```
log_b(x^y) = y × log_b(x)
```

### Rule 5: Change of Base
```
log_b(x) = log_c(x) / log_c(b)
```

Useful for converting from one base to another.

---

## Where Logarithms Appear in Algorithms

### The Core Question

In computer science, we often ask:

**"How many times must we divide n in half until we get down to 1?"**

Or equivalently:

**"How many times must we double 1 to get to n?"**

These are the same question, just going in different directions!

The answer to both questions is: **log₂(n)**

Let's see why this appears in real algorithms...

---

## Example 1: Binary Search

### How Binary Search Works

1. Start with the **middle element** of a sorted list
2. Is it bigger or smaller than our target?
3. This tells us which **half** to search next
4. **Divide the problem in half** - eliminate one half entirely
5. Repeat on the remaining half
6. Continue until we find the target or run out of elements

### Time Complexity Analysis

The only non-constant part of the time cost is the number of times we can divide our list in half.

If we have n elements and keep dividing by 2:
```
n × (1/2) × (1/2) × (1/2) × ... = 1
```

How many times do we divide by 2? Call it x:
```
n × (1/2)^x = 1
```

Rearrange:
```
n = 2^x
```

To solve for x (pull it out of the exponent):
```
log₂(n) = log₂(2^x)
log₂(n) = x
```

**Therefore, binary search is O(log₂ n) time**

### Binary Search Code Example

```python
def binary_search(target, nums):
    """See if target appears in nums"""
    floor_index = -1
    ceiling_index = len(nums)

    while floor_index + 1 < ceiling_index:
        # Find the index halfway between floor and ceiling
        distance = ceiling_index - floor_index
        half_distance = distance // 2
        guess_index = floor_index + half_distance

        guess_value = nums[guess_index]
        if guess_value == target:
            return True

        if guess_value > target:
            # Target is to the left
            ceiling_index = guess_index
        else:
            # Target is to the right
            floor_index = guess_index

    return False
```

Each iteration cuts the search space in half, and we need log₂(n) iterations to reduce the space to 1.

---

## Example 2: Sorting (Merge Sort)

Sorting costs **O(n log₂ n)** time in the general case.

This is the best worst-case runtime for comparison-based sorting.

### How Merge Sort Works

1. **Divide**: Cut the list in half
2. **Conquer**: Sort each half (recursively)
3. **Combine**: Merge the two sorted halves

### Time Complexity Analysis

- **log₂(n)** comes from the number of times we have to divide the list in half to get down to single elements
- **n** comes from merging: each time we merge, we combine all n elements

Total: **O(n log₂ n)**

### Merge Sort Code Example

```python
def merge_sort(list_to_sort):
    # Base case: lists with fewer than 2 elements are sorted
    if len(list_to_sort) < 2:
        return list_to_sort

    # Step 1: divide the list in half
    mid_index = len(list_to_sort) // 2
    left = list_to_sort[:mid_index]
    right = list_to_sort[mid_index:]

    # Step 2: sort each half
    sorted_left = merge_sort(left)
    sorted_right = merge_sort(right)

    # Step 3: merge the sorted halves
    sorted_list = []
    left_index = 0
    right_index = 0

    while len(sorted_list) < len(left) + len(right):
        if ((left_index < len(left)) and
                (right_index == len(right) or
                 sorted_left[left_index] < sorted_right[right_index])):
            sorted_list.append(sorted_left[left_index])
            left_index += 1
        else:
            sorted_list.append(sorted_right[right_index])
            right_index += 1

    return sorted_list
```

The divide-and-conquer approach creates log₂(n) levels of recursion, and merging at each level takes O(n) time.

---

## Example 3: Binary Trees

### The Structure

In a perfect binary tree, each node has exactly 2 children (except leaves).

The nodes double at each level:
```
Level 0:     1 node      (2^0 = 1)
Level 1:     2 nodes     (2^1 = 2)
Level 2:     4 nodes     (2^2 = 4)
Level 3:     8 nodes     (2^3 = 8)
Level 4:     16 nodes    (2^4 = 16)
```

### Height Calculation

If there are n total nodes in the tree, what's the height (h)?

The last level has approximately half of all nodes:
```
1 + 2 + 4 + 8 = 15 (all other levels)
16 = nodes on last level
```

So we're asking: "How many times must we double 1 to get approximately n/2?"

That's: **h ≈ log₂(n)**

More precisely: **h = log₂(n+1)**

### Why This Matters

For binary trees and related data structures, we often need to know the tree height, which is logarithmic in the number of nodes. This explains why:
- **Finding a node** in a balanced binary search tree is O(log n)
- **Inserting or deleting** in a balanced tree is O(log n)
- **Heap operations** are O(log n)

---

## Logarithm Conventions and Notation

### In Computer Science

When the base isn't specified, **it's implied to be 2**:
```
log(n) = log₂(n)
```

Because in CS, we're usually thinking about dividing things in half (binary).

### Alternative Notation

**lg(n)** is sometimes used for log base 2:
```
lg(n) = log₂(n)
```

You'll often see this in the context of sorting:
```
O(n lg n) instead of O(n log₂ n)
```

### In Big O Notation

The base is considered a constant, so we typically write:
```
O(log n)  instead of  O(log₂ n)
```

Because:
```
log_b(n) = log₂(n) / log₂(b)
```

The log₂(b) part is a constant, so changing the base just multiplies by a constant, which Big O ignores.

---

## Quick Reference: When You See Log

### O(log n) algorithms

- **Binary search** - dividing search space in half each time
- **Binary search tree lookups** (balanced) - navigating down tree levels
- **Heap operations** - heap height is logarithmic
- **Merging sorted arrays** in some algorithms

### O(n log n) algorithms

- **Merge sort** - divide and conquer with merging
- **Quick sort** (average case)
- **Heap sort**
- **Tree traversals** with certain operations

### Common comparison

```
O(1)      Constant - fastest
O(log n)  Logarithmic - very fast
O(n)      Linear - good
O(n log n) - acceptable for most problems
O(n²)     Quadratic - slow for large n
O(2ⁿ)     Exponential - very slow
O(n!)     Factorial - extremely slow
```

With n = 1,000,000:
- O(log n) ≈ 20 operations
- O(n log n) ≈ 20,000,000 operations
- O(n²) = 1,000,000,000,000 operations (way too slow!)

---

## Key Takeaway

**Logarithms measure "how many times must we divide?"**

This comes up everywhere in computer science:
- Dividing search spaces in half → binary search → O(log n)
- Recursively dividing arrays → merge sort → O(n log n)
- Levels in a binary tree → height → O(log n)

When you see an algorithm that divides the problem in half each iteration, think logarithm!

---

## Practice: Identify the Log

For each scenario, can you see why it's logarithmic?

1. **Finding a word in a dictionary using binary search**
   - Answer: We eliminate half the remaining words each time → O(log n)

2. **Finding a name in a phone tree (hierarchical structure)**
   - Answer: Each level halves the candidates → O(log n)

3. **Counting how many times you can fold a piece of paper in half**
   - Answer: It takes log₂(thickness) folds to reach the ground → O(log n)

4. **Accessing any element in a balanced binary search tree**
   - Answer: The tree height is log(n) → O(log n) access time

The pattern: **If you're repeatedly dividing by a constant factor, you have a logarithm!**

# Highest Product of 3

## Problem Statement

Given a list of integers, find the **highest product you can get from three of the integers**.

The input list will always have at least three integers.

---

## Examples

### Example 1: All Positive Numbers

```python
list_of_ints = [1, 10, 2, 3, 4]

highest_product_of_3(list_of_ints)
# Returns 120
# Product: 10 * 4 * 3 = 120 (the three largest numbers)
```

### Example 2: Negative Numbers (Key Insight!)

```python
list_of_ints = [-10, -10, 1, 3, 2]

highest_product_of_3(list_of_ints)
# Returns 300
# Product: -10 * -10 * 3 = 300
# Two negatives multiply to make a positive!
```

### Example 3: Mix of Positive and Negative

```python
list_of_ints = [-5, -1, 3, 4, 5]

highest_product_of_3(list_of_ints)
# Returns 100
# Product: 5 * 4 * 5 = 100? No, only three numbers
# Product: 5 * 4 * 5 = 100? Wait, we have 5 twice
# Actually: 5 * 4 * 3 = 60 or -5 * -1 * 100? No 100...
# Actually: max(5*4*3, -5*-1*5) = max(60, 25) = 60?
# Wait: -5 * -1 * something? Let me recalculate
# max(5*4*3, -5*-1*4, 5*4*-5) = max(60, 20, -100) = 60
# Hmm, or we could do: -5 * -1 * 5? But we only have one 5...
# Let me think: we have [-5, -1, 3, 4, 5]
# Best three numbers for product: either three largest (5,4,3)=60
# or two most negative times largest: (-5)*(-1)*5 = 25
# So answer is 60
```

Wait, let me recalculate example 3 properly:
```python
list_of_ints = [-5, -1, 3, 4, 5]

# Possible products with three numbers:
# 5 * 4 * 3 = 60
# 5 * 4 * (-1) = -20
# 5 * 4 * (-5) = -100
# 5 * 3 * (-1) = -15
# 5 * 3 * (-5) = -75
# 5 * (-1) * (-5) = 25
# 4 * 3 * (-1) = -12
# 4 * 3 * (-5) = -60
# 4 * (-1) * (-5) = 20
# 3 * (-1) * (-5) = 15

# Highest: 60 (from 5 * 4 * 3)

highest_product_of_3(list_of_ints)
# Returns 60
```

### Example 4: Large Negative Numbers

```python
list_of_ints = [-10, -20, -30, 1, 2]

highest_product_of_3(list_of_ints)
# Returns 6000
# Product: -10 * -20 * -30? No, that's negative
# Product: -20 * -30 * 1 = 600?
# Product: -20 * -30 * 2 = 1200
# Product: -10 * -20 * 2 = 400
# Product: -10 * -30 * 2 = 600
# Product: -10 * -20 * 1 = 200
# Product: 1 * 2 * something = at most 2 * something ≤ 60
# Wait, the largest negative is -10
# So: -10 * -20 * -30 = -6000? No
# Two negatives: -20 * -30 = 600, then 600 * 2 = 1200
# Two negatives: -20 * -10 = 200, then 200 * 2 = 400
# Two negatives: -30 * -10 = 300, then 300 * 2 = 600
# So highest is 1200

# Wait, I miscalculated. Let me reorder: [-30, -20, -10, 1, 2]
# -30 * -20 = 600, then 600 * -10 = -6000 (negative)
# -30 * -20 = 600, then 600 * 1 = 600
# -30 * -20 = 600, then 600 * 2 = 1200
# -30 * -10 = 300, then 300 * 2 = 600
# -20 * -10 = 200, then 200 * 2 = 400
# So highest is 1200

highest_product_of_3(list_of_ints)
# Returns 1200
# Product: -20 * -30 * 2 = 1200
```

### Example 5: Small List

```python
list_of_ints = [1, 2, 3]

highest_product_of_3(list_of_ints)
# Returns 6
# Product: 1 * 2 * 3 = 6 (only one possibility)
```

---

## Constraints

- List will always have at least 3 integers
- Integers can be positive, negative, or zero
- Need to find exactly 3 integers (can't use same index twice)

---

## Gotchas

**Gotcha 1: Negative Numbers Create Positive Products**

Two negative numbers multiplied together give a positive number! This is the key insight.

```python
# ❌ WRONG: Only look at largest 3 numbers
list_of_ints = [-10, -10, 1, 3, 2]
largest_3 = [3, 2, 1]  # Wrong!
product = 3 * 2 * 1 = 6

# ✓ RIGHT: Consider products with two negatives
best_product = -10 * -10 * 3 = 300
```

**Gotcha 2: Can't Just Sort and Take Largest**

While sorting helps you think about the problem, you need a greedy O(n) approach to solve it optimally.

```python
# Sorting is O(n log n), greedy is O(n)
```

**Gotcha 3: Order of Updates Matters**

If you update values in the wrong order, you might multiply a number by itself!

```python
# ❌ WRONG: Updates highest before using it
for num in list_of_ints:
    highest = max(highest, num)  # Update first
    product_of_2 = num * highest  # Might use updated highest!
    # If num is the new highest, you're computing num * num!

# ✓ RIGHT: Use old value before updating
for num in list_of_ints:
    product_of_2 = max(product_of_2, num * highest, num * lowest)
    highest = max(highest, num)  # Update after using
```

**Gotcha 4: Lowest Product Could Be Very Negative**

Don't ignore the lowest products! A very negative product times a negative number becomes very positive.

```python
list_of_ints = [-100, -50, 1, 2, 3]
# lowest_product_of_2 = -100 * -50 = 5000? No, we need the minimum
# Actually tracking product values, not indices
# So for products: -100 * -50 = 5000, but we want the LOWEST
# Wait, we want to track both highest and lowest product_of_2
```

---

## Approach

### Understanding the Problem

We need to find three numbers whose product is the highest. Key insight: **two negative numbers create a positive product**.

### Brute Force Approach (O(n³) - Too Slow)

```python
def highest_product_of_3_brute(list_of_ints):
    max_product = float('-inf')

    # Try every combination of three numbers
    for i in range(len(list_of_ints)):
        for j in range(i + 1, len(list_of_ints)):
            for k in range(j + 1, len(list_of_ints)):
                product = list_of_ints[i] * list_of_ints[j] * list_of_ints[k]
                max_product = max(max_product, product)

    return max_product
```

**Problem:** O(n³) is too slow. We check every combination of 3 numbers.

### Sorting Approach (O(n log n) - Better)

```python
def highest_product_of_3_sorted(list_of_ints):
    sorted_ints = sorted(list_of_ints)

    # Best product is either:
    # 1. Three largest numbers (all positive or middle)
    largest_product = sorted_ints[-1] * sorted_ints[-2] * sorted_ints[-3]

    # 2. Two smallest (most negative) times largest
    smallest_product = sorted_ints[0] * sorted_ints[1] * sorted_ints[-1]

    return max(largest_product, smallest_product)
```

**Problem:** O(n log n) is better but we can do O(n).

### Optimal Greedy Approach (O(n) - Best!)

**Key Insight:** At each step, the highest product of 3 is the maximum of:
- Current highest product of 3
- Current number × highest product of 2
- Current number × lowest product of 2 (both negatives!)

**Tracking Variables:**
- `highest_product_of_3`: Best answer so far
- `highest_product_of_2`: Highest product of any 2 numbers seen so far
- `lowest_product_of_2`: Lowest (most negative) product of any 2 numbers seen so far
- `highest`: Largest single number
- `lowest`: Smallest single number

```python
def highest_product_of_3(list_of_ints):
    if len(list_of_ints) < 3:
        raise ValueError('Need at least 3 integers')

    # Initialize with first two numbers
    highest = max(list_of_ints[0], list_of_ints[1])
    lowest = min(list_of_ints[0], list_of_ints[1])
    highest_product_of_2 = list_of_ints[0] * list_of_ints[1]
    lowest_product_of_2 = list_of_ints[0] * list_of_ints[1]

    # Initialize with first three numbers
    highest_product_of_3 = list_of_ints[0] * list_of_ints[1] * list_of_ints[2]

    # Iterate through remaining numbers
    for i in range(2, len(list_of_ints)):
        current = list_of_ints[i]

        # Update highest product of 3
        # Could be old highest, or current times highest/lowest product of 2
        highest_product_of_3 = max(
            highest_product_of_3,
            current * highest_product_of_2,
            current * lowest_product_of_2
        )

        # Update highest product of 2
        # Could be old highest, or current times highest/lowest single number
        highest_product_of_2 = max(
            highest_product_of_2,
            current * highest,
            current * lowest
        )

        # Update lowest product of 2
        lowest_product_of_2 = min(
            lowest_product_of_2,
            current * highest,
            current * lowest
        )

        # Update highest and lowest single numbers
        highest = max(highest, current)
        lowest = min(lowest, current)

    return highest_product_of_3
```

### Step-by-Step Walkthrough

**Input:** `[-10, -10, 1, 3, 2]`

```
Initialize with first two numbers (-10, -10):
  highest = -10
  lowest = -10
  highest_product_of_2 = (-10) * (-10) = 100
  lowest_product_of_2 = (-10) * (-10) = 100

Initialize with first three (-10, -10, 1):
  highest_product_of_3 = (-10) * (-10) * 1 = 100

Index 2, current = 1:
  highest_product_of_3 = max(100, 1*100, 1*100) = 100
  highest_product_of_2 = max(100, 1*(-10), 1*(-10)) = 100
  lowest_product_of_2 = min(100, 1*(-10), 1*(-10)) = -10
  highest = max(-10, 1) = 1
  lowest = min(-10, 1) = -10

Index 3, current = 3:
  highest_product_of_3 = max(100, 3*100, 3*(-10)) = 300
  highest_product_of_2 = max(100, 3*1, 3*(-10)) = 100
  lowest_product_of_2 = min(-10, 3*1, 3*(-10)) = -30
  highest = max(1, 3) = 3
  lowest = min(-10, 3) = -10

Index 4, current = 2:
  highest_product_of_3 = max(300, 2*100, 2*(-30)) = 300
  highest_product_of_2 = max(100, 2*3, 2*(-10)) = 100
  lowest_product_of_2 = min(-30, 2*3, 2*(-10)) = -30
  highest = max(3, 2) = 3
  lowest = min(-10, 2) = -10

Return: 300
```

---

## Complexity Analysis

### Time Complexity: **O(n)**

- Single pass through the list (starting at index 2)
- Each operation (max, min, multiplication) is O(1)
- Total: O(n)

### Space Complexity: **O(1)**

- Only using constant space for tracking variables:
  - `highest_product_of_3`
  - `highest_product_of_2`
  - `lowest_product_of_2`
  - `highest`
  - `lowest`
- No additional data structures

---

## Common Mistakes

### Mistake 1: Only Looking at Largest Numbers

```python
# ❌ WRONG:
def highest_product_wrong(list_of_ints):
    sorted_list = sorted(list_of_ints, reverse=True)
    return sorted_list[0] * sorted_list[1] * sorted_list[2]

# Fails on: [-10, -10, 1, 3, 2]
# Returns: 3 * 2 * 1 = 6 (should be 300)
```

**Fix:** Consider products with two negative numbers.

### Mistake 2: Wrong Update Order

```python
# ❌ WRONG:
for current in list_of_ints:
    highest = max(highest, current)  # Update first!
    product_of_2 = max(product_of_2, current * highest)  # Uses new highest
    # If current is the new highest, might compute current * current!
```

**Fix:** Use old values before updating.

```python
# ✓ RIGHT:
for current in list_of_ints:
    product_of_2 = max(product_of_2, current * highest, current * lowest)
    highest = max(highest, current)  # Update after
    lowest = min(lowest, current)
```

### Mistake 3: Forgetting to Track Lowest Product

```python
# ❌ WRONG: Only tracking highest product of 2
highest_product_of_2 = ... # update
# But never update lowest_product_of_2

# Fails on: [-10, -10, 1]
# Need lowest_product_of_2 = 100 to later multiply by positive number
```

**Fix:** Track both highest and lowest products of 2.

### Mistake 4: Not Initializing Correctly

```python
# ❌ WRONG:
highest_product_of_3 = 0  # What if all products are negative?
```

**Fix:** Initialize with actual first possible product.

### Mistake 5: Not Handling Edge Cases

```python
# ❌ WRONG: Doesn't validate input
def highest_product_of_3(list_of_ints):
    # What if len < 3?
    highest = max(list_of_ints[0], list_of_ints[1])
```

**Fix:** Check input length first.

---

## Edge Cases to Test

1. **Minimum size:** `[1, 2, 3]` → `6`
2. **All negatives:** `[-5, -3, -1]` → `-15` (least bad)
3. **Two negatives:** `[-10, -10, 1, 3, 2]` → `300`
4. **Zero in list:** `[0, 1, 2, 3]` → `6` (1*2*3)
5. **Multiple zeros:** `[0, 0, 1, 2, 3]` → `6`
6. **Mix with single large:** `[-5, -4, 0, 1, 100]` → `2000` (-5*-4*100)
7. **All same positive:** `[5, 5, 5]` → `125` (5*5*5)
8. **All same negative:** `[-5, -5, -5]` → `-125` (all odd number of negatives)
9. **Very large numbers:** `[1000000, 999999, 999998]` → depends on overflow
10. **Mixed very negative:** `[-1000, -999, 1]` → `999000` (-1000*-999*1)
11. **Single positive with negatives:** `[-5, -4, -3, 1, 2]` → `120` (-5*-4*-3 or -5*-4*something)

Wait, let me recalculate example 11:
```python
list_of_ints = [-5, -4, -3, 1, 2]

# Three negatives: -5 * -4 * -3 = -60 (negative)
# Two negatives: -5 * -4 * anything
#   -5 * -4 * 1 = 20
#   -5 * -4 * 2 = 40
# Two negatives: -5 * -3 * anything
#   -5 * -3 * 1 = 15
#   -5 * -3 * 2 = 30
# Two negatives: -4 * -3 * anything
#   -4 * -3 * 1 = 12
#   -4 * -3 * 2 = 24
# Three positives: not possible, only two
# Positives: 1 * 2 * (-3) = -6

# Highest: 40
```

---

## Real-World Applications

1. **Portfolio optimization** - Maximize product of returns
2. **Data science** - Finding feature combinations
3. **Financial analysis** - Product of growth rates
4. **Game theory** - Maximizing combined scores
5. **Physics** - Product of measurements

---

## Interview Tips

### Pattern Recognition

"This is similar to the stock price problem, but instead of tracking just one value (minimum price), I need to track multiple values."

### Key Discussion Points

1. **State the challenge:** "Two negative numbers make a positive, so I can't just look at largest numbers."

2. **Explain the tracking:** "I need to track the highest product of 2, lowest product of 2, highest number, and lowest number to calculate the highest product of 3 at each step."

3. **Justify the approach:** "At each step, the new highest product of 3 comes from either the old highest, or the current number times the highest/lowest product of 2."

4. **Confirm complexity:** "This is O(n) time because one pass, and O(1) space because we only track 5 variables."

### What Interviewers Want to Hear

✓ "Two negative numbers create a positive product"
✓ "I need to track highest/lowest products of 2 numbers"
✓ "Order of updates matters to avoid multiplying by itself"
✓ "Time: O(n), Space: O(1)"

### What NOT to Say

✗ "I'll just take the three largest numbers"
✗ "Negative numbers don't matter"
✗ "I can update variables in any order"
✗ "I'll sort the array" (that's O(n log n))

---

## Bonus Questions

### Bonus 1: Highest Product of 4

```python
def highest_product_of_4(list_of_ints):
    if len(list_of_ints) < 4:
        raise ValueError('Need at least 4 integers')

    # Track highest/lowest products of 3 and 2 and 1
    # Similar pattern extended
    # At each step: current * highest_product_of_3, etc.
    pass
```

**Time:** O(n), **Space:** O(1)

### Bonus 2: Highest Product of K

```python
def highest_product_of_k(list_of_ints, k):
    # Generalize: track highest/lowest products of k-1, k-2, ..., 1
    # But this becomes complex for large k
    # Might want DP for k > 3
    pass
```

### Bonus 3: Handle Overflow

```python
def highest_product_of_3_safe(list_of_ints, max_value=10**18):
    # Check before multiplying if result would overflow
    # Or use logarithms to compare products
    # log(a*b*c) = log(a) + log(b) + log(c)
    pass
```

---

## Test Cases

```python
def test_highest_product_of_3():
    # Test 1: Basic positive
    assert highest_product_of_3([1, 10, 2, 3, 4]) == 120

    # Test 2: Negative numbers (key test!)
    assert highest_product_of_3([-10, -10, 1, 3, 2]) == 300

    # Test 3: All negatives
    assert highest_product_of_3([-5, -3, -1]) == -15

    # Test 4: Minimum size
    assert highest_product_of_3([1, 2, 3]) == 6

    # Test 5: With zero
    assert highest_product_of_3([0, 1, 2, 3]) == 6

    # Test 6: Single large positive
    assert highest_product_of_3([-5, -4, 0, 1, 100]) == 2000

    # Test 7: All same positive
    assert highest_product_of_3([5, 5, 5]) == 125

    # Test 8: All same negative
    assert highest_product_of_3([-5, -5, -5]) == -125

    # Test 9: Mixed
    assert highest_product_of_3([-10, -10, 1, 3, 2]) == 300

    # Test 10: Edge case
    assert highest_product_of_3([1, -5, -10, 0, 5, 20]) == 1000  # 20 * (-10) * (-5)

    # Test 11: Error case
    try:
        highest_product_of_3([1, 2])
        assert False, "Should raise error"
    except ValueError:
        pass

    print("All tests passed!")

# Run tests
test_highest_product_of_3()
```

---

## Summary

| Aspect | Details |
|--------|---------|
| **Problem** | Find highest product of any 3 integers |
| **Key Insight** | Two negatives make a positive |
| **Must Track** | Highest/lowest products of 2, highest/lowest singles |
| **Algorithm Type** | Greedy |
| **Time Complexity** | O(n) |
| **Space Complexity** | O(1) |
| **Order Matters** | Update product of 3 before product of 2, singles after |

---

## What We Learned

This is another great example of greedy algorithms because:

1. **Local optimization:** At each step, we calculate the best product using current number
2. **State tracking:** We track exactly what we need (products of 2, individual numbers)
3. **One pass:** No need for sorting or multiple passes
4. **Handling negatives:** Understanding that negative products matter

The key difference from Apple Stocks: we need to track more state (5 variables instead of 2) because the relationship is more complex.

This teaches the "track what you need" principle: instead of trying to remember all combinations, track the products and numbers that matter for future decisions.

---

## Next Steps

You now understand:
- How greedy works for product maximization
- Why multiple tracking variables are needed
- How to handle negative numbers in products
- Order of updates and why it matters

Ready to tackle more greedy problems!

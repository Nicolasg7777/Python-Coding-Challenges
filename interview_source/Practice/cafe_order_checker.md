# Cafe Order Checker

## Problem Statement

Your cake shop is so popular, you're adding tables and hiring wait staff so customers can have a sit-down cake-eating experience.

You have two registers:
- One for **take-out orders**
- One for **dine-in orders**

All customer orders get combined into one list for the kitchen, where they should be handled **first-come, first-served**.

Recently, some customers have complained that people who placed orders after them are getting their food first. You need to investigate!

You recorded three things one afternoon:
- **take_out_orders** - Orders entered into the system in sequence
- **dine_in_orders** - Orders entered into the system in sequence
- **served_orders** - Each customer order as it was finished by the kitchen

Write a function to check that your service is truly **first-come, first-served**. All food should come out in the same order customers requested it.

### Key Insight

For the service to be first-come-first-served, each order in `served_orders` must be the next order from either `take_out_orders` or `dine_in_orders` (whichever is at the front of its respective queue).

---

## Examples

### Example 1: NOT First-Come-First-Served

```python
take_out_orders = [1, 3, 5]
dine_in_orders = [2, 4, 6]
served_orders = [1, 2, 4, 6, 5, 3]

# Order 3 was requested before order 5, but 5 was served first!
# Result: False
```

**Why it fails:**
- 1 ✓ (first in take_out)
- 2 ✓ (first in dine_in)
- 4 ✓ (next in dine_in)
- 6 ✓ (next in dine_in)
- 5 ✗ (order 3 should be next from take_out, not 5!)

### Example 2: First-Come-First-Served

```python
take_out_orders = [17, 8, 24]
dine_in_orders = [12, 19, 2]
served_orders = [17, 8, 12, 19, 24, 2]

# Result: True
```

**Why it works:**
- 17 ✓ (first in take_out)
- 8 ✓ (next in take_out)
- 12 ✓ (first in dine_in)
- 19 ✓ (next in dine_in)
- 24 ✓ (next in take_out)
- 2 ✓ (next in dine_in)

---

## Gotchas

### Gotcha 1: Index Out of Bounds
Watch out! Your function might try to access the 0th item from an empty list, or the nth item when the list has only n elements.

### Gotcha 2: Hidden Space Costs
We can do this in **O(n) time** and **O(1) additional space**.

But if you write a recursive solution, be careful! You'll incur **hidden O(n) space** in the call stack.

### Gotcha 3: Array Slicing Costs
Every time you slice a list (like `take_out_orders[1:]`), you pay O(m) time and space, where m is the size of the resulting list!

---

## Approach: Evolution of Solutions

### Solution 1: Recursive with Slicing (O(n²) Time & Space - BAD)

Let's start with a simple recursive approach:

```python
def is_first_come_first_served_v1(take_out_orders, dine_in_orders, served_orders):
    # Base case: we've checked all served orders
    if len(served_orders) == 0:
        return True

    # Check if first served order matches take_out
    if (len(take_out_orders) and
        take_out_orders[0] == served_orders[0]):
        # Slice off the first element and recurse
        return is_first_come_first_served_v1(
            take_out_orders[1:],  # ← O(n) slicing!
            dine_in_orders,
            served_orders[1:]      # ← O(n) slicing!
        )

    # Check if first served order matches dine_in
    elif (len(dine_in_orders) and
          dine_in_orders[0] == served_orders[0]):
        # Slice off the first element and recurse
        return is_first_come_first_served_v1(
            take_out_orders,
            dine_in_orders[1:],    # ← O(n) slicing!
            served_orders[1:]      # ← O(n) slicing!
        )

    # Order doesn't match either register
    else:
        return False
```

**Problem:** Each slice costs O(n), and we do this n times → **O(n²) time and space**!

Plus the call stack adds another **O(n) space** overhead.

### Solution 2: Recursive with Indices (O(n) Time, O(n) Space - BETTER)

Instead of slicing, use indices:

```python
def is_first_come_first_served_v2(
    take_out_orders, dine_in_orders, served_orders,
    take_out_orders_index=0, dine_in_orders_index=0,
    served_orders_index=0
):
    # Base case: we've checked all served orders
    if served_orders_index == len(served_orders):
        return True

    current_order = served_orders[served_orders_index]

    # Check if current served order matches take_out
    if ((take_out_orders_index < len(take_out_orders)) and
        current_order == take_out_orders[take_out_orders_index]):
        take_out_orders_index += 1

    # Check if current served order matches dine_in
    elif ((dine_in_orders_index < len(dine_in_orders)) and
          current_order == dine_in_orders[dine_in_orders_index]):
        dine_in_orders_index += 1

    # Order doesn't match either register
    else:
        return False

    # Recurse to check next order
    served_orders_index += 1
    return is_first_come_first_served_v2(
        take_out_orders, dine_in_orders, served_orders,
        take_out_orders_index, dine_in_orders_index,
        served_orders_index
    )
```

**Better:** O(n) time, but still **O(n) space from the call stack**.

### Solution 3: Iterative (O(n) Time, O(1) Space - BEST)

Convert to an iterative approach:

```python
def is_first_come_first_served(take_out_orders, dine_in_orders, served_orders):
    take_out_orders_index = 0
    dine_in_orders_index = 0

    for order in served_orders:
        # Check if current order matches take_out
        if (take_out_orders_index < len(take_out_orders) and
            order == take_out_orders[take_out_orders_index]):
            take_out_orders_index += 1

        # Check if current order matches dine_in
        elif (dine_in_orders_index < len(dine_in_orders) and
              order == dine_in_orders[dine_in_orders_index]):
            dine_in_orders_index += 1

        # Order doesn't match either register
        else:
            return False

    # Verify all orders were served (no leftover orders)
    if (take_out_orders_index != len(take_out_orders) or
        dine_in_orders_index != len(dine_in_orders)):
        return False

    # All served orders matched! ✓
    return True
```

**Optimal:** **O(n) time and O(1) space**!

---

## How It Works: Step-by-Step

**Input:**
```python
take_out_orders = [17, 8, 24]
dine_in_orders = [12, 19, 2]
served_orders = [17, 8, 12, 19, 24, 2]
```

**Execution:**

```
Initial state:
  take_out_index = 0, dine_in_index = 0

Order 17: matches take_out[0] ✓
  take_out_index = 1

Order 8: matches take_out[1] ✓
  take_out_index = 2

Order 12: matches dine_in[0] ✓
  dine_in_index = 1

Order 19: matches dine_in[1] ✓
  dine_in_index = 2

Order 24: matches take_out[2] ✓
  take_out_index = 3

Order 2: matches dine_in[2] ✓
  dine_in_index = 3

Check: take_out_index == len(take_out) ✓
Check: dine_in_index == len(dine_in) ✓

Result: True ✓
```

---

## Edge Cases

### Edge Case 1: Empty Served Orders
```python
is_first_come_first_served([], [], [])
# Result: True (no orders to check)
```

### Edge Case 2: One Register Empty
```python
take_out_orders = [1, 2, 3]
dine_in_orders = []
served_orders = [1, 2, 3]
# Result: True (all orders from take_out)
```

### Edge Case 3: Unserved Orders
```python
take_out_orders = [1, 2, 3]
dine_in_orders = [4]
served_orders = [1, 2, 3]
# Result: False (order 4 was never served!)
```

### Edge Case 4: Extra Orders in Served
```python
take_out_orders = [1, 2]
dine_in_orders = []
served_orders = [1, 2, 3]
# Result: False (order 3 doesn't match any register)
```

---

## Complexity Analysis

### Time Complexity: O(n)

- We iterate through `served_orders` once: O(n)
- Each iteration does constant work (comparisons, index increments)
- We check indices once at the end: O(1)
- Total: O(n)

### Space Complexity: O(1)

- We only use a constant number of variables:
  - `take_out_orders_index`
  - `dine_in_orders_index`
- No additional data structures
- No recursive call stack
- Total: O(1) additional space

---

## Common Mistakes

### Mistake 1: Forgetting to Check Leftover Orders
```python
# WRONG: doesn't check if all orders were served
for order in served_orders:
    # ... matching logic ...
return True  # What if there are unserved orders?

# CORRECT
if (take_out_orders_index != len(take_out_orders) or
    dine_in_orders_index != len(dine_in_orders)):
    return False
return True
```

### Mistake 2: Not Checking Index Bounds
```python
# WRONG: crashes if we're out of bounds
if order == take_out_orders[take_out_orders_index]:

# CORRECT
if (take_out_orders_index < len(take_out_orders) and
    order == take_out_orders[take_out_orders_index]):
```

### Mistake 3: Using Slicing in Recursion
```python
# WRONG: O(n²) time and space!
return is_first_come_first_served(
    take_out_orders[1:],  # Slicing costs O(n)!
    dine_in_orders,
    served_orders[1:]     # Slicing costs O(n)!
)

# CORRECT: use indices instead
take_out_orders_index += 1
```

### Mistake 4: Forgetting Index Checks in If Conditions
```python
# WRONG: will crash with IndexError
if take_out_orders[take_out_orders_index] == order:

# CORRECT: check bounds FIRST
if (take_out_orders_index < len(take_out_orders) and
    take_out_orders[take_out_orders_index] == order):
```

---

## Real-World Applications

This pattern is used in:
1. **Order management systems** - Validating order fulfillment
2. **Task scheduling** - Checking job execution order
3. **Stream validation** - Verifying data sequence integrity
4. **Transaction audit trails** - Ensuring operations happened in order
5. **Event processing** - Validating event sequences

---

## Bonus Questions

### Bonus 1: Handle Duplicate Order Numbers
What if order numbers could repeat? How would you adapt the solution?

```python
def is_first_come_first_served_with_duplicates(
    take_out_orders, dine_in_orders, served_orders
):
    # Challenge: handle duplicate order IDs
    pass
```

**Hint:** You might need to count occurrences instead of just checking equality...

### Bonus 2: Better Error Reporting
Instead of just returning True/False, return information about what went wrong:

```python
def check_orders_with_details(
    take_out_orders, dine_in_orders, served_orders
):
    # Returns: (is_valid, error_message, first_bad_order)
    pass
```

### Bonus 3: Reverse Traversal
Would the algorithm work if we iterated from the back towards the front? Which approach is cleaner?

```python
def is_first_come_first_served_reverse(
    take_out_orders, dine_in_orders, served_orders
):
    # Start from the end of served_orders
    pass
```

---

## Testing Your Solution

```python
def test_cafe_order_checker():
    # Example 1: NOT first-come-first-served
    assert not is_first_come_first_served(
        [1, 3, 5],
        [2, 4, 6],
        [1, 2, 4, 6, 5, 3]
    )

    # Example 2: First-come-first-served
    assert is_first_come_first_served(
        [17, 8, 24],
        [12, 19, 2],
        [17, 8, 12, 19, 24, 2]
    )

    # Empty orders
    assert is_first_come_first_served([], [], [])

    # One register empty
    assert is_first_come_first_served([1, 2, 3], [], [1, 2, 3])
    assert is_first_come_first_served([], [1, 2, 3], [1, 2, 3])

    # Unserved orders
    assert not is_first_come_first_served(
        [1, 2, 3],
        [4],
        [1, 2, 3]
    )

    # Extra orders in served
    assert not is_first_come_first_served(
        [1, 2],
        [],
        [1, 2, 3]
    )

    # Single order each
    assert is_first_come_first_served([1], [2], [1, 2])
    assert is_first_come_first_served([1], [2], [2, 1])

    # Different lengths
    assert is_first_come_first_served(
        [1, 2, 3, 4],
        [5],
        [1, 5, 2, 3, 4]
    )

    print("All tests passed!")

test_cafe_order_checker()
```

---

## Key Insights

1. **Recognize the pattern** - This is fundamentally checking if two input streams merge into an output stream
2. **Use multiple pointers** - Track position in multiple sequences simultaneously
3. **Avoid hidden costs** - Recursive solutions and slicing can hide O(n²) behavior
4. **Think about space** - Call stacks add space overhead you might not notice
5. **Handle edge cases** - Unserved orders, empty lists, index bounds

---

## Interview Tips

### What Interviewers Care About
- ✓ Recognizing this is a sequence validation problem
- ✓ Handling edge cases (unserved orders, bounds checking)
- ✓ Understanding hidden space costs in recursion
- ✓ Evolving from naive to optimal solution
- ✓ Explaining the algorithm clearly

### How to Explain Your Solution

1. **Start simple** - "Each served order should match the next order from one register"
2. **Identify the pattern** - "I'll track my position in each register"
3. **Walk through example** - Show how you match 1, 2, 4, 6...
4. **Address edge cases** - "What if some orders weren't served?"
5. **Discuss complexity** - "O(n) time, O(1) space"
6. **Mention optimizations** - "We could use recursion, but that adds stack overhead"

### Common Interview Questions
- "What if some orders weren't served?"
- "Can you handle duplicate order numbers?"
- "How would you optimize this?"
- "What about linked lists instead of arrays?"
- "Would a recursive solution work?"


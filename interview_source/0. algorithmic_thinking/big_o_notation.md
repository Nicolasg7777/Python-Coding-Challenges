# Big O Notation
## Using Not-Boring Math to Measure Code's Efficiency

---

## What is Big O Notation?

Big O notation is the language we use for talking about how long an algorithm takes to run. It's how we compare the efficiency of different approaches to a problem.

It's like math except it's an awesome, not-boring kind of math where you get to wave your hands through the details and just focus on what's basically happening.

With big O notation we express the runtime in terms of **how quickly it grows relative to the input, as the input gets arbitrarily large.**

Let's break that down:

### 1. How quickly the runtime grows
It's hard to pin down the exact runtime of an algorithm. It depends on:
- The speed of the processor
- What else the computer is running
- Other environmental factors

Instead of talking about the runtime directly, we use big O notation to talk about **how quickly the runtime grows**.

### 2. Relative to the input
We express our speed in terms of the **size of the input**, which we call **"n"**.

Examples:
- **O(n)** - Runtime grows on the order of the size of the input
- **O(n²)** - Runtime grows on the order of the square of the size of the input
- **O(1)** - Runtime doesn't grow with input (constant time)

### 3. As the input gets arbitrarily large
Our algorithm may have steps that seem expensive when n is small but are eclipsed eventually by other steps as n gets huge.

**We care most about the stuff that grows fastest as the input grows**, because everything else is quickly eclipsed as n gets very large.

---

## Common Big O Complexities

| Notation | Name | What It Means |
|----------|------|---------------|
| O(1) | Constant Time | Runtime doesn't change regardless of input size |
| O(log n) | Logarithmic | Runtime grows very slowly (like binary search) |
| O(n) | Linear Time | Runtime grows proportionally with input size |
| O(n log n) | Linearithmic | A bit slower than linear (like merge sort) |
| O(n²) | Quadratic | Runtime grows with the square of input size |
| O(n³) | Cubic | Runtime grows with the cube of input size |
| O(2ⁿ) | Exponential | Runtime doubles with each additional input |
| O(n!) | Factorial | Runtime is astronomically large |

---

## Examples

### Example 1: O(1) - Constant Time

```python
def print_first_item(items):
    print(items[0])
```

This function runs in **O(1)** time (or "constant time") relative to its input.

The input list could be 1 item or 1,000,000 items, but this function would still just require one "step."

### Example 2: O(n) - Linear Time

```python
def print_all_items(items):
    for item in items:
        print(item)
```

This function runs in **O(n)** time (or "linear time"), where n is the number of items in the list.

- If the list has 10 items → we print 10 times
- If the list has 1,000 items → we print 1,000 times
- Runtime grows directly with input size

### Example 3: O(n²) - Quadratic Time

```python
def print_all_possible_ordered_pairs(items):
    for first_item in items:
        for second_item in items:
            print(first_item, second_item)
```

Here we're nesting two loops. If our list has n items:
- Our outer loop runs **n** times
- Our inner loop runs **n** times for each iteration of the outer loop
- Total = **n × n = n²** operations

Thus this function runs in **O(n²)** time (or "quadratic time").

- If the list has 10 items → we print 100 times
- If the list has 1,000 items → we print 1,000,000 times

---

## Rules for Big O Analysis

### Rule 1: n can be different things

Sometimes n is an actual number input to the function. Other times n is the size of an input collection.

```python
# Here n is a number
def say_hi_n_times(n):
    for time in range(n):
        print("hi")

# Here n is the size of the list
def print_all_items(items):
    for item in items:
        print(item)
```

Both are **O(n)** but n means different things!

### Rule 2: Drop the Constants

When calculating big O complexity, **throw out the constants**.

The reasoning: As n gets arbitrarily large, constants become insignificant.

#### Example 1: Multiple loops
```python
def print_all_items_twice(items):
    # Loop 1
    for item in items:
        print(item)

    # Loop 2
    for item in items:
        print(item)
```

This is **O(2n)**, but we simplify to **O(n)**

#### Example 2: Mixed operations
```python
def print_first_item_then_first_half_then_say_hi_100_times(items):
    # This is O(1)
    print(items[0])

    # This is O(n/2)
    middle_index = len(items) / 2
    index = 0
    while index < middle_index:
        print(items[index])
        index += 1

    # This is O(100)
    for time in range(100):
        print("hi")
```

This is **O(1 + n/2 + 100)**, but we simplify to **O(n)**

### Rule 3: Drop Less Significant Terms

When you have multiple terms, keep only the most significant one.

```python
def print_all_numbers_then_all_pair_sums(numbers):
    # This part is O(n)
    print("these are the numbers:")
    for number in numbers:
        print(number)

    # This part is O(n²)
    print("and these are their sums:")
    for first_number in numbers:
        for second_number in numbers:
            print(first_number + second_number)
```

Runtime is **O(n + n²)**, but since n² dominates as n grows, we simplify to **O(n²)**

More examples:
- **O(n³ + 50n² + 10000)** → **O(n³)**
- **O((n+30) × (n+5))** → **O(n²)** (when expanded: n² + 35n + 150)

---

## Best, Worst, and Average Case

Often we talk about the "worst case" runtime (and this stipulation is usually implied).

### Example: Linear Search

```python
def contains(haystack, needle):
    # Does the haystack contain the needle?
    for item in haystack:
        if item == needle:
            return True
    return False
```

- **Best case**: O(1) - The needle is the first item
- **Worst case**: O(n) - The needle is the last item or not present
- **Average case**: O(n/2) → simplified to O(n)

When we say this is "O(n)", we're usually referring to the worst case.

---

## Space Complexity: The Other Dimension

Sometimes we want to optimize for using less memory instead of (or in addition to) using less time.

**Space complexity** is calculated the same way as time complexity—we look at how much additional memory we're allocating relative to the input size.

### Example 1: O(1) Space - Fixed Variables

```python
def say_hi_n_times(n):
    for time in range(n):
        print("hi")
```

This uses a fixed number of variables (doesn't matter how large n is). **O(1) space**

### Example 2: O(n) Space - Growing Data Structure

```python
def list_of_hi_n_times(n):
    hi_list = []
    for time in range(n):
        hi_list.append("hi")
    return hi_list
```

The size of `hi_list` scales with the input. **O(n) space**

### Example 3: O(1) Space - Don't Count Input

```python
def get_largest_item(items):
    largest = float('-inf')
    for item in items:
        if item > largest:
            largest = item
    return largest
```

Even though the input has n items, we only allocate one additional variable (`largest`). **O(1) space** (we don't count space taken by inputs)

---

## Space vs Time Tradeoff

Sometimes there's a tradeoff between saving time and saving space. You have to decide which one you're optimizing for.

For example:
- **Caching** saves time but uses more space
- **Streaming** saves space but might take more time

---

## When Big O Matters (and When It Doesn't)

### Big O is Powerful When:
- Comparing fundamentally different approaches
- Identifying potential bottlenecks
- Working with large datasets
- Building scalable systems

### Big O Limitations:
- **Big O ignores constants**: An O(n) algorithm taking 5 hours vs 1 hour still makes a difference
- **Premature optimization is bad**: Sometimes readability and development speed matter more than perfect efficiency
- **Real-world factors matter**: Cache behavior, memory access patterns, etc.

---

## Key Takeaways

1. **Big O describes how runtime grows with input size**
2. **Drop constants and less significant terms**
3. **Focus on worst case unless otherwise stated**
4. **Consider both time and space complexity**
5. **Balance efficiency with readability and development speed**
6. **Asymptotic analysis is powerful but apply it wisely**

---

## Practice: Identify the Big O

For each function, determine the time complexity:

1. **Function A**
```python
def find_max(numbers):
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num
```

2. **Function B**
```python
def has_duplicates(items):
    for i in range(len(items)):
        for j in range(i + 1, len(items)):
            if items[i] == items[j]:
                return True
    return False
```

3. **Function C**
```python
def binary_search(sorted_list, target):
    left = 0
    right = len(sorted_list) - 1
    while left <= right:
        mid = (left + right) // 2
        if sorted_list[mid] == target:
            return True
        elif sorted_list[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return False
```

**Answers:**
- Function A: **O(n)** - Single loop through all items
- Function B: **O(n²)** - Nested loops checking all pairs
- Function C: **O(log n)** - Binary search eliminates half the search space each iteration

---

## Resources

- [Interview Cake - Big O Notation](https://www.interviewcake.com/article/python/big-o-notation)
- [GeeksforGeeks - Big O Notation](https://www.geeksforgeeks.org/analysis-of-algorithms-set-1-asymptotic-analysis/)
- [Big O Cheat Sheet](https://www.bigocheatsheet.com/)

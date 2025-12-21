# In-Place Algorithm

## Overview

An **in-place function** modifies data structures or objects outside of its own stack frame (i.e.: stored on the process heap or in the stack frame of a calling function).

Because of this, the changes made by the function remain after the call completes.

In-place algorithms are sometimes called **destructive**, since the original input is "destroyed" (or modified) during the function call.

---

## Important Clarification

**"In-place" does NOT mean "without creating any additional variables!"**

Rather, it means **"without creating a new copy of the input."**

In general, an in-place function will only create additional variables that are **O(1) space**.

### Comparison: In-Place vs Out-of-Place

**In-place**: Modify the original data structure directly
```python
def square_list_in_place(int_list):
    for index, element in enumerate(int_list):
        int_list[index] *= element

    # NOTE: no need to return anything - we modified
    # int_list in place
```

**Out-of-place**: Create a new copy and return it
```python
def square_list_out_of_place(int_list):
    # We allocate a new list with the length of the input list
    squared_list = [None] * len(int_list)

    for index, element in enumerate(int_list):
        squared_list[index] = element ** 2

    return squared_list
```

---

## How Values Are Passed

Different languages handle this differently, which affects what "in-place" means:

### Primitive Types vs Complex Data Structures

- **Primitive values** (integers, floating point numbers, characters) are **copied** when passed as arguments
- **Complex data structures** (lists, arrays, heaps, hash tables) are **passed by reference**

This is what Python does:

```python
# Primitive: copied
def modify_int(num):
    num = 100

x = 5
modify_int(x)
print(x)  # Still 5 - the original wasn't modified

# Complex: passed by reference
def modify_list(arr):
    arr[0] = 100

numbers = [1, 2, 3]
modify_list(numbers)
print(numbers)  # [100, 2, 3] - the original WAS modified
```

---

## Space Complexity

### In-Place Advantage
Working in-place is a good way to **save time and space**.

An in-place algorithm:
- Avoids the cost of initializing new data structures
- Avoids the cost of copying data
- Usually has **O(1) space cost**

### Comparison
```python
# In-place: O(1) space
def square_in_place(arr):
    for i in range(len(arr)):
        arr[i] *= arr[i]

# Out-of-place: O(n) space
def square_out_of_place(arr):
    result = [0] * len(arr)
    for i in range(len(arr)):
        result[i] = arr[i] ** 2
    return result
```

---

## The Side Effects Problem

Be careful: **an in-place algorithm can cause side effects.**

Your input is "destroyed" or "altered," which can affect code outside of your function.

### Example: Unexpected Behavior
```python
original_list = [2, 3, 4, 5]
square_list_in_place(original_list)

print("original list: %s" % original_list)
# Prints: original list: [4, 9, 16, 25], confusingly!
```

The caller didn't expect their original list to be modified! This is a **side effect**.

### Example: More Serious Problem
```python
def process_data(data):
    # Modifies data in-place
    for i in range(len(data)):
        data[i] = transform(data[i])
    return sum(data)

user_data = [1, 2, 3, 4, 5]
result = process_data(user_data)

# Later in the program...
print(user_data)  # [transformed values], not the original!
# Debugging nightmare - you don't expect your input to change
```

---

## Safety vs Efficiency Tradeoff

### Out-of-Place (Safer)
```python
def square_list_out_of_place(int_list):
    squared_list = [None] * len(int_list)
    for index, element in enumerate(int_list):
        squared_list[index] = element ** 2
    return squared_list
```

**Pros:**
- Original input is preserved
- No side effects
- Easier to debug
- Safer for multi-threaded code

**Cons:**
- Uses O(n) extra space
- Slower due to allocation and copying

### In-Place (More Efficient)
```python
def square_list_in_place(int_list):
    for index, element in enumerate(int_list):
        int_list[index] *= element
```

**Pros:**
- Uses O(1) extra space
- Faster (no allocation or copying)

**Cons:**
- Original input is destroyed
- Can cause confusing side effects
- Harder to debug

---

## When to Use In-Place Algorithms

### Use In-Place When:
1. **Space is constrained** - You're in an embedded system or have strict memory limits
2. **You're positive you don't need the original input anymore** - You're completely done with it, even for debugging
3. **The caller expects it** - The function's contract is clear that it modifies in-place
4. **Performance is critical** - And profiling shows the allocation/copying is a bottleneck

### Use Out-of-Place When:
1. **Space isn't a concern** - Most modern systems have plenty of memory
2. **Clarity matters** - Your code is easier to understand and debug
3. **Side effects are dangerous** - Multi-threaded code, complex workflows
4. **You might need the original** - Even just for testing or debugging

---

## Interview Context

In coding interviews:

### In-Place Advantages
- Shows you understand memory allocation
- Demonstrates space optimization
- Many interview questions specifically ask for in-place solutions

### In-Place Challenges
- Can be trickier to implement correctly
- More opportunity for bugs
- Harder to debug with in-place modifications

### Best Practice
- If the problem **specifically asks for in-place**, do it that way
- If not specified, ask the interviewer: **"Should I modify the input or return a new array?"**
- This shows you understand the tradeoff

---

## Key Insight

The choice between in-place and out-of-place is fundamentally a tradeoff:

**In-place = Fast + Compact but Destructive**
**Out-of-place = Safe + Clear but Wasteful**

Choose based on your constraints and requirements. In interviews, when it's not specified, **safer is usually better** — unless the problem explicitly asks for in-place optimization.

---

## Common In-Place Patterns

### Pattern 1: Modify Array in-place
```python
def reverse_array_in_place(arr):
    left = 0
    right = len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    # No return needed - arr is modified
```

### Pattern 2: Remove elements in-place
```python
def remove_duplicates_in_place(arr):
    write_index = 0
    for read_index in range(1, len(arr)):
        if arr[read_index] != arr[write_index]:
            write_index += 1
            arr[write_index] = arr[read_index]
    return write_index + 1
```

### Pattern 3: Partition in-place
```python
def partition_in_place(arr, pivot):
    left = 0
    right = len(arr) - 1
    while left < right:
        while arr[left] < pivot:
            left += 1
        while arr[right] >= pivot:
            right -= 1
        if left < right:
            arr[left], arr[right] = arr[right], arr[left]
```

These patterns show how to modify data efficiently without extra space.


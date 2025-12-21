# Dynamic Array

## Overview

A **dynamic array** is an array with a big improvement: **automatic resizing**.

One limitation of arrays is that they're fixed size—you need to specify the number of elements your array will hold ahead of time.

A dynamic array expands as you add more elements. So you don't need to determine the size ahead of time.

**Other names:** Array list, growable array, resizable array, mutable array

---

## Quick Reference: Big O Complexity

| Operation | Average Case | Worst Case |
|-----------|--------------|-----------|
| Space     | O(n)         | O(n)      |
| Lookup    | O(1)         | O(1)      |
| Append    | O(1)         | O(n)      |
| Insert    | O(n)         | O(n)      |
| Delete    | O(n)         | O(n)      |

---

## Strengths

### Fast Lookups
Just like arrays, retrieving the element at a given index takes **O(1)** time.

You still get the instant address calculation:
```
address = start_address + (index × size)
```

### Variable Size
You can add as many items as you want, and the dynamic array will expand to hold them.

No need to guess the size ahead of time!

### Cache-Friendly
Just like arrays, dynamic arrays place items right next to each other in memory, making efficient use of caches.

Accessing sequential items is fast because they're already in the cache.

---

## Weaknesses

### Slow Worst-Case Appends
Usually, adding a new element at the end takes **O(1)** time.

But if the dynamic array doesn't have any room for the new item, it has to expand, which takes **O(n)** time.

### Costly Inserts and Deletes
Just like arrays, elements are stored adjacent to each other.

Adding or removing an item in the middle requires "scooting over" other elements, which takes **O(n)** time.

---

## How Dynamic Arrays Work

### Python Example

In Python, dynamic arrays are called **lists**:

```python
gas_prices = []

gas_prices.append(346)
gas_prices.append(360)
gas_prices.append(354)
```

It looks simple, but there's a lot happening under the hood!

---

## Size vs Capacity

### Understanding the Difference

When you allocate a dynamic array, the implementation creates an underlying **fixed-size array**.

The starting size depends on the implementation. Let's say our implementation starts with capacity 10.

Now say we append 4 items. At this point:
- **Size**: 4 (number of elements actually in the array)
- **Capacity**: 10 (total space allocated)

The dynamic array tracks an **end_index** to know where the actual data ends and the extra capacity begins:

```
Index:    0  1  2  3  4  5  6  7  8  9
Value:   [A][B][C][D][_][_][_][_][_][_]
         └─────────┘  └────────────────┘
            Size=4        Capacity=6
                    end_index
```

### Why Track Both?

We need to know:
1. **Where the data ends** (size) - for iteration and access
2. **How much space we have available** (capacity) - for knowing when to expand

---

## Doubling: The Expansion Strategy

### What Happens When We Run Out of Space?

When we try to append but capacity is full, the dynamic array creates a **new, bigger underlying array**, usually **twice as big**.

Why twice the size? Because:
1. **Doubling is efficient** - gives you lots of room for the next appends
2. **Memory continuity** - the old memory might be taken by another program, so we can't just extend it

### The Process

1. Create a new array with 2× the capacity
2. Copy every element from the old array to the new array
3. Free the old array
4. Continue with the new array

```
Old array (capacity 10, full):
[A][B][C][D][E][F][G][H][I][J]

Create new array (capacity 20):
[A][B][C][D][E][F][G][H][I][J][_][_][_][_][_][_][_][_][_][_]

Now append K:
[A][B][C][D][E][F][G][H][I][J][K][_][_][_][_][_][_][_][_][_]
```

---

## The Cost of Doubling

### Copying Takes O(n) Time

When we double, we have to copy every element:

```python
# When doubling happens, this is O(n)
for i in range(len(old_array)):
    new_array[i] = old_array[i]
```

This costs **O(n) time**, where n is the size of the array.

### Worst Case: O(n) Append

So if you append when the array is full, that append costs **O(n)** time!

```python
# Usually O(1), but sometimes O(n)
my_list.append(new_item)
```

### Best Case: O(1) Append

But most of the time, appending just places the item in the next available slot, which is **O(1)**.

---

## Amortized Cost: The Key Insight

Here's the clever part: even though some appends are O(n), we can say **appends are O(1) on average**.

### Why?

The cost of doubling and the frequency of doubling balance out:

**As the array grows:**
- Doubling cost = O(n) to copy n elements
- But after doubling, you can append n more times before doubling again

So:
- One expensive O(n) doubling
- Followed by n cheap O(1) appends
- Average cost = O(n) ÷ n = O(1) per append

### Example with Numbers

```
Append 1:     Capacity 1, Double! Copy 0 items → O(1) + O(0)
Appends 2:    Capacity 2, no double → O(1)
Append 3:     Capacity 2, Double! Copy 2 items → O(1) + O(2)
Appends 4-7:  Capacity 4, no double → O(1) × 4
Append 8:     Capacity 4, Double! Copy 4 items → O(1) + O(4)
Appends 9-15: Capacity 8, no double → O(1) × 8
```

Total work for 15 appends: 15 + (0 + 2 + 4) = 15 + 6 = 21 operations

Average per append: 21 ÷ 15 ≈ 1.4 = O(1)

### Industry Standard

Given this, in industry we say dynamic arrays have **O(1) amortized cost** for appends, even though strictly speaking the worst-case single append is O(n).

In interviews, unless specifically asked about worst case, you can say appends are **O(1)**.

---

## Doubling Factor

### Why Double?

Why not just add 1 more slot each time?
- Adding 1 slot: You'd double every append, making every append O(n)
- Doubling: You can append 2× more items before doubling again

### Why Not Triple or Quadruple?

- **Doubling** is the sweet spot
  - Doubling: You get n free appends after doubling, costing O(n) to double
  - Tripling: You get 2n free appends after doubling, costing O(n) to triple
  - Tripling uses more wasted space
- **Doubling is standard** in most languages (Python, Java, C++, JavaScript)

---

## Dynamic Arrays in Different Languages

### Python
```python
# Python lists are dynamic arrays
my_list = []
my_list.append(1)      # O(1) amortized
my_list.append(2)      # O(1) amortized
my_list.append(3)      # O(1) amortized
```

### Java
```java
// Java ArrayList is a dynamic array
ArrayList<Integer> myList = new ArrayList<>();
myList.add(1);         // O(1) amortized
myList.add(2);         // O(1) amortized
myList.add(3);         // O(1) amortized
```

### JavaScript
```javascript
// JavaScript arrays are dynamic arrays
let myArray = [];
myArray.push(1);       // O(1) amortized
myArray.push(2);       // O(1) amortized
myArray.push(3);       // O(1) amortized
```

---

## When to Use Dynamic Arrays

### Use Dynamic Arrays When:
1. You don't know the size ahead of time
2. You need fast lookups by index
3. You need O(1) amortized appends
4. You care about cache locality

### Use Linked Lists Instead When:
1. You need O(1) prepends (dynamic arrays are O(n))
2. You frequently remove from the middle
3. You don't need random access by index

---

## Key Insight: The Amortized Tradeoff

Dynamic arrays make a clever tradeoff:
- **Most appends are O(1)** and very fast
- **Occasional appends are O(n)** and slow (when doubling happens)
- **On average, they're O(1)** (amortized)

This is better than:
- **Fixed arrays**: Can't append if full
- **Linked lists**: Every append is O(n) due to finding the end or maintaining tail

---

## Interview Implications

### What Interviewers Care About
1. **Understand amortized analysis** - Why appends are considered O(1)
2. **Know the worst case exists** - When doubling happens, it's O(n)
3. **Understand the strategy** - Why doubling (not adding 1)?
4. **Trade-off awareness** - Space wasted vs convenience

### Common Interview Questions
- "What's the time complexity of append?"
  - Answer: O(1) amortized, O(n) worst case
- "Why do we double instead of add 1?"
  - Answer: Doubling gives us n free appends before the next doubling
- "How much extra space is wasted?"
  - Answer: On average, ~50% of capacity is unused

---

## Terminology

Different languages use different names for the same concept:
- **Python**: `list`
- **Java**: `ArrayList`
- **JavaScript**: `Array`
- **C++**: `vector`
- **General term**: Dynamic array, growable array, resizable array

They all follow the same doubling strategy!


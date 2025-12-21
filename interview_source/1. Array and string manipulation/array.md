# Array

## Data Structure Overview

An array organizes items sequentially, one after another in memory.

Each position in the array has an index, starting at 0.

---

## Quick Reference: Big O Complexity

| Operation | Time Complexity |
|-----------|-----------------|
| Space     | O(n)            |
| Lookup    | O(1)            |
| Append    | O(1)            |
| Insert    | O(n)            |
| Delete    | O(n)            |

---

## Strengths

### Fast Lookups
Retrieving the element at a given index takes **O(1)** time, regardless of the length of the array.

The reason is simple: arrays store elements sequentially in memory. We can calculate the memory address of any element instantly:

```
address of element = address of array start + (index × size of each element)
```

### Fast Appends
Adding a new element at the end of the array takes **O(1)** time, if the array has space.

You simply write the new value to the next empty slot.

---

## Weaknesses

### Fixed Size
You need to specify how many elements you're going to store in your array ahead of time.

Languages like Java require you to declare array size:
```java
// instantiate an array that holds 10 integers
int gasPrices[] = new int[10];
```

(Unless you're using a dynamic array, which automatically resizes.)

### Costly Inserts and Deletes
You have to "scoot over" the other elements to fill in or close gaps, which takes worst-case **O(n)** time.

---

## How Insertions Work

If we want to insert something into an array, first we have to make space by "scooting over" everything starting at the index we're inserting into:

```
Before insertion:
Index: 0  1  2  3  4  5
Value: A  B  C  E  F  G

Insert D at index 3:
Index: 0  1  2  3  4  5  6
Value: A  B  C  D  E  F  G
                 ↑  ↑  ↑  ↑
              (shifted right)
```

**Worst case**: We're inserting into the 0th index (prepending), so we have to "scoot over" everything in the array. That's **O(n)** time.

---

## How Deletions Work

Array elements are stored adjacent to each other. So when we remove an element, we have to fill in the gap—"scooting over" all the elements that came after it:

```
Before deletion:
Index: 0  1  2  3  4  5  6
Value: A  B  C  Z  D  E  F

Delete Z at index 3:
Index: 0  1  2  3  4  5
Value: A  B  C  D  E  F
             ↑  ↑  ↑  ↑
          (shifted left)
```

**Worst case**: We're deleting the 0th item in the array, so we have to "scoot over" everything else in the array. That's **O(n)** time.

---

## Why We Can't Just Leave Gaps

You might wonder: why can't we just leave a gap where the deleted element was?

The answer: Because the **quick lookup power of arrays depends on everything being sequential and uninterrupted**.

If elements are contiguous in memory, we can predict exactly where any element is:
- Element at index 0: address 1000
- Element at index 1: address 1004 (assuming 4-byte integers)
- Element at index 138: address 1000 + (138 × 4) = 1552

If there are gaps, we can no longer predict exactly where each array item will be, and lookups would become slow.

---

## Code Example: Java Arrays

```java
// Declare and initialize an array
int gasPrices[] = new int[10];

// Add elements
gasPrices[0] = 346;
gasPrices[1] = 360;
gasPrices[2] = 354;

// Access element
int firstPrice = gasPrices[0];  // O(1) lookup

// Append (if space available)
gasPrices[3] = 372;  // O(1) append
```

---

## Data Structures Built on Arrays

Arrays are the building blocks for lots of other, more complex data structures:

- **Dynamic Arrays**: Add automatic resizing so you don't need to specify size ahead of time
- **Dictionaries/Hash Tables**: Look up items by something other than just an index
- **Heaps**: Use arrays with special ordering properties
- **Tries**: Use arrays to store multiple pointers

Understanding arrays deeply is essential, as many advanced data structures are built on top of them.

---

## Key Takeaway

Arrays are incredibly efficient for one operation: **fast lookups by index in O(1) time**.

This efficiency comes at a cost: insertions and deletions require moving elements around, which takes O(n) time.

Choose arrays when you need **fast lookups by index**. If you need fast insertions and deletions, consider other data structures like linked lists or dynamic arrays.


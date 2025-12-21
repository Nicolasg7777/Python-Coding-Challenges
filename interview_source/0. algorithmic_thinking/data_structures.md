# Data Structures
## Computer Science in Plain English

---

## Introduction

To really understand how data structures work, we're going to derive each of them from scratch. Starting with bits.

Don't worry—we'll skip the convoluted academic jargon and proofs. We'll build intuition instead.

---

## Table of Contents

1. Random Access Memory (RAM)
2. Binary Numbers
3. Fixed-Width Integers
4. Arrays
5. Strings
6. Pointers
7. Dynamic Arrays
8. Linked Lists
9. Hash Tables

---

## Random Access Memory (RAM)

When a computer is running code, it needs to keep track of variables (numbers, strings, arrays, etc.).

Variables are stored in **random access memory (RAM)**. We sometimes call RAM "working memory" or just "memory."

### RAM vs Storage

RAM is **not** where mp3s and apps get stored. Your computer has two types of storage:

- **Memory (RAM)**: Where variables are kept as functions crunch data. Faster but less space (~16GB on modern laptops)
- **Storage (Disk)**: Where files like mp3s, videos, and documents are kept. Slower but more space (~500GB on modern laptops)

### How RAM Works

Think of RAM like a really tall bookcase with billions of shelves.

The shelves are numbered—we call a shelf's number its **address**.

Each shelf holds **8 bits**. A bit is a tiny electrical switch that can be turned "on" or "off" (1 or 0).

**8 bits = 1 byte** (one shelf)

### The Memory Controller

A memory controller has a direct connection to each shelf of RAM. This means we can:
- Access address 0
- Then immediately access address 918,873
- Without having to "climb down" the bookshelf

This is why it's called **Random Access Memory (RAM)**—we can access any random address instantly.

### Cache

The processor has a **cache** where it stores recently read data from RAM. The cache is much faster to read from than RAM.

When the processor reads from a memory address, the memory controller also sends nearby addresses to the cache. So reading sequential addresses is faster than jumping around.

**Key Point:** Reading from sequential memory addresses is faster than jumping around.

---

## Binary Numbers

### Number Systems

The number system we usually use is **base 10** (decimal) because each digit has 10 possible values (0-9).

Computers use **base 2** (binary) because they have bits with 2 possible values (0 or 1).

### How Binary Works

Base 10 uses powers of 10:
- **10⁰ = 1** (ones place)
- **10¹ = 10** (tens place)
- **10² = 100** (hundreds place)

Base 2 uses powers of 2:
- **2⁰ = 1** (ones place)
- **2¹ = 2** (twos place)
- **2² = 4** (fours place)
- **2³ = 8** (eights place)

### Example: Binary 101

Reading "101" in binary (right to left):
- 1 in the ones place = 1
- 0 in the twos place = 0
- 1 in the fours place = 4
- **Total = 1 + 0 + 4 = 5**

### Counting in Binary

| Decimal | Binary |
|---------|--------|
| 0 | 0000 |
| 1 | 0001 |
| 2 | 0010 |
| 3 | 0011 |
| 4 | 0100 |
| 5 | 0101 |
| 6 | 0110 |
| 7 | 0111 |
| 8 | 1000 |
| 9 | 1001 |
| 10 | 1010 |
| 11 | 1011 |
| 12 | 1100 |

### Other Number Types

How we can store different types of numbers:

- **Fractions**: Store numerator and denominator as two separate numbers
- **Decimals**: Store the number without the decimal point, plus the decimal position
- **Negative Numbers**: Reserve the leftmost bit to express the sign (0 for positive, 1 for negative)

---

## Fixed-Width Integers

### How Many Numbers Can We Store?

With 1 byte (8 bits): **2⁸ = 256** different numbers

### Integer Overflow

What happens if we have 255 (1111 1111) in an 8-bit unsigned integer and add 1?

The answer (256) needs 9 bits (1 0000 0000). But we only have 8 bits!

This is called **integer overflow**. The computer might:
- Give you an error
- Throw out the 9th bit, giving you 0 instead of 256

(Python handles this by automatically allocating more bits)

### Common Integer Sizes

- **8-bit integers**: 2⁸ = 256 possibilities
- **32-bit integers**: 2³² = more than 4 billion possibilities
- **64-bit integers**: 2⁶⁴ = more than 10 billion billion possibilities

Different languages use different default sizes:
- Java: `int` is 32 bits, `long` is 64 bits
- SQL: `tinyint` (1 byte), `smallint` (2 bytes), `int` (4 bytes), `bigint` (8 bytes)

### Real World Example

YouTube had to upgrade from 32-bit to 64-bit integers when the Gangnam Style video exceeded 2³¹ views!

### Big O Complexity

Fixed-width integers take **O(1) space** because they always take the same number of bits.

Operations on fixed-width integers (addition, subtraction, multiplication, division) take **O(1) time**.

### The Tradeoff

**Advantage:** Very space and time efficient

**Disadvantage:** Limited to 2ⁿ possibilities (where n is the number of bits)

---

## Arrays

### What is an Array?

An array is a way to store multiple values of the same size next to each other in RAM.

Suppose we want to store kombucha counts for each day. We store each count in an 8-bit unsigned integer, right next to each other in RAM:

```
Address: 0  1  2  3  4  5  6  7
Value:   3  5  1  2  4  8  2  1
```

That's an array!

### Array Indexing

Array elements are numbered—we call this number the **index**.

Each array element's index corresponds to its address (though not always exactly):

```
Index:   0  1  2  3  4  5  6  7
Address: 0  1  2  3  4  5  6  7
Value:   3  5  1  2  4  8  2  1
```

### Finding Array Elements

To find the nth item in an array:

```
address of nth item = address of array start + n
```

For example, if our array starts at address 3 and we want index 4:
```
address = 3 + 4 = 7
```

### Multi-byte Arrays

When items are larger than 1 byte (like 64-bit integers), we multiply:

```
address of nth item = address of array start + (n × size of each item in bytes)
```

### Why This Works

This formula works because:
1. **Each item is the same size** (takes up the same number of bytes)
2. **The array is contiguous** (no gaps in memory)

These constraints make arrays predictable—we can calculate exactly where any element is.

### Array Lookup Complexity

- **Time**: O(1) — We can calculate the address and read it instantly
- **Space**: O(1) per element — Fixed-width items take fixed space

### Array Tradeoffs

**Advantages:**
- O(1) lookups by index

**Disadvantages:**
- All items must be the same size
- Need a large block of uninterrupted memory
- Expensive to insert or delete in the middle

---

## Strings

### What is a String?

A string is a series of characters (letters, punctuation, etc.).

### Character Encoding

We map numbers to characters using a **character encoding**. Common example: ASCII

```
A = 1 (00000001)
B = 2 (00000010)
...
Z = 26 (00011010)
a = 27 (00011011)
...
```

### Strings as Arrays

Since characters are just 8-bit numbers, we can store strings as arrays of numbers!

```
String: "NICE"
Binary: 78, 73, 67, 69
```

---

## Pointers

### The Problem with Array Requirements

Remember: array items must all be the same size, and the array must be contiguous in memory.

This creates problems when we want to store variable-length data like baby names:

```
Names stored in array with fixed 13-character slots:
[Bill______] [Jane______] [Wigglesworth]
           ↑ Wasted space!
```

### The Solution: Pointers

Instead of storing the strings directly in an array, we:
1. Store the strings wherever we can fit them in memory
2. Store **pointers** (memory addresses) in our array instead

```
Array of pointers:
[*3456] → "Bill" at address 3456
[*7899] → "Jane" at address 7899
[*1204] → "Wigglesworth" at address 1204
```

### Pointers Solve Both Problems

1. **Items don't have to be the same size** — each string can be any length
2. **No need for contiguous memory** — strings can be scattered throughout RAM

### The Tradeoff

**Advantages:**
- Variable-length items
- Don't need contiguous memory

**Disadvantages:**
- **Not cache-friendly** — items are scattered throughout RAM
- Slower to access because memory jumps aren't cached
- Lookups are still O(1) but slower in practice

---

## Dynamic Arrays

### The Problem

In low-level languages like C, you must specify array size ahead of time. But what if you don't know how big your array needs to be?

For example, a word processor doesn't know ahead of time how long the document will be!

### The Solution

A **dynamic array** automatically resizes itself when it runs out of space.

Python's "list" is a dynamic array. Java has both `array` (fixed) and `ArrayList` (dynamic).

### How It Works

**Starting state:**
```
Size: 0, Capacity: 10
[_][_][_][_][_][_][_][_][_][_]
```

**After appending 4 items:**
```
Size: 4, Capacity: 10
[D][e][a][r][_][_][_][_][_][_]
      ↑ end_index
```

### When Capacity Runs Out

When you try to append to a full dynamic array:

1. **Create a new, bigger array** (usually 2x the size)
2. **Copy elements** from old array to new array
3. **Free the old array**
4. **Append the new item**

```
Old array: [D][e][a][r][...rest...]
                    ↓
New array: [D][e][a][r][...rest...][_][_][_][...]
```

### Performance

- **Normal append**: O(1) time
- **Doubling append**: O(n) time (have to copy all n items)

But since doubling happens less and less frequently, the **amortized cost** of append is O(1).

In industry, we say appends are O(1) even though the worst case is O(n).

### Dynamic Array Tradeoff

**Advantages:**
- Don't need to specify size ahead of time
- O(1) append amortized cost

**Disadvantages:**
- Some appends are expensive O(n) when doubling happens

---

## Linked Lists

### The Problem We're Solving

We want fast appends like dynamic arrays, but we don't want the worst-case O(n) cost.

### Linked List Concept

What if each element was a **node** containing:
1. The value itself
2. A pointer to the next node

```
[D]→[e]→[a]→[r]→[NULL]
```

### Nodes in Memory

Linked list nodes can be scattered throughout RAM:

```
Memory:
Address 100: ['D'] → pointer to 205
Address 205: ['e'] → pointer to 350
Address 350: ['a'] → pointer to 421
Address 421: ['r'] → pointer to NULL
```

### Head and Tail Pointers

We keep:
- **head**: pointer to the first node
- **tail**: pointer to the last node (optional but useful)

### Append Operation

To append 'S' to "DEAR":

1. Create new node with 'S'
2. Point the 'R' node's next to 'S'
3. Update tail pointer to 'S'

**Time: O(1)**

### Prepend Operation

To prepend 'B' to "LOGS":

1. Create new node with 'B'
2. Point 'B' node's next to 'L'
3. Update head pointer to 'B'

**Time: O(1)**

### Comparison: Dynamic Array Prepend

With a dynamic array, prepending requires:
1. Moving every element one position forward
2. Inserting the new element at the start

**Time: O(n)** — much slower!

### Lookup Operation

To find the ith element, we must walk through the list:

```python
def get_ith_item_in_linked_list(head, i):
    current_node = head
    current_position = 0
    while current_node:
        if current_position == i:
            return current_node
        current_node = current_node.next
        current_position += 1
    return None
```

**Time: O(i)** — worst case O(n)

### Linked List Tradeoff

**Advantages:**
- O(1) append
- O(1) prepend
- Don't need contiguous memory

**Disadvantages:**
- O(i) lookup (much slower than array's O(1))
- Not cache-friendly
- Extra memory for pointers

### When to Use Each

- **Arrays**: Need fast lookups
- **Linked Lists**: Need fast appends/prepends

---

## Hash Tables

### Quick Lookup Problem

Arrays give us O(1) lookups by index (0, 1, 2, 3...). But what if we want to look up by an arbitrary key like "lies" or "foes"?

### The Idea

Use the key to generate an array index!

Example: Count word frequencies in Romeo and Juliet

1. Convert each character to its ASCII value
2. Sum them up
3. Use modulus to get an array index

For "lies":
```
l=108, i=105, e=101, s=115
Sum: 429
429 % 30 = 9 (array index)
```

This process is called **hashing**, and the process is the **hashing function**.

### Hash Table Structure

```
Key → [Hashing Function] → Array Index → Value

"lies" → [sum % 30] → 9 → 20
```

### Hash Collisions

What if two keys hash to the same index?

"lies" and "foes" both sum to 429:
```
l=108, i=105, e=101, s=115 = 429
f=102, o=111, e=101, s=115 = 429
```

Both give us index 9 when we mod by 30!

### Resolving Collisions

Common strategy: Store a **linked list** at each array index

```
Array[9] → Linked List:
  ["lies", 20] → ["foes", 15] → NULL
```

Now each array slot stores both the key and value.

### Performance with Collisions

With collisions, worst case lookup becomes O(n) instead of O(1).

But in practice:
- Hash functions minimize collisions
- Collision chains are usually short
- We say hash table lookups are **average case O(1)**

### Important Limitation

Quick lookups work in **one direction only**:
- Fast: key → value
- Slow: value → key (must walk through all entries)

Same with arrays: fast by index, slow by value.

### Hash Table Tradeoff

**Advantages:**
- O(1) average-case lookups by arbitrary key

**Disadvantages:**
- Hash collisions can cause slow lookups
- Can only quickly search key → value (not value → key)
- Requires good hash function design

---

## Summary & Tradeoffs

### Arrays
- **O(1) lookups** by index
- Need uninterrupted memory
- All items must be same size

### Dynamic Arrays
- **O(1) amortized appends**
- Worst case O(n) when doubling
- Still need O(1) lookups

### Linked Lists
- **O(1) appends and prepends**
- **O(n) lookups** — must walk the list
- Don't need contiguous memory

### Hash Tables
- **O(1) average lookups** by key
- **O(n) worst case** with collisions
- Only works one direction (key → value)

### Key Principle

**Every data structure has tradeoffs. You can't have it all.**

You must know what's important for your problem:
- Need fast lookups by index? Use **arrays**
- Need fast appends/prepends? Use **linked lists**
- Need fast lookups by key? Use **hash tables**
- Need flexibility? Use **dynamic arrays**

Choose the structure that's best for your use case!

---

## Next Steps

These fundamental data structures are the building blocks for more complex structures:
- Trees and graphs build on these concepts
- Heaps use arrays with special properties
- Tries combine pointers and arrays

Understanding these basics deeply will help you understand everything else!

# 1. Array and String Manipulation

Practical techniques for working with arrays and strings in coding interviews. These are among the most common data structures you'll encounter, and mastering them is essential.

## Readings

### 1. Array
Understanding the fundamentals of arrays and their performance characteristics.

**File:** `array.md`

**Topics Covered:**
- What arrays are and how they work in memory
- Big O complexity for all operations
- Why lookups are fast but inserts/deletes are slow
- How insertion and deletion work
- Why arrays must be contiguous in memory
- Code examples in Java
- Building blocks for other data structures

**Key Concepts:**
- O(1) lookups by index
- O(1) appends (if space available)
- O(n) inserts and deletes (require "scooting over")
- Fixed size limitation
- Memory address calculation
- Contiguity requirement

**The Big Idea:**
Arrays trade flexibility for speed. You get blazing-fast lookups but pay the price for modifications.

---

### 2. Array Slicing
Understanding the hidden cost of slicing arrays and lists.

**File:** `array_slicing.md`

**Topics Covered:**
- What array slicing is and how it works in Python
- The hidden O(n) time and space cost
- When slicing costs are obvious vs hidden
- Common slicing patterns in interviews
- Why slicing matters for interview performance
- Techniques to avoid unnecessary slicing
- When slicing is acceptable vs problematic

**Key Concepts:**
- Array slicing allocates a new list and copies elements
- O(n) time and O(n) space cost for a slice of size n
- Hidden costs in return statements and for loops
- Index arithmetic as an alternative to slicing
- Pointer/index techniques to avoid slicing
- When readability trumps micro-optimization

**The Big Idea:**
Slicing looks simple but carries a hidden cost. In interviews, always be aware of the allocations and copies happening behind the scenes.

---

## How to Use This Section

1. **Start with Array** - Master the fundamental data structure and its tradeoffs
2. **Learn about Array Slicing** - Understand the hidden costs of a seemingly simple operation
3. **Work through examples** - Follow code examples showing when slicing is efficient vs wasteful
4. **Internalize the patterns** - Recognize slicing in real interview problems
5. **Apply alternatives** - Use index arithmetic and pointers instead of slicing when appropriate
6. **Compare with alternatives** - Understand why you might choose linked lists instead of arrays

---

## Learning Path

This section will build on your understanding of Big O notation and data structures from the previous section.

Future readings will cover:
- String operations and manipulation
- Two-pointer techniques
- Sliding window patterns
- Common array interview patterns

---

## Pro Tips

- **Visualize it** - Draw out what happens when you insert or delete
- **Think about worst case** - When would insertion/deletion be most expensive?
- **Know the alternatives** - When would you use a linked list instead of an array?
- **Practice the operations** - Mentally trace through a few examples
- **Connect the concepts** - Arrays are the foundation for many other structures

Ready to practice? Start with the Array reading!


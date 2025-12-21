# 0. Algorithmic Thinking

Foundational concepts for analyzing and designing efficient algorithms. Learn the building blocks that all advanced CS knowledge is built upon.

## Readings

### 1. Big O Notation
Learn how to express algorithm complexity and compare efficiency.

**File:** `big_o_notation.md`

**Topics Covered:**
- What Big O notation is and why it matters
- Common complexity classes
- Rules for Big O analysis
- Time and space complexity
- Best, worst, and average cases
- Practice problems

**Key Concepts:**
- O(1), O(n), O(n²), O(log n), O(n log n), and more
- Dropping constants and less significant terms
- When to optimize and when not to
- Real-world limitations of Big O

---

### 2. Data Structures
Understand how data is stored in memory and the fundamental data structures built from scratch.

**File:** `data_structures.md`

**Topics Covered:**
- Random Access Memory (RAM) and how it works
- Binary numbers and how computers count
- Fixed-width integers and overflow
- Arrays: the foundation for everything
- Strings as arrays of characters
- Pointers: indirect memory access
- Dynamic Arrays: flexible sizing
- Linked Lists: pointer-based structures
- Hash Tables: fast key-value lookups

**Key Concepts:**
- Memory addresses and how to access them
- Tradeoffs between all major data structures
- Why arrays are fast for lookups but slow for insertion
- Why linked lists are fast for appending but slow for lookups
- How hash tables achieve O(1) average lookups
- Cache-friendly vs cache-unfriendly data access

**The Big Idea:**
Every data structure makes a choice: you get one advantage but lose another. Understand these tradeoffs so you can choose the right structure for your problem.

---

### 3. Logarithms
How to think about logarithms, especially in programming interviews and algorithm design.

**File:** `logarithms.md`

**Topics Covered:**
- What a logarithm actually means
- Logarithm rules and properties
- Where logarithms appear in algorithms
- Binary search - O(log n) analysis
- Sorting - merge sort O(n log n)
- Binary trees and height calculation
- Logarithm notation conventions
- Identifying logarithmic patterns

**Key Concepts:**
- Logarithms measure "how many times must we divide?"
- log₂(n) appears whenever we divide by 2 repeatedly
- Binary search, merge sort, and tree operations use logarithms
- Why O(log n) is much faster than O(n) for large inputs
- Understanding the relationship between exponents and logarithms

---

## How to Use This Section

1. **Start with Big O Notation** - You need this vocabulary to discuss complexity
2. **Study Data Structures** - Understand how data actually sits in memory
3. **Learn Logarithms** - Understand O(log n) operations and why they're fast
4. **Work through examples** - Follow the visual examples and implementations
5. **Internalize the patterns** - Recognize when logarithms appear in real algorithms
6. **Reference when solving** - Use this knowledge when designing solutions

---

## Learning Path

This is just the beginning! Future readings will build on these foundations:
- Trees and Graphs
- More complex data structures
- Algorithm design patterns

---

## Pro Tips

- **Don't memorize** - Understand the concepts deeply
- **Draw diagrams** - Visual understanding is critical
- **Think about tradeoffs** - Every design decision involves tradeoffs
- **Practice analysis** - Analyze real code to see these structures in action
- **Build intuition** - Eventually this becomes second nature

More readings will be added as you continue learning!

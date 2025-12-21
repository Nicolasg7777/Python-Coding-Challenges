# Practice: Hashing and Hash Tables

Real coding interview problems that apply hash table concepts from the readings.

---

## Practice Problems

### 1. Inflight Entertainment

**File:** `inflight_entertainment.md`

**Difficulty:** Medium

**Topics:** Hash tables, sets, two-sum pattern, O(n) solutions

**Description:**
Build an inflight entertainment system that finds two movies whose combined runtime equals the exact flight length. Users shouldn't watch the same movie twice.

**Key Concepts:**
- Using sets for O(1) lookups instead of nested loops
- The complement pattern (find what's needed for a sum)
- Checking before adding to prevent self-matching
- Why checking before adding matters
- O(n) time, O(n) space solution

**What You'll Learn:**
- The "two-sum" pattern is everywhere in interviews
- Sets enable constant-time membership checks
- How to avoid the O(n²) nested loop trap
- Real-world applications: entertainment, shopping, scheduling
- Why hashing is the first tool for lookup problems

**Difficulty Progression:**
- **Basic:** Implement the set-based solution
- **Intermediate:** Handle all edge cases (empty list, single movie, duplicates)
- **Advanced:** Solve bonus problems (minimize wasted time, any number of movies, sorted input)

### 2. Permutation Palindrome

**File:** `permutation_palindrome.md`

**Difficulty:** Medium

**Topics:** Hash tables, sets, character frequency, parity tracking

**Description:**
Check whether any permutation of a string is a palindrome. Learn to think about what data really matters (odd vs even counts, not exact counts).

**Key Concepts:**
- Understanding "permutation is palindrome" vs "string is palindrome"
- Palindrome requirement: characters must pair up (even count), except possibly one middle character
- Using sets to track characters with odd counts
- Why we don't need exact counts, only parity
- O(n) time, O(k) space solution where k = unique characters

**What You'll Learn:**
- How to analyze frequency/count problems
- Asking "what data do I really need to track?"
- Why sets are perfect for parity tracking
- Difference between brute force O(n! × n) and optimal O(n)
- How a simple insight (only odd/even matters) transforms the solution

**Difficulty Progression:**
- **Basic:** Implement the set-based solution
- **Intermediate:** Handle all edge cases (empty, single char, etc.)
- **Advanced:** Solve bonus problems (construct palindrome, extended character sets)

---

## How to Use This Section

1. **Read the readings first** - Understand hash functions and hash tables
2. **Read the problem carefully** - Understand all constraints
3. **Identify the pattern** - "Find two X's with property Y" = hash table!
4. **Attempt the solution** - Try it yourself before looking ahead
5. **Check your approach** - Read the breakdown and algorithm explanation
6. **Study the solution** - Understand why it works
7. **Test thoroughly** - Use the provided test cases
8. **Practice explaining** - Be ready to walk through your solution

---

## Pattern Recognition

### When to Use Hash Tables in Interviews

**Use a hash table/set when:**
- Finding two/multiple items with a property (two-sum, two-product, etc.)
- Tracking seen items or visited states
- Counting occurrences of elements
- Building inverse mappings (value → key lookups)
- Checking membership quickly
- Deduplication

**Classic patterns:**
- "Find two numbers that sum to X" → Set
- "Count occurrences of X" → Hash map
- "Have we seen this before?" → Set
- "Map X to Y" → Hash map

---

## Problem-Solving Strategy

For each problem:

1. **Understand** (5 min)
   - Read problem carefully
   - Work through examples
   - Identify constraints and gotchas

2. **Brainstorm** (10 min)
   - What data structures could help?
   - What's the brute force solution?
   - Can hashing help?

3. **Plan** (5 min)
   - Choose hash-based approach
   - Sketch the algorithm
   - Estimate complexity

4. **Code** (15 min)
   - Write the solution
   - Handle edge cases
   - Keep it clean

5. **Test** (5 min)
   - Run test cases
   - Check edge cases
   - Verify complexity

6. **Optimize** (10 min)
   - Could you use less space?
   - Is the code clear?
   - Does it handle all gotchas?

---

## Interview Tips

### What Interviewers Want to Hear

✓ "I recognize this as a two-sum pattern"
✓ "I'll use a set for O(1) lookups"
✓ "This avoids the O(n²) nested loop"
✓ "I need to handle edge cases like X"
✓ "Time: O(n), Space: O(n)"

### Common Mistakes to Avoid

✗ Using nested loops when set is available
✗ Forgetting about the "same element twice" gotcha
✗ Not checking all edge cases (empty, single element, etc.)
✗ Assuming input properties (sorted, unique, etc.)
✗ Not explaining your approach

---

## Coming Soon

More practice problems using hash tables:
- String permutation problems
- Duplicate detection
- Caching and memoization
- Hash table collisions
- Building custom hash functions

---

## Tips for Success

- **Start simple** - Get a working solution before optimizing
- **Test early** - Don't wait until you're done
- **Think out loud** - Explain your reasoning
- **Handle edge cases** - Explicitly address gotchas
- **Use sets wisely** - They're powerful for interview problems

Remember: The pattern is more important than the code!

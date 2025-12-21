# 2. Hashing and Hash Tables

Understanding hashing and hash tables is crucial for interview success. Hash tables are one of the most important data structures, appearing in nearly every interview, and they're built on the foundation of hash functions.

---

## Readings

### 1. Hashing and Hash Functions

Learn the fundamentals of how hashing works and why hash functions are powerful.

**File:** `hashing_and_hash_functions.md`

**Topics Covered:**
- What hash functions are and how they work
- Examples of hashing (MD5, SHA-1, SHA-256)
- Hash collisions and the pigeonhole principle
- Properties of good hash functions
- Cryptographic vs non-cryptographic hashing
- Hash fingerprints and why they matter
- Fixed-size output regardless of input size

**Key Concepts:**
- Deterministic: same input always produces same output
- Irreversible: cannot recover original from hash
- Fixed size: output length is constant regardless of input size
- Collisions: different inputs can produce same hash
- One-way function: function only works in one direction

**Use Cases:**
- Dictionaries and hash tables for O(1) lookups
- Detecting tampering and man-in-the-middle attacks
- Digital signatures and authentication
- Password storage and verification
- File integrity verification

**The Big Idea:**
Hash functions create a "fingerprint" of data. They're fast, deterministic, and one-way. This makes them perfect for building fast data structures like dictionaries and for security applications.

---

### 2. Hash Table

Understand the data structure that enables fast key-value lookups.

**File:** `hash_table.md`

**Topics Covered:**
- What hash tables are and how they work
- Built on arrays with hash functions
- Converting keys to array indices
- Hash collisions and resolution strategies
- Separate chaining, linear probing, double hashing
- Load factors and when to resize
- When operations cost O(n) time
- Sets (hash tables without values)
- Comparison with other data structures

**Key Concepts:**
- Fast O(1) average lookups by key
- Built using arrays + hash functions
- Collisions are inevitable with finite space
- Worst case O(n) with many collisions
- Unordered: keys don't have guaranteed order
- Single-directional: key→value O(1), value→key O(n)
- Not cache-friendly due to linked list collisions

**Use Cases:**
- Counting occurrences of items
- Finding pairs or complements (two-sum)
- Deduplication and removing duplicates
- Tracking visited nodes in graphs
- Caching and memoization
- Building inverse mappings

**The Big Idea:**
Hash tables are one of the most important data structures because they provide O(1) average lookups. They're everywhere in real systems: caches, databases, compilers, and more.

---

## Practice Problems

### 1. Inflight Entertainment

**File:** `Practice/inflight_entertainment.md`

**Difficulty:** Medium

**Topics:** Hash tables, sets, two-sum pattern, finding complements

**Description:**
Build an inflight entertainment system that finds two movies whose combined runtime equals the exact flight length.

**Key Concepts:**
- Using sets for O(1) lookups instead of nested loops
- The complement pattern: find what's needed for a sum
- Checking before adding to prevent self-matching
- O(n) time, O(n) space solution
- Why this is the classic "two-sum" interview pattern

**What You'll Learn:**
- The "two-sum" pattern appears everywhere in interviews
- How sets enable constant-time membership checks
- Why checking before adding matters for edge cases
- How to recognize when hashing is the answer
- Real-world applications: entertainment, shopping, scheduling

**Difficulty Progression:**
- **Basic:** Implement the set-based solution
- **Intermediate:** Handle edge cases (empty, single movie, duplicates)
- **Advanced:** Solve bonus problems (minimize wasted time, any number of movies)

---

### 2. Permutation Palindrome

**File:** `Practice/permutation_palindrome.md`

**Difficulty:** Medium

**Topics:** Hash tables, sets, character frequency, parity tracking

**Description:**
Check whether any permutation of a string is a palindrome. Learn to think about what data really matters.

**Key Concepts:**
- "Permutation is palindrome" vs "string is palindrome"
- Palindrome requirement: at most one character with odd count
- Using sets to track parity (odd/even), not exact counts
- Why we only care about odd/even, not absolute counts
- O(n) time, O(k) space solution

**What You'll Learn:**
- How to analyze frequency/count problems deeply
- Asking "what data do I really need to track?"
- Why simple insights (odd/even matters, not count) transform solutions
- Comparing brute force O(n! × n) vs optimal O(n)
- The power of choosing the right data structure

**Difficulty Progression:**
- **Basic:** Implement the set-based solution
- **Intermediate:** Handle edge cases (empty, single character)
- **Advanced:** Solve bonus problems (construct palindrome, extended characters)

---

## How to Use This Section

1. **Start with Hash Functions** - Understand the fundamentals
2. **Learn about Hash Tables** - See how they work and when to use them
3. **Study the patterns** - Learn common hash table interview patterns
4. **Read the practice problems** - See hash tables in action
5. **Attempt the solutions** - Try before looking at answers
6. **Test thoroughly** - Verify edge cases and complexity

---

## Learning Path

This section builds on your understanding from previous sections:
- **Section 0:** Big O notation helps you understand performance
- **Section 1:** Array and string techniques give you fundamentals
- **Section 2:** Hashing teaches you fast data structure techniques

Future readings in this section will cover:
- Collision resolution strategies (in depth)
- Load factors and resizing (in depth)
- Hash table vs other data structures (in depth)
- Advanced hashing techniques

---

## Key Concepts Overview

### Hash Functions
- Take any input and produce fixed-size output
- Deterministic: same input = same output
- Irreversible: can't go from output back to input
- May have collisions: different inputs can produce same output

### Common Hash Functions
- **MD5:** 128-bit (DEPRECATED for security)
- **SHA-1:** 160-bit (DEPRECATED for security)
- **SHA-256:** 256-bit (SECURE, modern standard)
- **Custom:** Simple functions for dictionaries

### Applications
1. **Fast lookups** - Dictionaries, cache, indexing
2. **Verification** - File integrity, downloads
3. **Security** - Passwords, digital signatures
4. **Deduplication** - Finding duplicate data
5. **Blockchain** - Hashing blocks and transactions

---

## Practical Implications

### For Interviews
- Hash tables are asked in ~70% of technical interviews
- Understanding hashing is essential for hash table problems
- Know the difference between hash functions and hash tables
- Understand collision strategies and when to use them

### For Your Code
- Use built-in hash tables (dictionaries, hash maps) when you need O(1) lookups
- For security: use cryptographic hash functions (SHA-256+)
- For dictionaries: simple hash functions are fine
- Always consider collisions in design

### Common Mistakes
- Confusing hash functions with encryption (hashing is one-way!)
- Using MD5 for security (it's broken!)
- Not salting passwords before hashing
- Assuming no collisions (they happen!)
- Not understanding performance implications

---

## Pro Tips

- **Hash vs Encrypt:** Hashing is one-way; encryption is two-way
- **Determinism matters:** If function isn't deterministic, hash tables break
- **Distribution matters:** Good hash functions spread keys evenly
- **Collisions happen:** With infinite inputs and finite outputs, collisions are mathematical certainty
- **Use tools wisely:** Python dictionaries handle hashing for you automatically

---

## Next Steps

You've now learned:
1. **How hash functions work** - Converting data to fixed-size fingerprints
2. **How hash tables work** - Building fast data structures on arrays and hashing

You're ready to:
- Use hash tables confidently in interviews
- Solve problems involving counting, deduplication, and pair finding
- Understand when to use hash tables vs other data structures
- Implement hash table patterns in your code

### Practice Problems

Head to the **Practice** folder in this section to apply what you've learned:
- **Inflight Entertainment** - Classic two-sum problem using sets for O(n) solution
- **Permutation Palindrome** - Check if string permutation is palindrome using parity tracking

These problems will help you recognize hash table patterns and master this crucial interview topic!


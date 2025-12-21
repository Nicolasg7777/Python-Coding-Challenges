# Practice

Real coding interview problems to practice your skills. These problems apply the concepts from the readings and prepare you for actual interviews.

---

## Practice Problems

### 1. Merging Meeting Times

**File:** `merging_meeting_times.md`

**Difficulty:** Medium

**Topics:** Array manipulation, sorting, greedy algorithms

**Description:**
Merge overlapping meeting time ranges from a calendar system. Handle edge cases like adjacent meetings and subsumed ranges.

**Key Concepts:**
- Sorting to enable a greedy approach
- Handling overlapping ranges
- Edge cases: adjacent meetings, subsumed meetings, multiple cascading merges
- Time complexity: O(n log n), Space complexity: O(n)

**What You'll Learn:**
- How sorting can transform a problem from O(n²) to O(n log n)
- Greedy algorithms after preprocessing
- Careful edge case handling
- Why in-place solutions might not always be worth it

**Difficulty Progression:**
- **Basic:** Implement the merge function for overlapping ranges
- **Intermediate:** Handle all edge cases correctly
- **Advanced:** Optimize space complexity or discuss in-place approaches

---

### 2. Reverse String in Place

**File:** `reverse_string_in_place.md`

**Difficulty:** Easy

**Topics:** In-place algorithms, two-pointer technique, string manipulation

**Description:**
Write a function that reverses a list of characters in place. Learn the two-pointer technique and why in-place algorithms are useful.

**Key Concepts:**
- In-place modification using swapping
- Two-pointer technique from opposite ends
- O(1) space complexity with in-place approach
- Why mutable types (lists) are needed instead of strings
- Swapping without temporary variables

**What You'll Learn:**
- The two-pointer pattern for in-place problems
- How to swap elements efficiently
- Recognizing when O(1) space is critical
- Understanding mutable vs immutable data types
- Why reversing is O(n) even though we visit each element

**Difficulty Progression:**
- **Basic:** Implement the basic reverse function
- **Intermediate:** Handle all edge cases correctly
- **Advanced:** Solve bonus problems (reverse only vowels, reverse a string, etc.)

---

### 3. Reverse Words

**File:** `reverse_words.md`

**Difficulty:** Medium

**Topics:** In-place algorithms, multi-phase approach, string manipulation

**Description:**
Reverse the order of words in a message (a list of characters) in place. The challenge is doing this in O(n) time while avoiding the O(n²) pitfall of swapping words with different lengths.

**Key Concepts:**
- Two-phase approach (reverse all, then each word)
- Why naive word-swapping is O(n²)
- How "scooting over" causes performance problems
- Finding word boundaries (spaces)
- O(n) time, O(1) space in-place algorithm
- Helper functions for code clarity

**What You'll Learn:**
- How to avoid the O(n²) trap of naive approaches
- Problem-solving: solve simpler version first
- Two-phase algorithms
- Importance of understanding worst-case complexity
- Finding word boundaries while traversing

**Difficulty Progression:**
- **Basic:** Implement the two-phase algorithm
- **Intermediate:** Handle all edge cases correctly
- **Advanced:** Solve bonus problems (punctuation, multiple spaces, reverse k groups)

---

### 4. Merge Sorted Arrays

**File:** `merge_sorted_arrays.md`

**Difficulty:** Medium

**Topics:** Two-pointer technique, sorted arrays, efficient merging

**Description:**
Merge two sorted lists of order IDs into one sorted list. The key is using the fact that both input lists are already sorted to achieve O(n) time instead of O(n log n).

**Key Concepts:**
- Two-pointer technique for sorted arrays
- Why naive approach (concatenate + sort) is O(n log n)
- Taking advantage of input properties (already sorted)
- Handling exhausted lists gracefully
- Short-circuit evaluation for safe comparisons
- Edge cases: empty lists, different lengths, duplicates
- O(n) time, O(n) space complexity

**What You'll Learn:**
- How to recognize when you can do better than sorting
- Two-pointer algorithm for merged lists
- Safe index bounds checking
- Short-circuit evaluation to prevent crashes
- How merge operation is used in merge sort
- Real-world applications (databases, streams, external sort)

**Difficulty Progression:**
- **Basic:** Implement the two-pointer merge algorithm
- **Intermediate:** Handle all edge cases correctly
- **Advanced:** Solve bonus problems (merge multiple lists, merge in-place, linked lists)

---

## How to Use This Section

1. **Read the problem carefully** - Understand all constraints and edge cases
2. **Identify the gotchas** - Each problem explicitly lists tricky cases
3. **Attempt the solution** - Try to solve it yourself first
4. **Check your approach** - Read the breakdown and algorithm explanation
5. **Study the solution** - Understand why it works
6. **Practice explaining** - Be ready to walk through your solution
7. **Consider variations** - Think about the bonus questions
8. **Test thoroughly** - Use the provided test cases

---

## Problem Progression

Start with easier problems and work up:

**Currently Available:**
1. **Reverse String in Place** - Two-pointer technique (Easy)
2. **Reverse Words** - Multi-phase approach (Medium)
3. **Merging Meeting Times** - Sorting + Greedy (Medium)
4. **Merge Sorted Arrays** - Two-pointer merging (Medium)

**Coming Soon:**
- Palindrome checking
- String reversal variations (reverse only vowels, multiple spaces)
- Container with Most Water (two-pointer advanced)
- Sliding window problems
- More complex interview patterns

---

## Interview Preparation Tips

### Before Attempting
- Review the related readings in the Readings section
- Make sure you understand Big O notation and space complexity
- Think about what data structures might be useful

### During Problem Solving
- Read the problem statement carefully at least twice
- Identify all constraints and edge cases
- Start with a brute force approach if you're stuck
- Think about sorting, hashing, or other preprocessing steps
- Consider what tradeoffs you're making (time vs space)

### After Solving
- Verify your solution against all test cases
- Analyze your time and space complexity
- Think about edge cases you might have missed
- Practice explaining your approach out loud
- Consider alternative solutions

---

## Working with Interview Problems

### Each Problem Includes

1. **Problem Statement** - Clear description of what to solve
2. **Examples** - Input/output examples
3. **Constraints** - What assumptions you can/can't make
4. **Gotchas** - Common mistakes and edge cases to watch for
5. **Approach** - How to think about solving it
6. **Solution** - Full code implementation
7. **Complexity** - Time and space analysis
8. **Bonus Questions** - Ways to extend or optimize
9. **Test Cases** - Code to verify your solution

### Problem-Solving Strategy

For each problem, follow this process:

1. **Understand** (5 min)
   - Read problem carefully
   - Work through examples
   - Identify edge cases

2. **Brainstorm** (10 min)
   - What approaches come to mind?
   - What data structures could help?
   - What's the brute force solution?

3. **Plan** (5 min)
   - Choose your approach
   - Sketch the algorithm
   - Estimate complexity

4. **Code** (15 min)
   - Write the solution
   - Handle edge cases
   - Keep it clean and readable

5. **Test** (5 min)
   - Run test cases
   - Check edge cases
   - Verify complexity

6. **Optimize** (10 min)
   - Can you improve time complexity?
   - Can you improve space complexity?
   - Is the code clear and maintainable?

---

## Tips for Success

### General Strategies
- **Start simple** - Get a working solution before optimizing
- **Test early** - Don't wait until you're done to test
- **Think out loud** - Explain your reasoning as you go
- **Handle edge cases** - Explicitly address gotchas
- **Verify complexity** - Make sure your solution meets requirements

### Common Mistakes to Avoid
- Not reading the problem fully
- Missing edge cases
- Assuming sorted input when it's not
- Forgetting to handle empty inputs
- Creating unnecessary extra space
- Not explaining your approach

---

## Connecting Readings to Practice

**Merging Meeting Times** uses concepts from:
- **Big O Notation** (from Section 0) - Understanding O(n log n) complexity
- **Array** (from Section 1) - Working with arrays and their operations
- **Array Slicing** (from Section 1) - Efficiently working with subarrays
- **Dynamic Arrays** (from Section 1) - Building new lists with results

---

## Ready to Practice?

Start with **Merging Meeting Times** and work through the problem step by step. Don't rush—interview preparation is about depth, not speed.

Remember: Understanding the problem deeply is more valuable than getting a quick solution!


# 3. Greedy Algorithms

Greedy algorithms are a powerful technique for solving optimization problems by making locally optimal choices at each step. Understanding when and how to use greedy algorithms is crucial for interview success.

---

## Readings

### 1. Greedy Algorithms

Learn the fundamentals of greedy algorithms and when they're applicable.

**File:** `reading/greedy_algorithms.md`

**Topics Covered:**
- What greedy algorithms are and how they work
- Simple example: making change with minimum coins
- Classic greedy problems and their solutions
- When greedy works (activity selection, MST, Dijkstra's, etc.)
- When greedy fails (knapsack, TSP, etc.)
- Characteristics of greedy-solvable problems
- How to approach greedy problems
- Proving greedy correctness

**Key Concepts:**
- Greedy choice: make locally optimal choice at each step
- Never reconsider previous choices
- Greedy choice property: greedy choices lead to globally optimal solution
- Optimal substructure: optimal solution contains optimal solutions to subproblems
- Proof by exchange argument: show non-greedy solutions can be improved

**Use Cases:**
- Activity/interval scheduling
- Minimum spanning trees
- Shortest path (Dijkstra's)
- Huffman coding and compression
- Fractional knapsack
- Task scheduling with deadlines
- Resource allocation and load balancing

**The Big Idea:**
Greedy algorithms are elegant and efficient, but they require careful analysis to ensure they actually produce optimal solutions. The key is recognizing the greedy choice property and proving (or disproving) that locally optimal choices lead to global optimality.

---

## Practice Problems

### 1. Apple Stocks

**File:** `practice/apple_stocks.md`

**Difficulty:** Medium

**Topics:** Greedy algorithms, optimization, profit maximization

**Description:**
Find the maximum profit from buying and selling Apple stock once, given a list of prices throughout the day.

**Key Concepts:**
- Greedy choice: track minimum price so far
- Calculate profit at each step
- Handle negative profits when prices only decrease
- Why max_price - min_price doesn't work
- O(n) time, O(1) space solution

**What You'll Learn:**
- How greedy works for optimization problems
- Tracking exactly what you need to solve the problem
- Why one pass through the data is sufficient
- How to think about greedy choices

**Difficulty Progression:**
- **Basic:** Implement the greedy solution
- **Intermediate:** Handle negative profits correctly
- **Advanced:** Solve bonus problems (multiple transactions, fees, hold constraints)

---

## How to Use This Section

1. **Understand the fundamentals** - Read the greedy algorithms reading
2. **Learn the characteristics** - Understand when greedy works and fails
3. **Study the examples** - See how greedy is applied to real problems
4. **Practice the approach** - Follow the problem-solving steps for greedy
5. **Practice problems** - Apply to real interview questions (coming soon)

---

## Learning Path

This section builds on your understanding from previous sections:
- **Section 0:** Big O notation helps analyze greedy algorithm efficiency
- **Section 1:** Array techniques used in greedy implementations
- **Section 2:** Hash tables used in some greedy solutions
- **Section 3:** Greedy algorithms for optimization problems

Future readings in this section will cover:
- Greedy algorithm analysis and proof techniques
- More complex greedy problems
- Combining greedy with other approaches

---

## Key Concepts Overview

### Greedy Algorithms Work When:
- **Greedy choice property:** Locally optimal choices lead to global optimum
- **Optimal substructure:** Optimal solution contains optimal subproblems
- **No conflicts:** Greedy choices don't contradict global optimum

### Classic Greedy Algorithms:
- **Activity Selection:** Schedule maximum non-overlapping activities
- **Huffman Coding:** Optimal prefix-free binary codes
- **Dijkstra's Algorithm:** Shortest path in graphs
- **Kruskal's Algorithm:** Minimum spanning tree
- **Prim's Algorithm:** Minimum spanning tree (alternate)

### When Greedy Fails:
- **0/1 Knapsack:** Can't take fractions, greedy fails
- **Traveling Salesman:** Nearest neighbor doesn't find shortest tour
- **Weighted Interval Scheduling:** Requires dynamic programming
- **Some coin change:** Depends on coin denominations

---

## Practical Implications

### For Interviews

- Greedy problems are asked frequently (~20-30% of algorithm problems)
- You must be able to identify when greedy is appropriate
- You need to prove (or disprove) that greedy works
- Common follow-up: "Is there a counterexample to your greedy approach?"

### For Your Code

- Use greedy when you can prove the greedy choice property
- Always consider: "What is 'best' at each step?"
- Implement efficiently (usually O(n log n) or O(n))
- Test thoroughly with examples and edge cases

### Common Mistakes

- Assuming greedy always works without proof
- Picking wrong metric for "best" choice
- Inefficient implementation of greedy selection
- Not considering all constraints

---

## Pro Tips

- **Think locally first:** What's the best choice right now?
- **Then think globally:** Does that lead to global optimum?
- **Prove or disprove:** Either prove greedy works or find counterexample
- **Test extensively:** Try multiple examples before committing
- **Implement efficiently:** Sort once, then single pass through data

---

## Interview Tips

### When to Suggest Greedy

"This optimization problem might have a greedy solution. At each step, I could choose the option that looks best right now..."

### How to Discuss Greedy

1. State the greedy choice: "I'll always pick X because..."
2. Explain why it's locally optimal: "This is best right now because..."
3. Justify global optimality: "This leads to optimal solution because..."
4. Analyze complexity: "Sorting is O(n log n), iteration is O(n), total O(n log n)"

### What Interviewers Want to Hear

✓ "Let me think about what 'best' means at each step"
✓ "I need to verify this greedy approach is correct"
✓ "Here's why the greedy choice property holds..."
✓ "Let me test this with a counterexample"

### What NOT to Say

✗ "Greedy always works for optimization"
✗ "I'll just greedily pick the maximum"
✗ "This should be correct" (without proof)
✗ "Let me try a greedy solution" (without analysis first)

---

## Next Steps

You've now learned:
1. **How greedy algorithms work** - Making locally optimal choices
2. **When greedy works** - The conditions and properties required
3. **When greedy fails** - Classic counterexamples
4. **How to approach problems** - The five-step problem-solving process

### Practice Problems

Head to the **Practice** folder in this section to apply what you've learned:
- **Apple Stocks** - Maximize profit by tracking minimum price (Medium)
- **Highest Product of 3** - Handle negatives and track multiple values (Medium)

These problems progress from single-variable tracking (Apple Stocks) to multi-variable tracking (Highest Product). Together they show how greedy algorithms scale!

---

## Coming Soon

More greedy algorithm practice problems:
- Highest Product of 3 - Find maximum product of 3 numbers
- Meeting Room Scheduling - Maximum non-overlapping meetings
- Optimal Load Balancing - Distribute work to minimize latency
- Interval Scheduling with Weights - Maximize value
- And many more!

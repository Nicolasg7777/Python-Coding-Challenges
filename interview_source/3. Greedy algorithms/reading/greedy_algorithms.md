# Greedy Algorithms

## What is a Greedy Algorithm?

A **greedy algorithm** is an approach to solving problems where you make the locally optimal choice at each step, hoping to find a global optimum. At every decision point, you pick the option that looks best *right now*, without reconsidering previous choices.

The name "greedy" comes from the fact that the algorithm always greedily picks the best immediate option available.

---

## Simple Example: Making Change

Imagine you're a cashier and need to give someone **67 cents** using as few coins as possible.

### The Greedy Approach

At each step, choose the **highest-value coin** you can use:

```
Remaining: 67¢
Take a quarter (25¢)  → Remaining: 42¢ (1 coin used)
Take a quarter (25¢)  → Remaining: 17¢ (2 coins used)
Take a dime (10¢)     → Remaining: 7¢  (3 coins used)
Take a nickel (5¢)    → Remaining: 2¢  (4 coins used)
Take a penny (1¢)     → Remaining: 1¢  (5 coins used)
Take a penny (1¢)     → Remaining: 0¢  (6 coins used)

Result: 6 coins
```

This greedy approach gives us: **2 quarters + 1 dime + 1 nickel + 2 pennies = 6 coins**

### Why Does This Work?

For US currency, the greedy algorithm **always produces the optimal solution**. This is because:
- Each coin value is at least double the next smaller coin (quarter > dime + nickel, dime > 2 nickels, etc.)
- Taking the largest coin at each step is always the best choice
- We can prove this mathematically (though the proof is beyond scope here)

### But It Doesn't Always Work!

Not all currency systems work this way. Consider a hypothetical system with coins: **1¢, 3¢, 4¢**

To make **6 cents**:
- **Greedy approach:** Take 4¢ → Remaining 2¢ → Take 1¢ twice → **3 coins** ❌
- **Optimal approach:** Take 3¢ twice → **2 coins** ✓

The greedy approach failed because it didn't look ahead!

---

## How Greedy Algorithms Work

### The Greedy Choice Property

At each step, a greedy algorithm makes a choice based on:
1. **Current state** - What information is available now?
2. **Evaluation function** - How do we measure "best"?
3. **Local optimum** - Which choice is best right now?

```python
def greedy_algorithm(problem_state):
    solution = []

    while problem_state is not fully solved:
        # Find the best immediate choice
        best_choice = find_best_choice(problem_state)

        # Make that choice
        solution.append(best_choice)

        # Update the problem state
        problem_state = update_state(problem_state, best_choice)

    return solution
```

### Key Characteristic

Once you make a choice in a greedy algorithm, **you never reconsider it**. You can't go back and change previous decisions.

---

## Classic Examples

### Example 1: Meeting Room Scheduling

**Problem:** You have a conference room and a list of meeting requests, each with a start time and end time. You want to schedule as many non-overlapping meetings as possible.

**Greedy Approach:** Always schedule the meeting that **ends earliest**.

```python
def schedule_meetings(meetings):
    # meetings = [(start_time, end_time), ...]

    # Sort by end time
    meetings.sort(key=lambda m: m[1])

    scheduled = [meetings[0]]
    last_end_time = meetings[0][1]

    for start, end in meetings[1:]:
        # If this meeting starts after the last one ended
        if start >= last_end_time:
            scheduled.append((start, end))
            last_end_time = end

    return scheduled
```

**Why it works:** By scheduling meetings that end earliest, you leave the most room in the schedule for future meetings.

### Example 2: Minimum Spanning Tree (Kruskal's Algorithm)

**Problem:** Connect all vertices in a graph with minimum total edge weight, with no cycles.

**Greedy Approach:** Always pick the **cheapest edge** that doesn't create a cycle.

```python
def minimum_spanning_tree(vertices, edges):
    # edges = [(cost, vertex1, vertex2), ...]

    # Sort edges by cost
    edges.sort()

    mst = []
    components = UnionFind(vertices)

    for cost, u, v in edges:
        # If u and v are not already connected
        if components.find(u) != components.find(v):
            mst.append((u, v, cost))
            components.union(u, v)

    return mst
```

**Why it works:** Adding the cheapest edge that doesn't create a cycle always leads to the minimum spanning tree.

### Example 3: Interval Scheduling Maximization

**Problem:** Given intervals with weights, select non-overlapping intervals with maximum total weight.

**Greedy Approach:** Sort by end time and use dynamic programming (this one actually needs greedy + DP).

```python
def weighted_interval_scheduling(intervals):
    # intervals = [(start, end, weight), ...]

    # Sort by end time
    intervals.sort(key=lambda i: i[1])
    n = len(intervals)

    # dp[i] = max weight using intervals 0..i
    dp = [0] * n
    dp[0] = intervals[0][2]

    for i in range(1, n):
        # Option 1: Don't take this interval
        dont_take = dp[i - 1]

        # Option 2: Take this interval
        take = intervals[i][2]

        # Find the latest interval that doesn't overlap
        latest_non_overlapping = -1
        for j in range(i - 1, -1, -1):
            if intervals[j][1] <= intervals[i][0]:
                latest_non_overlapping = j
                break

        if latest_non_overlapping != -1:
            take += dp[latest_non_overlapping]

        dp[i] = max(dont_take, take)

    return dp[n - 1]
```

---

## When Greedy Works (And When It Doesn't)

### ✓ Greedy Works Well For:

1. **Activity Selection Problem** - Schedule maximum non-overlapping activities
   - Greedy: Sort by end time, pick earliest ending
   - Works: YES ✓

2. **Fractional Knapsack** - Fill bag with items (can take fractions)
   - Greedy: Pick items by highest value/weight ratio
   - Works: YES ✓

3. **Huffman Coding** - Create optimal prefix-free codes
   - Greedy: Build tree by repeatedly combining lowest-frequency nodes
   - Works: YES ✓

4. **Minimum Spanning Tree** - Connect all vertices with minimum cost
   - Greedy: Pick cheapest edge that doesn't create cycle (Kruskal's)
   - Works: YES ✓

5. **Dijkstra's Shortest Path** - Find shortest path in graph
   - Greedy: Always expand the closest unexplored vertex
   - Works: YES ✓ (with non-negative weights)

### ✗ Greedy Fails For:

1. **0/1 Knapsack Problem** - Fill bag with items (can't take fractions)
   - Greedy: Pick by value/weight ratio
   - Works: NO ✗
   ```python
   # Counterexample:
   # Bag capacity: 10
   # Items: (weight=6, value=30), (weight=5, value=25), (weight=5, value=25)
   # Greedy (by value/weight): Pick (6, 30) first → can add (5, 25) → Total: 55
   # Optimal: Pick both 5-weight items → Total: 50
   # Wait, actually greedy gives 55 which is better...

   # Better counterexample:
   # Bag capacity: 10
   # Items: (weight=6, value=30), (weight=3, value=14), (weight=3, value=14), (weight=3, value=14)
   # Greedy: value/weight = 5, 4.67, 4.67, 4.67
   # Pick (6, 30) → remaining 4 → pick one (3, 14) → Total: 44
   # Optimal: Pick three 3-weight items → Total: 42
   # Hmm, greedy still better...
   ```

   Better counterexample:
   ```python
   # Bag capacity: 10
   # Items: (weight=6, value=30), (weight=5, value=29), (weight=5, value=29)
   # Greedy: value/weight = 5, 5.8, 5.8
   # Pick (5, 29) → pick (5, 29) → Total: 58
   # Greedy: value/weight = 5, 5.8, 5.8
   # Pick (6, 30) first → remaining 4 → can't fit anything → Total: 30
   # Optimal: Pick both 5-weight items → Total: 58
   ```

2. **Traveling Salesman Problem** - Visit all cities with minimum distance
   - Greedy: Always go to nearest unvisited city
   - Works: NO ✗
   ```
   Cities arranged in triangle with one in middle:
   Greedy might visit: A → B → C → A (longer route)
   Optimal: A → C → B → A (shorter route)
   ```

3. **Coin Change (some currency)** - Make amount with minimum coins
   - Greedy: Always use largest coin possible
   - Works: NO ✗ (for some coin systems)

4. **Weighted Interval Scheduling** - Schedule overlapping intervals
   - Greedy: Can't solve optimally without DP
   - Works: NO ✗ (needs dynamic programming)

---

## Characteristics of Greedy-Solvable Problems

Problems that CAN be solved with greedy usually have these properties:

### 1. Greedy Choice Property

There exists a globally optimal solution that can be constructed by making locally optimal choices. Once you make a choice, it's never reconsidered.

### 2. Optimal Substructure

An optimal solution contains optimal solutions to subproblems. If you make the greedy choice, the remaining problem has optimal substructure.

### 3. No Conflicts

Locally optimal choices don't conflict with the global optimum.

---

## How to Approach Greedy Problems

### Step 1: Understand the Problem

What are we trying to optimize? What's the goal?

### Step 2: Identify the Greedy Choice

What's the "best" choice at each step? What metric should we use?

### Step 3: Prove (or Disprove) Correctness

**Option A: Prove it's optimal**
- Show that greedy choice property holds
- Show that optimal substructure exists
- Use exchange argument: show any non-greedy solution can be improved by making the greedy choice

**Option B: Test with examples**
- Try to find a counterexample
- If you find one, the greedy approach doesn't work
- If you can't find one after thorough testing, you might have a correct solution

### Step 4: Implement Efficiently

Make sure your greedy selection is actually O(1) or O(log n) per step, not O(n).

---

## Common Mistakes

### Mistake 1: Assuming Greedy Always Works

```python
# ❌ WRONG: Never assume without proof!
def solve_knapsack_greedy(items, capacity):
    # This doesn't always give optimal answer
    items.sort(key=lambda x: x[1]/x[0], reverse=True)  # value/weight
    # ... rest of code
```

**Fix:** Prove the greedy approach works for your specific problem, or use DP/other approach.

### Mistake 2: Wrong Greedy Metric

```python
# ❌ WRONG: What is "best"?
def schedule_meetings(meetings):
    # Sorting by duration is wrong!
    meetings.sort(key=lambda m: m[1] - m[0])

    # Sorting by start time is wrong!
    meetings.sort(key=lambda m: m[0])
```

**Fix:** The correct greedy metric for meetings is **end time** (earliest ending first).

### Mistake 3: Not Considering All Constraints

```python
# ❌ WRONG: What if there are constraints we're missing?
def select_tasks(tasks):
    # Tasks might have prerequisites!
    # Greedy by profit might violate prerequisites
    tasks.sort(key=lambda t: t['profit'], reverse=True)
```

**Fix:** Identify ALL constraints and verify greedy respects them.

### Mistake 4: Inefficient Implementation

```python
# ❌ WRONG: O(n²) implementation
def greedy_solution(items):
    solution = []
    remaining = items[:]

    while remaining:
        # This is O(n) per iteration!
        best = max(remaining, key=lambda x: x['priority'])
        solution.append(best)
        remaining.remove(best)  # O(n)

    return solution
```

**Fix:** Use appropriate data structures (heaps, sorted lists) to make greedy selection efficient.

```python
# ✓ RIGHT: O(n log n) implementation
def greedy_solution(items):
    # Sort once: O(n log n)
    items.sort(key=lambda x: x['priority'], reverse=True)

    # Iterate once: O(n)
    solution = [item for item in items]

    return solution
```

---

## Real-World Applications

1. **GPS Navigation** - Dijkstra's algorithm (greedy shortest path)
2. **Compression** - Huffman coding (greedy tree building)
3. **Network Routing** - Minimize latency by choosing best next hop
4. **Scheduling** - Schedule tasks with deadlines
5. **Resource Allocation** - Allocate limited resources efficiently
6. **Load Balancing** - Distribute work to least loaded server
7. **Huffman Coding** - Create optimal compression codes
8. **Fractional Knapsack** - Maximize value in weight-constrained container

---

## Interview Tips

### When to Suggest Greedy

"This looks like a problem where we can make locally optimal choices at each step. Let me think about whether the greedy approach could work..."

### How to Discuss Greedy Solutions

1. **State the greedy choice:** "At each step, I'll choose..."
2. **Explain why it's locally optimal:** "This is best right now because..."
3. **Justify global optimality:** "This leads to global optimum because..."
4. **Give time complexity:** "Sorting is O(n log n), and iteration is O(n)..."

### Common Interview Questions

- "Will a greedy approach work here?"
- "Can you prove your greedy solution is optimal?"
- "What's a counterexample to this greedy approach?"
- "How would you make this greedy solution more efficient?"

### What Interviewers Want to Hear

✓ "Let me think about what 'best' means at each step"
✓ "I need to prove this greedy approach works"
✓ "Here's a counterexample to greedy..."
✓ "The greedy choice property holds because..."
✓ "This greedy solution is O(n log n) due to sorting"

### What NOT to Say

✗ "Greedy always works"
✗ "I'll just pick the maximum" (without explaining metric)
✗ "This looks greedy-ish, so let's try it" (without analysis)
✗ "I'm 100% sure this greedy approach is optimal" (without proof)

---

## Comparing Approaches

| Algorithm Type | When To Use | Pros | Cons |
|----------------|------------|------|------|
| **Greedy** | Optimal substructure, greedy choice property | Fast, simple, elegant | Requires proof, doesn't always work |
| **Dynamic Programming** | Overlapping subproblems, optimal substructure | Always correct for right problems | Slower (O(n²) or more), more space |
| **Brute Force** | Small input, need guaranteed optimal | Always correct | Slow (exponential) |
| **Divide & Conquer** | Problem can be split and recombined | Efficient for many problems | Not suitable for all problems |

---

## Summary Table

| Aspect | Details |
|--------|---------|
| **Definition** | Make locally optimal choices hoping for global optimum |
| **Key Property** | Once you choose, you don't reconsider |
| **Proof Needed?** | Yes! Must prove or provide extensive testing |
| **Time Complexity** | Usually O(n log n) or O(n) with proper implementation |
| **Space Complexity** | Usually O(1) or O(n) |
| **Best For** | Problems with greedy choice property + optimal substructure |
| **Not Good For** | 0/1 knapsack, TSP, problems requiring backtracking |

---

## What We Learned

Greedy algorithms are powerful for certain problems, but they're not a magic solution. The key is:

1. **Identify** the greedy choice (what's "best" at each step?)
2. **Prove** it works (or find a counterexample)
3. **Implement** efficiently (usually with sorting + single pass)
4. **Test** thoroughly before committing to the approach

The problems where greedy works share common characteristics, and learning to recognize these patterns will help you quickly identify when greedy is appropriate.

---

## Next Steps

You now understand:
- How greedy algorithms make locally optimal choices
- Why greedy doesn't always work
- How to identify and prove greedy solutions
- Real-world applications of greedy

You're ready to tackle greedy algorithm practice problems where you'll apply these concepts to real interview questions!

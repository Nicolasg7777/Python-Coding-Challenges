# Practice: Greedy Algorithms

Real coding interview problems that apply greedy algorithm concepts from the readings.

---

## Practice Problems

### 1. Apple Stocks

**File:** `apple_stocks.md`

**Difficulty:** Medium

**Topics:** Greedy algorithms, optimization, profit maximization

**Description:**
Find the maximum profit from buying and selling Apple stock once, given a list of prices throughout the day.

**Key Concepts:**
- Greedy choice: track minimum price so far
- Calculate profit at each step
- Handle negative profits when prices only decrease
- Why max_price - min_price doesn't work (order matters)
- O(n) time, O(1) space solution

**What You'll Learn:**
- How greedy works for optimization problems
- Tracking what you need: minimum price, not all prices
- Why one pass is sufficient
- How to think: "What's the best I can do selling at each price?"
- Real-world stock trading applications

**Difficulty Progression:**
- **Basic:** Implement the greedy solution
- **Intermediate:** Handle negative profits correctly
- **Advanced:** Solve bonus problems (multiple transactions, fees, hold time)

### 2. Highest Product of 3

**File:** `highest_product_of_3.md`

**Difficulty:** Medium

**Topics:** Greedy algorithms, handling negatives, multi-variable tracking

**Description:**
Find the highest product you can get from three integers in a list, considering that two negative numbers create a positive product.

**Key Concepts:**
- Two negative numbers multiply to positive
- Need to track highest/lowest products of 2 numbers
- Track highest/lowest single numbers
- Update order matters (can't multiply current by itself)
- O(n) time, O(1) space solution

**What You'll Learn:**
- How to track multiple values simultaneously
- Why sorting approach O(n log n) is slower than greedy O(n)
- Handling negative numbers in product calculations
- Careful update ordering in loops
- How greedy scales to more complex problems

**Difficulty Progression:**
- **Basic:** Understand why negatives matter, implement greedy
- **Intermediate:** Handle all edge cases correctly
- **Advanced:** Solve bonus problems (product of 4, k, overflow handling)

---

## How to Use This Section

1. **Read the Greedy Algorithms reading first** - Understand the fundamentals
2. **Read the problem carefully** - Understand all constraints
3. **Identify the greedy choice** - What's "best" at each step?
4. **Attempt the solution** - Try it yourself before looking ahead
5. **Check your approach** - Read the breakdown and algorithm explanation
6. **Study the solution** - Understand why it works
7. **Test thoroughly** - Use the provided test cases
8. **Practice explaining** - Be ready to walk through your solution

---

## Pattern Recognition

### When to Use Greedy in Interviews

**Use a greedy approach when:**
- You're optimizing something (maximum, minimum, best, etc.)
- Local optimal choices might lead to global optimum
- You can solve in one pass through the data
- You can track necessary information efficiently

**Classic greedy patterns:**
- "Find the maximum profit" → Track minimum so far
- "Schedule maximum non-overlapping events" → Pick earliest ending
- "Minimize cost" → Greedy pick the cheapest option
- "Maximize value" → Greedy pick the highest value

---

## Problem-Solving Strategy

For each greedy problem:

1. **Understand** (5 min)
   - Read problem carefully
   - Work through examples
   - Identify what you're optimizing

2. **Identify the Greedy Choice** (10 min)
   - What's "best" at each step?
   - What information do you need to track?
   - Can you solve in one pass?

3. **Sketch the Algorithm** (5 min)
   - Write pseudocode
   - Estimate complexity

4. **Implement** (15 min)
   - Write the solution
   - Handle edge cases
   - Keep it clean

5. **Verify** (10 min)
   - Test with examples
   - Check edge cases
   - Verify time/space complexity

---

## Interview Tips

### How to Approach Greedy Problems

"I want to optimize X. At each step, I could greedily choose Y. Let me think if this actually leads to the best solution..."

### Key Points to Emphasize

✓ "I'm tracking X because that's all I need at each step"
✓ "The greedy choice is Y because..."
✓ "This works in O(n) time with O(1) space"
✓ "Let me verify this works with a test case"

### Common Mistakes to Avoid

✗ Assuming greedy works without verification
✗ Tracking too much information
✗ Not handling negative cases (profits can be negative)
✗ Multiple pass when one pass would work

---

## Coming Soon

More greedy algorithm practice problems:
- Maximum product of array elements
- Highest product of 3 numbers
- Meeting room scheduling
- Interval scheduling with weights
- And more!

---

## Tips for Success

- **Think locally first:** What's the best choice right now?
- **Then think globally:** Does that lead to the best overall result?
- **Test thoroughly:** Try your greedy approach on multiple examples
- **Handle edge cases:** Negative numbers, all same values, etc.
- **Verify correctness:** Can you prove your greedy choice is always optimal?

Remember: Greedy algorithms are elegant when they work, but they require careful analysis!

# Apple Stocks

## Problem Statement

Writing programming interview questions hasn't made me rich yet... so I might give up and start trading Apple stocks all day instead.

You want to know how much money you could have made yesterday if you'd been trading Apple stocks all day.

You have a list called `stock_prices` where:
- The **index** is the time in minutes past 9:30am (market open)
- The **value** is the price of one share of Apple stock at that time

Write an efficient function that takes `stock_prices` and returns the **best profit** you could have made from **one purchase and one sale** of one share of Apple stock.

### Constraints

- **No shorting:** You must buy before you can sell
- **Time gap:** You can't buy and sell in the same time step (at least 1 minute must pass)
- **Negative profit:** If prices only go down, return the least-bad negative profit

---

## Examples

### Example 1: Basic Case

```python
stock_prices = [10, 7, 5, 8, 11, 9]

get_max_profit(stock_prices)
# Returns 6
# Buy at $5 (index 2), sell at $11 (index 4)
# Profit: 11 - 5 = 6
```

### Example 2: Prices Going Down

```python
stock_prices = [9, 7, 4, 1]

get_max_profit(stock_prices)
# Returns -2
# Best case: buy at $9, sell at $7
# Profit: 7 - 9 = -2
# (Can't avoid losing money)
```

### Example 3: Single Peak

```python
stock_prices = [5, 1, 5, 0, 7]

get_max_profit(stock_prices)
# Returns 6
# Buy at $1 (index 1), sell at $7 (index 4)
# Profit: 7 - 1 = 6
# Note: Can't use $5 at index 2 even though it's high
```

### Example 4: Prices Increasing

```python
stock_prices = [1, 2, 3, 4, 5]

get_max_profit(stock_prices)
# Returns 4
# Buy at $1, sell at $5
# Profit: 5 - 1 = 4
```

### Example 5: Two Prices Only

```python
stock_prices = [3, 5]

get_max_profit(stock_prices)
# Returns 2
# Buy at $3, sell at $5
# Profit: 5 - 3 = 2
```

---

## Constraints

- `stock_prices` contains at least 2 prices
- Prices are positive integers
- Time gap required: at least 1 minute between buy and sell (index difference ≥ 1)

---

## Gotchas

**Gotcha 1: Highest and Lowest Prices**

You can't just take `max(prices) - min(prices)` because the maximum price might come **before** the minimum price!

```python
# ❌ WRONG:
stock_prices = [10, 7, 5, 8, 11, 9]
max_price = max(stock_prices)  # 11
min_price = min(stock_prices)  # 5
profit = max_price - min_price  # 6

# Looks right here, but what about:
stock_prices = [11, 7, 5, 8]
max_price = max(stock_prices)  # 11
min_price = min(stock_prices)  # 5
profit = max_price - min_price  # 6
# ❌ WRONG! You'd be selling at 8, not 11, because 11 comes before 5
```

**Gotcha 2: Prices Only Go Down**

If the price decreases all day, your best profit will be **negative**. You can't return 0 (that would be misleading).

```python
stock_prices = [9, 7, 4, 1]
# Best case: buy at 9, sell at 7 = -2 profit
# NOT 0!
```

**Gotcha 3: Can't Buy and Sell at Same Time**

You can't buy and sell at the same index. You need at least 1 minute of gap.

```python
# ❌ WRONG: If you initialize max_profit = 0 and update min_price
# first, then when price always decreases, max_profit stays 0
# This is wrong because profit should be negative
```

**Gotcha 4: Index Out of Bounds**

You need at least 2 prices to make a transaction (one to buy, one to sell). Handle this edge case.

```python
stock_prices = [10]  # Only one price
# Should raise an error or handle gracefully
```

---

## Approach

### Understanding the Problem

We want to find the best **buy time** and **sell time** where:
- Buy time < Sell time (must buy first)
- Maximize (sell_price - buy_price)

### Brute Force Approach (O(n²) - Too Slow)

```python
def get_max_profit_brute(stock_prices):
    if len(stock_prices) < 2:
        raise ValueError('Need at least 2 prices')

    max_profit = 0

    # Try every pair of times
    for buy_time in range(len(stock_prices)):
        for sell_time in range(buy_time + 1, len(stock_prices)):
            buy_price = stock_prices[buy_time]
            sell_price = stock_prices[sell_time]
            profit = sell_price - buy_price
            max_profit = max(max_profit, profit)

    return max_profit
```

**Problem:** O(n²) time is too slow for large inputs. Can we do better?

### Key Insight: Greedy Approach

At each time step, the best profit we can make **selling now** is:
- Current price - Minimum price seen so far

**Why greedy works:**
- For any sell time, the best profit is to buy at the lowest price before it
- Once we see a new minimum, we never need to go back to the old minimum
- We can calculate the answer in one pass!

```python
# At each step:
# - Keep track of the minimum price so far
# - Calculate profit if we sell now (current_price - min_price)
# - Update max profit if this is better
```

### Optimal Solution (O(n) - Best)

```python
def get_max_profit(stock_prices):
    # Validate input
    if len(stock_prices) < 2:
        raise ValueError('Getting a profit requires at least 2 prices')

    # Initialize with the first possible transaction
    min_price = stock_prices[0]
    max_profit = stock_prices[1] - stock_prices[0]

    # Iterate through prices starting from index 1
    # (We can't sell at index 0 since we must buy first)
    for current_price in stock_prices[1:]:
        # Calculate profit if we sell at current price
        potential_profit = current_price - min_price

        # Update max profit if better
        max_profit = max(max_profit, potential_profit)

        # Update minimum price if this is lower
        min_price = min(min_price, current_price)

    return max_profit
```

### Step-by-Step Walkthrough

**Input:** `[10, 7, 5, 8, 11, 9]`

```
Initialize:
  min_price = 10 (first price)
  max_profit = 7 - 10 = -3 (first transaction)

Index 1, price = 7:
  potential_profit = 7 - 10 = -3
  max_profit = max(-3, -3) = -3
  min_price = min(10, 7) = 7

Index 2, price = 5:
  potential_profit = 5 - 7 = -2
  max_profit = max(-3, -2) = -2
  min_price = min(7, 5) = 5

Index 3, price = 8:
  potential_profit = 8 - 5 = 3
  max_profit = max(-2, 3) = 3
  min_price = min(5, 8) = 5

Index 4, price = 11:
  potential_profit = 11 - 5 = 6
  max_profit = max(3, 6) = 6
  min_price = min(5, 11) = 5

Index 5, price = 9:
  potential_profit = 9 - 5 = 4
  max_profit = max(6, 4) = 6
  min_price = min(5, 9) = 5

Return: 6
```

---

## Complexity Analysis

### Time Complexity: **O(n)**

- Single pass through the list
- Each operation (min, max, subtraction) is O(1)
- Total: O(n)

### Space Complexity: **O(1)**

- Only using two variables: `min_price` and `max_profit`
- No extra data structures
- Total: O(1)

---

## Common Mistakes

### Mistake 1: Taking Max Price - Min Price

```python
# ❌ WRONG:
def get_max_profit_wrong(stock_prices):
    return max(stock_prices) - min(stock_prices)

# Fails when max comes before min:
# [11, 7, 5] → 11 - 5 = 6, but you can't buy at 11 and sell at 5
```

**Fix:** Track the minimum price you've actually *seen before* each selling opportunity.

### Mistake 2: Initializing max_profit to 0

```python
# ❌ WRONG:
max_profit = 0  # Always returns >= 0

# Fails for decreasing prices:
# [9, 7, 4] → returns 0, should return -2
```

**Fix:** Initialize `max_profit` to the first possible transaction: `stock_prices[1] - stock_prices[0]`

### Mistake 3: Updating min_price Before Calculating Profit

```python
# ❌ WRONG:
for price in stock_prices:
    min_price = min(min_price, price)  # Update first
    profit = price - min_price  # Always 0 or positive!
    max_profit = max(max_profit, profit)
```

**Problem:** If you update `min_price` first, then `price - min_price` can be 0 (selling to yourself), which masks negative profits.

**Fix:** Calculate profit first, then update `min_price`:

```python
# ✓ RIGHT:
for price in stock_prices[1:]:
    profit = price - min_price  # Use old min_price
    max_profit = max(max_profit, profit)
    min_price = min(min_price, price)  # Then update
```

### Mistake 4: Not Handling Edge Cases

```python
# ❌ WRONG: Doesn't handle < 2 prices
def get_max_profit_wrong(stock_prices):
    min_price = stock_prices[0]
    max_profit = stock_prices[1] - stock_prices[0]  # IndexError!
```

**Fix:** Validate input length first.

### Mistake 5: Using a Sorted Approach

```python
# ❌ WRONG: O(n log n) when we can do O(n)
sorted_prices = sorted(stock_prices)
# This loses the time information!
# We can't buy at the minimum if it comes after we sell
```

---

## Edge Cases to Test

1. **Minimum size:** `[3, 5]` → `2`
2. **Single element:** `[5]` → Should raise error
3. **Two elements (increasing):** `[2, 5]` → `3`
4. **Two elements (decreasing):** `[5, 2]` → `-3`
5. **All same price:** `[5, 5, 5]` → `0`
6. **Strictly decreasing:** `[9, 7, 4, 1]` → `-1` (best is 9→7=-2, wait... should be -1 for 4→1? No, 9→7 is least bad at -2)
7. **Strictly increasing:** `[1, 2, 3, 4, 5]` → `4` (1→5)
8. **Valley shape:** `[10, 1, 10]` → `9` (1→10)
9. **Peak shape:** `[1, 10, 1]` → `9` (1→10)
10. **Random order:** `[3, 1, 4, 1, 5, 9, 2, 6]` → `8` (1→9)
11. **Large numbers:** `[1000000, 999999]` → `-1`
12. **Very long list:** Should handle efficiently in O(n)

---

## Why This is Greedy

**Greedy Choice:** At each time step, we assume the best profit comes from selling at the current price.

**Why it works:** For any sell time, the best we can do is buy at the **lowest price before** that sell time. Once we've seen a new minimum price, we don't need to consider the old one. This greedy choice never causes us to miss the global optimum.

**Proof sketch:** If the optimal solution is to buy at time B and sell at time S, then at time S when we evaluate the profit, we will have seen the minimum price up to S, which includes B. So our greedy algorithm will find this profit (or better).

---

## Real-World Applications

1. **Stock trading** - Find best buy/sell times
2. **Traffic analysis** - Find when congestion peaked relative to baseline
3. **Temperature monitoring** - Find largest temperature swing
4. **Data stream processing** - Find maximum profit in real-time
5. **Financial analysis** - Analyze investment performance

---

## Interview Tips

### When to Mention Greedy

"This looks like a profit maximization problem. I think I can solve it with a greedy approach by tracking the minimum price and calculating the profit at each step."

### How to Discuss the Solution

1. **State the strategy:** "I'll track the minimum price seen so far and calculate the profit if I sell at each current price."

2. **Explain why it works:** "For any sell time, the best profit comes from buying at the lowest price before that time. Once I see a new minimum, I don't need to revisit old ones."

3. **Give the complexity:** "Time: O(n) because we make one pass. Space: O(1) because we only use two variables."

### What Interviewers Want to Hear

✓ "I need to track the minimum price so far"
✓ "At each step, I calculate potential profit"
✓ "This is a greedy approach"
✓ "Time: O(n), Space: O(1)"
✓ "I need to handle negative profits"

### What NOT to Say

✗ "I'll just take max price - min price"
✗ "I'll sort the prices" (changes the meaning)
✗ "Greedy always works"
✗ "I don't need to worry about negative profits"

---

## Bonus Questions

### Bonus 1: What if You Can Make Multiple Transactions?

If you can buy and sell multiple times (but hold only one share at a time):

```python
def max_profit_multiple(stock_prices):
    if len(stock_prices) < 2:
        raise ValueError('Need at least 2 prices')

    max_profit = 0

    # Buy at every local minimum and sell at every local maximum
    for i in range(len(stock_prices) - 1):
        if stock_prices[i + 1] > stock_prices[i]:
            # Price goes up, so sell tomorrow
            max_profit += stock_prices[i + 1] - stock_prices[i]

    return max_profit

# Example: [10, 7, 5, 8, 11, 9, 5, 7]
# Transactions: (5→8) + (8→11) + (5→7) = 3 + 3 + 2 = 8
```

**Time:** O(n), **Space:** O(1)

### Bonus 2: What if You Can Make Up to K Transactions?

This becomes a dynamic programming problem (beyond scope, but mentioned for completeness).

```python
def max_profit_k_transactions(stock_prices, k):
    # This requires DP and is O(n*k) or O(n*min(k, n/2))
    # More complex than the greedy single transaction
    pass
```

### Bonus 3: What if You Must Hold for Exactly N Days?

```python
def max_profit_hold_n_days(stock_prices, hold_days):
    if len(stock_prices) < hold_days + 1:
        raise ValueError(f'Need at least {hold_days + 1} prices')

    max_profit = float('-inf')

    for buy_time in range(len(stock_prices) - hold_days):
        sell_time = buy_time + hold_days
        profit = stock_prices[sell_time] - stock_prices[buy_time]
        max_profit = max(max_profit, profit)

    return max_profit
```

**Time:** O(n), **Space:** O(1)

### Bonus 4: What if You Have a Transaction Fee?

```python
def max_profit_with_fee(stock_prices, fee):
    if len(stock_prices) < 2:
        raise ValueError('Need at least 2 prices')

    min_price = stock_prices[0]
    max_profit = 0

    for current_price in stock_prices[1:]:
        # Profit after paying the fee
        potential_profit = current_price - min_price - fee

        max_profit = max(max_profit, potential_profit)
        min_price = min(min_price, current_price)

    return max_profit

# Example: [10, 7, 5, 8, 11, 9], fee=2
# Best: buy at 5, sell at 11, profit = 11 - 5 - 2 = 4
```

---

## Test Cases

```python
def test_apple_stocks():
    # Test 1: Basic example
    assert get_max_profit([10, 7, 5, 8, 11, 9]) == 6

    # Test 2: All prices go down
    assert get_max_profit([9, 7, 4, 1]) == -2

    # Test 3: Two prices only
    assert get_max_profit([3, 5]) == 2

    # Test 4: Prices only go up
    assert get_max_profit([1, 2, 3, 4, 5]) == 4

    # Test 5: All same price
    assert get_max_profit([5, 5, 5, 5]) == 0

    # Test 6: Valley (best profit in middle)
    assert get_max_profit([10, 1, 10]) == 9

    # Test 7: Peak then valley
    assert get_max_profit([5, 10, 1]) == 5

    # Test 8: Random order
    assert get_max_profit([3, 1, 4, 1, 5, 9, 2, 6]) == 8

    # Test 9: Negative profit (buy at 2, sell at 1)
    assert get_max_profit([5, 2, 1]) == -1

    # Test 10: Large profit
    assert get_max_profit([1, 100]) == 99

    # Test 11: Edge case - two elements going down
    assert get_max_profit([10, 1]) == -9

    # Test 12: Error case - only one price
    try:
        get_max_profit([5])
        assert False, "Should raise error"
    except ValueError:
        pass  # Expected

    print("All tests passed!")

# Run tests
test_apple_stocks()
```

---

## Summary

| Aspect | Details |
|--------|---------|
| **Problem** | Find max profit from one buy/sell of a stock |
| **Key Insight** | Track min price so far, calculate profit at each step |
| **Algorithm Type** | Greedy |
| **Time Complexity** | O(n) |
| **Space Complexity** | O(1) |
| **Why Greedy Works** | For any sell time, best buy is at lowest prior price |
| **Edge Case** | Negative profit when prices only decrease |
| **Order Matters** | Can't use max-min directly; must track minimum sequentially |

---

## What We Learned

This is a classic greedy algorithm problem because:

1. **Local optimality:** At each step, we make the best immediate choice
2. **Global optimality:** This leads to the overall best solution
3. **Efficiency:** We solve in one pass instead of checking all pairs

The key insight is recognizing that you only need to track:
- The minimum price you've seen
- The maximum profit you can make

This transforms the problem from O(n²) brute force to O(n) greedy solution!

---

## Next Steps

You now understand:
- How greedy works for stock profit problems
- Why tracking minimum price is sufficient
- How to handle negative profits
- How to optimize from O(n²) to O(n)

Ready to tackle more greedy algorithm problems!

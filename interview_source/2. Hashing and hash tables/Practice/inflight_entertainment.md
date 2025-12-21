# Inflight Entertainment

## Problem Statement

You've built an inflight entertainment system with on-demand movie streaming. Users on longer flights like to start a second movie right when their first one ends, but they complain that the plane usually lands before they can see the ending.

**Your task:** Write a function that takes an integer `flight_length` (in minutes) and a list of integers `movie_lengths` (in minutes) and returns a boolean indicating whether there are two numbers in `movie_lengths` whose sum equals `flight_length`.

### Requirements
- Users will watch exactly **two movies**
- Users shouldn't watch the **same movie twice**
- Optimize for runtime over memory

---

## Examples

### Example 1: Movie Pair Exists

```python
movie_lengths = [2, 4, 6, 8, 9, 10]
flight_length = 12

# Result: True
# Explanation: 2 + 10 = 12, or 4 + 8 = 12
```

### Example 2: No Movie Pair

```python
movie_lengths = [2, 3, 5, 7]
flight_length = 12

# Result: False
# Explanation: No two movies sum to 12
```

### Example 3: Duplicate Movies (Can't Watch Same Movie Twice)

```python
movie_lengths = [6, 6]
flight_length = 12

# Result: False
# Explanation: Can't watch the same movie twice (even if we have two copies)
```

### Example 4: Single Movie (Not Enough)

```python
movie_lengths = [10]
flight_length = 20

# Result: False
# Explanation: Only one movie available
```

---

## Constraints

- `flight_length` is a positive integer
- `movie_lengths` is a list of positive integers
- Movies can have any length ≥ 1

---

## Gotchas

**The big gotcha:** We can do this in **O(n) time**. Your initial instinct might be nested loops (O(n²)), but there's a better way.

**The sneaky gotcha:** Your function shouldn't give a false positive if the list has one element that is half of `flight_length`. For example:
- `flight_length = 10`
- `movie_lengths = [5]`
- Result should be `False` (can't watch the same movie twice)

If your solution doesn't check for this carefully, you might think one movie of length 5 can pair with another 5, which it can't!

---

## Approach

### Naive Approach (O(n²) - Too Slow)

```python
def can_two_movies_fill_flight(movie_lengths, flight_length):
    for i in range(len(movie_lengths)):
        for j in range(i + 1, len(movie_lengths)):
            if movie_lengths[i] + movie_lengths[j] == flight_length:
                return True
    return False
```

**Problem:** Two nested loops = O(n²) time. For a large flight with thousands of movies, this is unacceptably slow.

### Optimized Approach (O(n) - Best)

**Key insight:** For each movie, we need to find a **complement** movie that sums to `flight_length`.

If we see a movie of length `x`, we need a movie of length `flight_length - x`.

We can use a **set** to track movies we've already seen. For each movie:
1. Check if its complement is already in our set
2. If yes, we found a pair!
3. If no, add the current movie to the set and continue

**Why this works:**
- We check if the complement is in the set **before** adding the current movie
- This naturally prevents us from matching a movie with itself
- Each lookup and insertion in the set is O(1)
- We only iterate through the list once: O(n)

---

## Solution

### Solution 1: Single Pass with Set (Optimal)

```python
def can_two_movies_fill_flight(movie_lengths, flight_length):
    # Movies we've seen so far
    movie_lengths_seen = set()

    for first_movie_length in movie_lengths:
        # What length would the second movie need to be?
        matching_second_movie_length = flight_length - first_movie_length

        # Is there already a movie with that length?
        if matching_second_movie_length in movie_lengths_seen:
            return True

        # Add the current movie to our set for future comparisons
        movie_lengths_seen.add(first_movie_length)

    # We never found a matching pair
    return False
```

### How It Works (Step-by-Step Example)

**Input:** `movie_lengths = [2, 4, 6, 8, 9, 10]`, `flight_length = 12`

```
Iteration 1: first_movie = 2
  - Need: 12 - 2 = 10
  - Is 10 in {}: No
  - Add 2 → set = {2}

Iteration 2: first_movie = 4
  - Need: 12 - 4 = 8
  - Is 8 in {2}: No
  - Add 4 → set = {2, 4}

Iteration 3: first_movie = 6
  - Need: 12 - 6 = 6
  - Is 6 in {2, 4}: No
  - Add 6 → set = {2, 4, 6}

Iteration 4: first_movie = 8
  - Need: 12 - 8 = 4
  - Is 4 in {2, 4, 6}: Yes!
  - Return True (found pair: 8 + 4 = 12)
```

### Why We Don't Match with Itself

**Key point:** We check for the complement BEFORE adding the current movie to the set.

Example: `movie_lengths = [6]`, `flight_length = 12`

```
Iteration 1: first_movie = 6
  - Need: 12 - 6 = 6
  - Is 6 in {}: No (set is empty!)
  - Add 6 → set = {6}
  - Continue...

Result: False (correct! We can't watch the same movie twice)
```

If we had added the movie BEFORE checking, we would incorrectly return True.

---

## Complexity Analysis

### Time Complexity: **O(n)**

- We iterate through the list once: O(n)
- Set lookups: O(1) per operation
- Set insertions: O(1) per operation
- Total: O(n)

### Space Complexity: **O(n)**

- In the worst case, we store all movies in the set: O(n)
- We trade space for time (faster algorithm, more memory used)

---

## Common Mistakes

### Mistake 1: Using Two Loops (O(n²))

```python
def can_two_movies_fill_flight_slow(movie_lengths, flight_length):
    for i in range(len(movie_lengths)):
        for j in range(i + 1, len(movie_lengths)):
            if movie_lengths[i] + movie_lengths[j] == flight_length:
                return True
    return False
```

**Problem:** Too slow for large inputs.

### Mistake 2: Not Handling Duplicates

```python
def can_two_movies_fill_flight_wrong(movie_lengths, flight_length):
    movie_set = set(movie_lengths)
    for movie in movie_set:
        complement = flight_length - movie
        if complement in movie_set:
            return True
    return False
```

**Problem:** This returns `True` for `[6]` and `flight_length = 12` because both `movie` and `complement` are 6!

**Fix:** Check BEFORE adding to the set, or count occurrences if duplicates exist.

### Mistake 3: Forgetting Edge Cases

```python
# ❌ Wrong: Doesn't handle single movie
if len(movie_lengths) < 2:
    return False  # Add this check!
```

---

## Edge Cases to Test

1. **Empty list:** `[] → False`
2. **Single movie:** `[5] → False`
3. **No pairs:** `[1, 2, 3] → False` (if flight_length = 10)
4. **Exact pair exists:** `[5, 5] → False` (can't watch same movie twice)
5. **Multiple valid pairs:** `[2, 4, 6, 8]` → should return `True` for `flight_length = 10`
6. **Very long movies:** `[1000000, 500000] → True` for `flight_length = 1500000`

---

## Real-World Applications

1. **Entertainment systems** - Suggesting movie pairs for flights
2. **Streaming services** - Playlist recommendations
3. **Game recommendations** - Game pairs that fit a time budget
4. **Shopping** - Finding two items that total a budget
5. **Meeting scheduling** - Finding two events that fill a time slot

---

## Interview Tips

### When to Mention This

"I need two items from a list that sum to a target. This is a classic **two-sum** problem, and the optimal solution uses a set for O(n) time."

### Key Points to Emphasize

1. **Recognize the pattern** - "Two-sum" = set/hash table
2. **Explain the complement** - "For each number, I need its complement"
3. **Justify the set** - "Set gives O(1) lookups instead of O(n) search"
4. **Address the gotcha** - "I check before adding to prevent same-movie matching"
5. **Trade-offs** - "We use extra space (O(n)) to save time"

### What the Interviewer Wants to Hear

- ✓ "I'll use a set for constant-time lookups"
- ✓ "I check for the complement before adding to the set"
- ✓ "This prevents matching a movie with itself"
- ✓ "Time: O(n), Space: O(n)"

### What NOT to Say

- ✗ "I'll use nested loops" (O(n²) is too slow)
- ✗ "I'll sort first" (unnecessary, doesn't improve worst case)
- ✗ "A set stores unique values" (true but irrelevant here)

---

## Bonus Questions

### Bonus 1: What if we wanted to minimize wasted flight time?

Find two movies whose sum is **closest to** (but not exceeding) the flight length.

```python
def best_two_movies_for_flight(movie_lengths, flight_length):
    # Sort and use two pointers
    movie_lengths.sort()
    left = 0
    right = len(movie_lengths) - 1
    best_difference = float('inf')

    while left < right:
        current_sum = movie_lengths[left] + movie_lengths[right]

        if current_sum <= flight_length:
            difference = flight_length - current_sum
            if difference < best_difference:
                best_difference = difference
            left += 1
        else:
            right -= 1

    return flight_length - best_difference if best_difference != float('inf') else None
```

**Time:** O(n log n) due to sorting
**Space:** O(1) if we can modify input

### Bonus 2: What if we wanted to fill the flight with any number of movies (not just 2)?

This becomes the **subset sum problem**, which is NP-hard. But we can solve it with dynamic programming:

```python
def can_movies_fill_flight(movie_lengths, flight_length):
    dp = [False] * (flight_length + 1)
    dp[0] = True  # We can always make 0

    for movie in movie_lengths:
        # Traverse backwards to avoid using same movie twice
        for time in range(flight_length, movie - 1, -1):
            dp[time] = dp[time] or dp[time - movie]

    return dp[flight_length]
```

**Time:** O(n × flight_length)
**Space:** O(flight_length)

### Bonus 3: What if the movie_lengths were sorted?

We could use a **two-pointer approach** instead of a set:

```python
def can_two_movies_fill_flight_sorted(movie_lengths, flight_length):
    left = 0
    right = len(movie_lengths) - 1

    while left < right:
        current_sum = movie_lengths[left] + movie_lengths[right]

        if current_sum == flight_length:
            return True
        elif current_sum < flight_length:
            left += 1
        else:
            right -= 1

    return False
```

**Time:** O(n) (but requires sorted input, which costs O(n log n))
**Space:** O(1)

The set approach is still better if the list isn't already sorted!

---

## Test Cases

```python
def test_can_two_movies_fill_flight():
    # Test 1: Valid pair exists
    assert can_two_movies_fill_flight([2, 4, 6, 8, 9, 10], 12) == True

    # Test 2: No valid pair
    assert can_two_movies_fill_flight([2, 3, 5, 7], 12) == False

    # Test 3: Duplicate movies (can't use same movie twice)
    assert can_two_movies_fill_flight([6, 6], 12) == False

    # Test 4: Single movie
    assert can_two_movies_fill_flight([10], 20) == False

    # Test 5: Empty list
    assert can_two_movies_fill_flight([], 10) == False

    # Test 6: Two movies, valid pair
    assert can_two_movies_fill_flight([3, 7], 10) == True

    # Test 7: Two movies, no pair
    assert can_two_movies_fill_flight([3, 5], 10) == False

    # Test 8: Multiple valid pairs (should return True for any)
    assert can_two_movies_fill_flight([1, 2, 3, 4, 5], 7) == True  # 3+4 or 2+5

    # Test 9: Large numbers
    assert can_two_movies_fill_flight([1000000, 500000], 1500000) == True

    # Test 10: Unordered list
    assert can_two_movies_fill_flight([10, 2, 4, 6, 8], 12) == True

    print("All tests passed!")

# Run the tests
test_can_two_movies_fill_flight()
```

---

## Summary

| Aspect | Details |
|--------|---------|
| **Problem** | Find two movies that sum to flight length |
| **Key Insight** | Use a set to track complements in O(1) time |
| **Optimal Time** | O(n) with single pass |
| **Space** | O(n) for the set |
| **Gotcha** | Check for complement BEFORE adding to set |
| **Pattern** | Two-sum = hash table/set |
| **Real-World** | Entertainment, shopping, scheduling |

---

## What We Learned

The key insight is that **hashing enables fast lookups**. Instead of searching for each complement (O(n)), we store seen values in a set (O(1) lookup).

This two-sum pattern appears everywhere:
- "Find two numbers that sum to target"
- "Find two items with a combined cost of X"
- "Find two events that fill a time slot"

Whenever you see "two X's with property Y," think **hash table first**!

---

## Next Steps

You now understand:
- Hash table two-sum pattern
- Why sets enable O(n) solutions
- How to avoid matching an element with itself
- Real-world applications of hashing

Ready to tackle more hash table problems!

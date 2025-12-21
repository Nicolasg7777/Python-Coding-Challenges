# Permutation Palindrome

## Problem Statement

Write an efficient function that checks whether any **permutation** of an input string is a palindrome.

You can assume the input string only contains lowercase letters.

### Important Note

We're checking if **any permutation** of the string is a palindrome, not whether the string itself is a palindrome. This is a crucial distinction!

---

## Examples

### Example 1: String Itself is a Palindrome

```python
input_string = "civic"

# Result: True
# Explanation: "civic" is already a palindrome
# Also true: "vicc" can't form palindrome, but "civic" itself is one
```

### Example 2: Permutation Forms a Palindrome

```python
input_string = "ivicc"

# Result: True
# Explanation: "ivicc" is NOT a palindrome itself
# But we can rearrange to "civic" which IS a palindrome
# Characters: i=2, v=1, c=2 (two i's, one v, two c's)
```

### Example 3: No Permutation is a Palindrome

```python
input_string = "civil"

# Result: False
# Explanation: Characters: c=1, i=2, v=1, l=1
# Multiple characters appear odd number of times
# Can't form palindrome with these character frequencies
```

### Example 4: Another Non-Permutable Case

```python
input_string = "livci"

# Result: False
# Explanation: Same characters as "civil"
# l=1, i=2, v=1, c=1 - too many odd-count characters
```

---

## Constraints

- Input contains only lowercase letters (a-z)
- Empty string is considered a valid palindrome
- Case-insensitive not required (only lowercase)

---

## Gotchas

**The main gotcha:** We can do this in **O(n) time**, not with brute force.

**The problem statement gotcha:** We're checking if **any permutation** is a palindrome, not if the string itself is a palindrome. Make sure you understand this before you start!

Example that trips people up:
- String: `"ivicc"`
- Not a palindrome itself
- But CAN be rearranged to `"civic"` which IS a palindrome
- Answer: `True`

---

## Approach

### Understanding Palindromes

For a string to be a palindrome (or have a palindrome permutation):
- Characters must be mirrored around the center
- For even-length palindromes: every character appears an even number of times
- For odd-length palindromes: exactly one character appears an odd number of times (the middle)

**Examples:**
- `"civic"`: c=2, i=2, v=1 ✓ (one char with odd count)
- `"abba"`: a=2, b=2 ✓ (all even counts)
- `"abc"`: a=1, b=1, c=1 ✗ (three odd counts)

### Naive Brute Force Approach (O(n! × n) - Too Slow)

```python
from itertools import permutations

def has_palindrome_permutation_brute(the_string):
    # Generate all permutations
    for permutation in permutations(the_string):
        # Check if this permutation is a palindrome
        perm_str = ''.join(permutation)
        if perm_str == perm_str[::-1]:
            return True
    return False
```

**Why it's terrible:**
- Generates n! permutations (if string has n characters)
- Checks each one: O(n) per permutation
- Total: O(n! × n) - incredibly slow even for modest strings

### Optimal Approach (O(n) - Best)

**Key insight:** We don't need to generate permutations! We just need to check character frequencies.

**Logic:**
1. Count how many characters appear an odd number of times
2. If 0 or 1 characters have odd counts → can form palindrome
3. If 2+ characters have odd counts → cannot form palindrome

**Why it works:**
- In a palindrome, at most one character can appear odd times (the center)
- All other characters must pair up (even count)
- We only need to check counts, not generate permutations

### Implementation Strategy

We can use a **set** to track characters with odd counts:
- When we see a character, toggle whether it has odd count
- If character in set: it had odd count, now remove it (even count)
- If character not in set: add it (now has odd count)
- At the end, set should have ≤ 1 character

---

## Solutions

### Solution 1: Set-Based Approach (Optimal)

```python
def has_palindrome_permutation(the_string):
    # Track characters that appear an odd number of times
    unpaired_characters = set()

    for char in the_string:
        if char in unpaired_characters:
            # This character now has even count
            unpaired_characters.remove(char)
        else:
            # This character now has odd count
            unpaired_characters.add(char)

    # Palindrome permutation exists if at most one character has odd count
    return len(unpaired_characters) <= 1
```

### How It Works (Step-by-Step Example)

**Input:** `"ivicc"`

```
char='i': unpaired = {'i'}        (i count: odd)
char='v': unpaired = {'i','v'}    (v count: odd)
char='i': unpaired = {'v'}        (i count: even, remove)
char='c': unpaired = {'v','c'}    (c count: odd)
char='c': unpaired = {'v'}        (c count: even, remove)

Result: len({'v'}) = 1 ≤ 1 → True
```

**Why this works:**
- We removed 'i' because we saw it twice (even)
- We removed 'c' because we saw it twice (even)
- Only 'v' remains (odd count)
- One odd count = palindrome possible ✓

### Solution 2: Dictionary Approach (Also O(n))

```python
def has_palindrome_permutation_dict(the_string):
    # Count character frequencies
    char_counts = {}

    for char in the_string:
        char_counts[char] = char_counts.get(char, 0) + 1

    # Count how many characters have odd counts
    odd_count_chars = 0
    for count in char_counts.values():
        if count % 2 == 1:
            odd_count_chars += 1

    # At most one character can have odd count
    return odd_count_chars <= 1
```

**Why use set over dictionary?**
- Set is simpler (we only need odd/even, not exact counts)
- Set uses less memory (no count values)
- Set is more efficient (no modulo operation)
- More elegant and explicit about what we're tracking

### Solution 3: One-Pass Dictionary (Compact)

```python
def has_palindrome_permutation_compact(the_string):
    char_counts = {}

    for char in the_string:
        char_counts[char] = char_counts.get(char, 0) + 1

    odd_count = sum(1 for count in char_counts.values() if count % 2 == 1)
    return odd_count <= 1
```

---

## Complexity Analysis

### Time Complexity: **O(n)**

- Single pass through the string: O(n)
- Set operations (add, remove, contains): O(1) per operation
- Final check: O(1)
- Total: O(n)

### Space Complexity: **O(k)**

Where k = number of unique characters

**Options for expressing this:**
- **Option 1:** O(n) - worst case if all characters are unique
- **Option 2:** O(k) - more precise, where k ≤ 26 (lowercase English letters)
- **Option 3:** O(1) - if treating 26 as a constant

**Why?**
- The set stores at most all unique characters
- For lowercase English: max 26 unique characters
- In practice, k is usually small and constant

Most interviewers accept any of these, but O(k) or O(1) are more precise.

---

## Common Mistakes

### Mistake 1: Checking if String Itself is Palindrome

```python
def has_palindrome_permutation_wrong(the_string):
    return the_string == the_string[::-1]  # ❌ WRONG!
```

**Problem:** This only checks if the input string is a palindrome, not if ANY permutation is.

Input: `"ivicc"` → Returns `False` (wrong! Should be `True`)

### Mistake 2: Using Brute Force

```python
def has_palindrome_permutation_slow(the_string):
    from itertools import permutations
    for perm in permutations(the_string):
        if ''.join(perm) == ''.join(perm)[::-1]:
            return True
    return False
```

**Problem:** O(n! × n) time - only works for small strings (< 8 characters)

### Mistake 3: Incorrect Odd Count Logic

```python
def has_palindrome_permutation_wrong2(the_string):
    char_counts = {}
    for char in the_string:
        char_counts[char] = char_counts.get(char, 0) + 1

    return sum(char_counts.values()) % 2 == 0  # ❌ WRONG!
```

**Problem:** Checks if string length is even, not character frequencies.

Input: `"abc"` (length 3) → Wrong logic
Correct: Need to check how many characters have odd counts

---

## Edge Cases to Test

1. **Empty string:** `""` → `True` (no characters = palindrome)
2. **Single character:** `"a"` → `True` (single char is always palindrome)
3. **All same characters:** `"aaaa"` → `True` (already palindrome)
4. **All unique characters:** `"abcd"` → `False` (all have odd count)
5. **Even length, palindromic chars:** `"aabb"` → `True` (a=2, b=2)
6. **Odd length, palindromic chars:** `"aabbc"` → `True` (a=2, b=2, c=1)
7. **Single repeated pair:** `"aa"` → `True` (pairs up perfectly)
8. **Long string with pattern:** `"aabbccdd"` → `True` (all even)

---

## Real-World Applications

1. **Anagram checking** - Is this an anagram of a palindrome?
2. **Text analysis** - Analyzing character frequency patterns
3. **Cryptography** - Character distribution analysis
4. **Game design** - Validating letter distributions
5. **Natural language processing** - Text pattern recognition

---

## Interview Tips

### When to Mention This

"I need to check if a permutation of a string can be a palindrome. Instead of generating all permutations, I can just check character frequencies."

### Key Points to Emphasize

1. **Understand the problem** - "Any permutation" not "the string itself"
2. **Key insight** - "For palindromes, characters need to pair up"
3. **Use sets efficiently** - "I track characters with odd counts, not exact counts"
4. **Time optimization** - "This is O(n), not O(n!)"
5. **Why it works** - "At most one character can have odd count"

### What the Interviewer Wants to Hear

- ✓ "I need to check character frequencies"
- ✓ "For a palindrome, at most one character appears odd times"
- ✓ "I can use a set to track odd-count characters"
- ✓ "This is O(n) time, O(k) space"
- ✓ "I don't need to generate permutations"

### What NOT to Say

- ✗ "I'll generate all permutations and check" (way too slow)
- ✗ "I'll reverse the string and compare" (checks palindrome, not permutation)
- ✗ "I'll sort the string" (unnecessary, doesn't solve the problem)

---

## Bonus Questions

### Bonus 1: What if we wanted the actual palindrome string, not just True/False?

```python
def construct_palindrome(the_string):
    char_counts = {}
    for char in the_string:
        char_counts[char] = char_counts.get(char, 0) + 1

    # Check if palindrome is possible
    odd_char = None
    for char, count in char_counts.items():
        if count % 2 == 1:
            if odd_char:
                return None  # Can't construct palindrome
            odd_char = char

    # Build the palindrome
    left_half = []
    for char in sorted(char_counts.keys()):
        left_half.extend([char] * (char_counts[char] // 2))

    palindrome = left_half[:]
    if odd_char:
        palindrome.append(odd_char)
    palindrome.extend(left_half[::-1])

    return ''.join(palindrome)

# Examples:
construct_palindrome("ivicc")    # "civvic" or similar
construct_palindrome("abc")      # None
construct_palindrome("aabb")     # "abba"
```

**Time:** O(n) for counting + O(k log k) for sorting = O(n)
**Space:** O(n) for the result

### Bonus 2: What if the string contains uppercase and spaces?

```python
def has_palindrome_permutation_extended(the_string):
    # Only consider letters, ignore case
    unpaired_characters = set()

    for char in the_string.lower():
        if not char.isalpha():
            continue  # Skip non-letters

        if char in unpaired_characters:
            unpaired_characters.remove(char)
        else:
            unpaired_characters.add(char)

    return len(unpaired_characters) <= 1

# Examples:
has_palindrome_permutation_extended("Civic")           # True
has_palindrome_permutation_extended("A man a plan")    # True (ignores spaces)
```

### Bonus 3: What's the frequency of each character in a palindrome permutation?

```python
def analyze_palindrome_frequencies(the_string):
    char_counts = {}
    for char in the_string:
        char_counts[char] = char_counts.get(char, 0) + 1

    odd_count_chars = {char: count for char, count in char_counts.items() if count % 2 == 1}
    even_count_chars = {char: count for char, count in char_counts.items() if count % 2 == 0}

    return {
        'can_form_palindrome': len(odd_count_chars) <= 1,
        'odd_count_chars': odd_count_chars,
        'even_count_chars': even_count_chars,
        'middle_char': list(odd_count_chars.keys())[0] if odd_count_chars else None
    }

# Example:
analyze_palindrome_frequencies("ivicc")
# {
#     'can_form_palindrome': True,
#     'odd_count_chars': {'v': 1},
#     'even_count_chars': {'i': 2, 'c': 2},
#     'middle_char': 'v'
# }
```

---

## Test Cases

```python
def test_has_palindrome_permutation():
    # Test 1: Empty string
    assert has_palindrome_permutation("") == True

    # Test 2: Single character
    assert has_palindrome_permutation("a") == True

    # Test 3: Two same characters
    assert has_palindrome_permutation("aa") == True

    # Test 4: Two different characters
    assert has_palindrome_permutation("ab") == False

    # Test 5: String itself is palindrome
    assert has_palindrome_permutation("civic") == True

    # Test 6: Permutation of odd-length palindrome
    assert has_palindrome_permutation("ivicc") == True

    # Test 7: Cannot form palindrome (given example)
    assert has_palindrome_permutation("civil") == False

    # Test 8: Cannot form palindrome (another example)
    assert has_palindrome_permutation("livci") == False

    # Test 9: All same characters
    assert has_palindrome_permutation("aaaa") == True

    # Test 10: Even count pairs
    assert has_palindrome_permutation("aabbcc") == True

    # Test 11: Odd-length with middle char
    assert has_palindrome_permutation("aabbc") == True

    # Test 12: All unique characters
    assert has_palindrome_permutation("abcdef") == False

    # Test 13: Two odd, one even
    assert has_palindrome_permutation("aabbc") == True

    # Test 14: Three odd characters
    assert has_palindrome_permutation("abcde") == False

    # Test 15: Longer string
    assert has_palindrome_permutation("racecar") == True

    # Test 16: Longer non-palindromic
    assert has_palindrome_permutation("ratrace") == False

    print("All tests passed!")

# Run the tests
test_has_palindrome_permutation()
```

---

## Summary

| Aspect | Details |
|--------|---------|
| **Problem** | Check if any permutation of string is palindrome |
| **Key Insight** | At most one character can have odd count |
| **Optimal Approach** | Use set to track odd-count characters |
| **Time Complexity** | O(n) |
| **Space Complexity** | O(k) where k = unique characters |
| **Why Sets Work** | Efficient toggle of odd/even state |
| **Common Mistake** | Confusing "permutation is palindrome" with "string is palindrome" |

---

## What We Learned

The main lesson: **Always think about what data really matters.**

In this problem:
- We don't care about exact character counts
- We only care about odd vs even
- A set efficiently tracks this distinction
- This simple insight transforms O(n! × n) to O(n)

This is the power of choosing the right data structure. The set wasn't the first thing you'd think of, but once you understand the underlying insight (only odd/even matters), it becomes obvious.

Remember: When you see frequency/count problems, ask yourself:
1. What do I really need to track?
2. Can I use a simpler data structure?
3. Can sets help me avoid excess information?

These questions often lead to elegant, efficient solutions.

---

## Next Steps

You now understand:
- How to think about permutation problems
- Why character frequency matters
- How sets efficiently track parity
- The power of finding the right insight

Ready to tackle more hash table pattern problems!

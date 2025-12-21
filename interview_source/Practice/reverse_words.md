# Reverse Words

## Problem Statement

You're working on a secret team solving coded transmissions.

Your team is scrambling to decipher a recent message, worried it's a plot to break into a major European National Cake Vault. The message has been mostly deciphered, but all the words are backward! Your colleagues have handed off the last step to you.

Write a function `reverse_words()` that takes a message as a list of characters and **reverses the order of the words in place**.

### Why a List of Characters?

The goal of this question is to practice manipulating strings in place. Since we're modifying the message, we need a **mutable type** like a list, instead of Python's immutable strings.

### Constraints

- The message contains only letters and spaces
- All words are separated by one space

---

## Example

**Input:**
```python
message = ['c', 'a', 'k', 'e', ' ',
           'p', 'o', 'u', 'n', 'd', ' ',
           's', 't', 'e', 'a', 'l']

reverse_words(message)
print(''.join(message))
# Output: 'steal pound cake'
```

### More Examples

```python
# Single word
['h', 'e', 'l', 'l', 'o'] → ['h', 'e', 'l', 'l', 'o']

# Two words
['a', ' ', 'b'] → ['b', ' ', 'a']

# Three words (different lengths)
['t', 'h', 'e', ' ', 'e', 'a', 'g', 'l', 'e', ' ', 'h', 'a', 's']
→ ['h', 'a', 's', ' ', 'e', 'a', 'g', 'l', 'e', ' ', 't', 'h', 'e']
```

---

## Gotchas: What Makes This Tricky

### Gotcha 1: O(1) Space Required
We must do this in place! No creating new lists or extra data structures.

### Gotcha 2: O(n) Time Required
We must do this in O(n) time, not O(n²).

### Gotcha 3: Word Length Variations
If we swap words one at a time, swapping words of different lengths requires "scooting over" all the characters in between. This would be O(n) per swap, leading to O(n²) total time.

For example:
```
# Original: a bb c dd e ff g hh
# Swap 'a' and 'hh': hh bb c dd e ff g a
# This requires moving all n characters!
```

---

## Naive Approach: Why It Fails

### The Obvious Solution

Try to swap words one at a time from the outside in, just like reversing characters:

```python
# Pseudocode (DON'T DO THIS)
def reverse_words_naive(message):
    # Find first and last word
    # Swap them
    # Move inward
    # Repeat
```

### Why This Is O(n²)

When swapping words of different lengths, we have to "scoot over" the entire middle section.

Example with `['a', ' ', 'b', 'b', ' ', 'c', ' ', 'd', 'd']`:
- First swap ('a' ↔ 'dd'): Move ~7 characters
- Second swap ('bb' ↔ 'c'): Move ~3 characters
- Total: O(n) + O(n-5) + O(n-10) + ... = O(n²)

This is too slow!

---

## The Clever Insight: Two-Phase Reversal

Here's the key breakthrough:

**What if we reverse ALL the characters first, then reverse each word individually?**

### Step-by-Step Example

**Input:** `['t', 'h', 'e', ' ', 'e', 'a', 'g', 'l', 'e', ' ', 'h', 'a', 's', ' ', 'l', 'a', 'n', 'd', 'e', 'd']`

**Phase 1: Reverse all characters**
```
Before: the eagle has landed
After:  dednal sah elgae eht
['d', 'e', 'd', 'n', 'a', 'l', ' ', 's', 'a', 'h', ' ',
 'e', 'l', 'g', 'a', 'e', ' ', 'e', 'h', 't']
```

Notice: **The words are now in the correct order!** But each word is backward.

**Phase 2: Reverse each word individually**
```
'dednal' → 'landed'
'sah' → 'has'
'elgae' → 'eagle'
'eht' → 'the'

Result: landed has eagle the
['l', 'a', 'n', 'd', 'e', 'd', ' ', 'h', 'a', 's', ' ',
 'e', 'a', 'g', 'l', 'e', ' ', 't', 'h', 'e']
```

Perfect! ✓

### Why This Works

- Phase 1 puts words in correct positions (no "scooting over" needed)
- Phase 2 unscrambles each word (no "scooting over" needed)
- Total: O(n) + O(n) = O(n) time
- Space: Only two index variables = O(1) space

---

## Solution

```python
def reverse_words(message):
    # Phase 1: Reverse all characters in the entire message
    reverse_characters(message, 0, len(message) - 1)

    # This gives us the right word order,
    # but each word is backward

    # Phase 2: Reverse each word individually
    current_word_start_index = 0

    for i in range(len(message) + 1):
        # Found the end of the current word!
        if (i == len(message)) or (message[i] == ' '):
            # Reverse the characters in this word
            reverse_characters(message, current_word_start_index, i - 1)

            # Next word starts after the space
            current_word_start_index = i + 1


def reverse_characters(message, left_index, right_index):
    """Helper function: reverses characters from left_index to right_index"""
    while left_index < right_index:
        # Swap the characters
        message[left_index], message[right_index] = \
            message[right_index], message[left_index]

        left_index += 1
        right_index -= 1
```

### How It Works Step-by-Step

**Input:** `['c', 'a', 'k', 'e', ' ', 'p', 'o', 'u', 'n', 'd', ' ', 's', 't', 'e', 'a', 'l']`

**Phase 1: Reverse all characters**
```python
reverse_characters(message, 0, len(message) - 1)
# message = ['l', 'a', 'e', 't', 's', ' ', 'd', 'n', 'u', 'o', 'p', ' ', 'e', 'k', 'a', 'c']
```

**Phase 2: Reverse each word**
```python
# Word 1: 'laets' (indices 0-4) → 'steal'
# Word 2: 'dnuop' (indices 6-10) → 'pound'
# Word 3: 'ekac' (indices 12-15) → 'cake'
# Result: ['s', 't', 'e', 'a', 'l', ' ', 'p', 'o', 'u', 'n', 'd', ' ', 'c', 'a', 'k', 'e']
```

**Output:** `['s', 't', 'e', 'a', 'l', ' ', 'p', 'o', 'u', 'n', 'd', ' ', 'c', 'a', 'k', 'e']`
Joined: `'steal pound cake'` ✓

---

## Complexity Analysis

### Time Complexity: O(n)

- Phase 1 (reverse all): O(n) - visit each character once
- Phase 2 (reverse each word): O(n) - visit each character once
- Total: O(n) + O(n) = O(n)

No "scooting over" needed! That's the key insight.

### Space Complexity: O(1)

We only use a constant amount of extra space:
- `current_word_start_index`
- `left_index` and `right_index` in the helper function
- No additional data structures

This is optimal!

---

## Why the Naive Approach Would Be O(n²)

To understand why this two-phase approach is clever, let's see why the naive approach fails:

If we swap words individually:
```
Original: a bb c dd e ff g hh
          1st swap: hh bb c dd e ff g a (moved n chars)
          2nd swap: hh g c dd e ff bb a (moved n-5 chars)
          3rd swap: hh g e dd c ff bb a (moved n-10 chars)
          ...
```

Total moves: n + (n-5) + (n-10) + ... = O(n²)

The two-phase approach avoids this by reversing everything once, eliminating the need for character movement.

---

## Edge Cases

### Single Word
```python
reverse_words(['h', 'e', 'l', 'l', 'o'])
# Result: ['h', 'e', 'l', 'l', 'o'] (unchanged)
```

### Single Character
```python
reverse_words(['a'])
# Result: ['a'] (unchanged)
```

### Words of Same Length
```python
reverse_words(['a', 'a', ' ', 'b', 'b'])
# Result: ['b', 'b', ' ', 'a', 'a']
```

### Words of Different Lengths
```python
reverse_words(['a', ' ', 'b', 'b', 'b'])
# Result: ['b', 'b', 'b', ' ', 'a']
```

---

## Common Mistakes

### Mistake 1: Forgetting to Handle Spaces
```python
# WRONG: trying to reverse spaces as word boundaries
# Must explicitly check for spaces or message end

# CORRECT
if (i == len(message)) or (message[i] == ' '):
    # Found word boundary
```

### Mistake 2: Off-by-One Errors
```python
# WRONG
reverse_characters(message, current_word_start_index, i)

# CORRECT (space is not part of the word)
reverse_characters(message, current_word_start_index, i - 1)
```

### Mistake 3: Loop Bounds
```python
# WRONG: doesn't process the last word
for i in range(len(message)):

# CORRECT: must go one past the end
for i in range(len(message) + 1):
```

---

## Real-World Applications

This pattern is useful for:
1. **String manipulation** - Reversing words in sentences
2. **Text processing** - Paragraph formatting
3. **Language processing** - Text analysis
4. **Interview problems** - Many string problems use similar techniques

---

## Bonus Questions

### Bonus 1: Handle Punctuation

What if the message had punctuation like commas and periods?

```python
def reverse_words_with_punctuation(message):
    # Challenge: reverse words but keep punctuation attached to words
    # Example: ['h', 'i', ',', ' ', 'b', 'y', 'e', '.']
    # Output:  ['b', 'y', 'e', '.', ' ', 'h', 'i', ',']
    pass
```

Hint: What counts as a word boundary?

### Bonus 2: Handle Multiple Spaces

What if there were multiple spaces between words?

```python
def reverse_words_multiple_spaces(message):
    # Preserve multiple spaces and their positions
    pass
```

### Bonus 3: Reverse k Groups

What if instead of reversing all words, you reversed every k words?

```python
def reverse_k_words(message, k):
    # Reverse every k words
    # Leave remaining words untouched if less than k
    pass
```

---

## Testing Your Solution

```python
def test_reverse_words():
    # Basic case
    message = list("cake pound steal")
    reverse_words(message)
    assert ''.join(message) == "steal pound cake"

    # Single word
    message = list("hello")
    reverse_words(message)
    assert ''.join(message) == "hello"

    # Two words
    message = list("hello world")
    reverse_words(message)
    assert ''.join(message) == "world hello"

    # Different length words
    message = list("a bb ccc")
    reverse_words(message)
    assert ''.join(message) == "ccc bb a"

    # Single character
    message = ['a']
    reverse_words(message)
    assert ''.join(message) == "a"

    print("All tests passed!")

test_reverse_words()
```

---

## Key Insights

1. **Problem-solving strategy** - Solve a simpler version first (reverse all characters) and see if it helps
2. **Two-phase approach** - Sometimes the solution requires multiple passes
3. **Avoiding "scooting over"** - This naive pitfall costs O(n²); clever solutions avoid it
4. **In-place manipulation** - Can be tricky but powerful for interviews
5. **Pattern recognition** - Similar techniques work for many string problems

---

## Interview Tips

### What Interviewers Care About
- ✓ Understanding the O(n²) pitfall of naive approach
- ✓ Recognizing the clever two-phase strategy
- ✓ Implementing correctly with proper word boundary handling
- ✓ Explaining your approach clearly
- ✓ Handling edge cases (single word, different lengths)

### How to Explain Your Solution

1. **Acknowledge the naive approach** - "If we swap words one by one, we'd have O(n²)"
2. **Explain why it fails** - "Different length words require moving all characters"
3. **Present the insight** - "What if we reverse all characters, then each word?"
4. **Walk through an example** - Show phase 1 and phase 2 clearly
5. **Discuss complexity** - "O(n) time, O(1) space"
6. **Handle edge cases** - "Single word, different lengths, multiple spaces..."

### Common Interview Questions
- "Why is the naive approach O(n²)?"
- "Can you handle multiple spaces?"
- "Can you do this without the helper function?"
- "What about punctuation?"
- "How would you solve this if the words had already been reversed?"


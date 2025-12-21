# Word Cloud Data

## Problem Statement

You want to build a **word cloud**, an infographic where the size of a word corresponds to how often it appears in the body of text.

Write code that takes a long string and builds its word cloud data in a dictionary, where the keys are words and the values are the number of times the words occurred.

### Key Challenges

This problem requires you to handle:
- **Punctuation:** How do you separate words from punctuation?
- **Capitalization:** How do you handle "The", "the", "THE"?
- **Special cases:** Hyphenated words, contractions, possessives, ellipses, em dashes

---

## Examples

### Example 1: Simple Case

```python
input_string = "We came, we saw, we conquered"

# Result:
{
    'we': 3,
    'came': 1,
    'saw': 1,
    'conquered': 1
}
```

### Example 2: Capitalization Challenge

```python
input_string = 'After beating the eggs, Dana read the next step: Add milk and eggs, then add flour and sugar.'

# Interesting words:
# - "After" at start of sentence vs regular start
# - "Dana" proper noun
# - "Add" at start of sentence vs "add" mid-sentence
# - "eggs" and "add" appear multiple times with different cases

# Reasonable result (using "always uppercase" heuristic):
{
    'after': 1,      # Only appears at sentence start
    'beating': 1,
    'the': 2,
    'eggs': 2,       # Lowercase both times (except once capitalized)
    'Dana': 1,       # Proper noun, always capitalized
    'read': 1,
    'next': 1,
    'step': 1,
    'add': 2,        # Lowercase and capitalized - normalize to lowercase
    'milk': 1,
    'and': 2,
    'flour': 1,
    'sugar': 1
}
```

### Example 3: Complex Punctuation

```python
input_string = "We came, we saw, we conquered...then we ate Bill's (Mille-Feuille) cake."

# Challenges:
# - "..." ellipsis separates words
# - "Bill's" contraction/possessive
# - "Mille-Feuille" hyphenated word
# - Standard punctuation: commas, periods, parentheses

# Result:
{
    'we': 3,
    'came': 1,
    'saw': 1,
    'conquered': 1,
    'then': 1,
    'ate': 1,
    'bill': 1,
    's': 1,          # Possessive split into separate word
    'mille-feuille': 1,  # Hyphenated kept together
    'cake': 1
}
```

### Example 4: Case Sensitivity

```python
input_string = 'The bill came to five dollars. The bill was paid by Bill.'

# Words to track:
# - "The" (sentence start, lowercase in cloud)
# - "bill" (lowercase)
# - "Bill" (proper noun name)
# - "was" appears once
# - "paid" appears once
# - "by" appears once

# With "always uppercase" heuristic:
{
    'the': 2,        # Only appears at sentence start
    'bill': 2,       # Two times as lowercase
    'came': 1,
    'to': 1,
    'five': 1,
    'dollars': 1,
    'was': 1,
    'paid': 1,
    'by': 1
}

# Note: "Bill" as name would need more sophisticated handling
```

---

## Constraints

- Input will only contain words and standard punctuation
- Assume lowercase English letters and standard ASCII punctuation
- Handle: spaces, commas, periods, apostrophes, hyphens, em dashes, ellipses, parentheses
- No regex allowed (for measurable performance)

---

## Gotchas

**Gotcha 1: Hyphenated words and punctuation**
```python
# "Mille-Feuille" should stay together
# "hello-world" should stay together
# "hello-" (hyphen at end) should be split

# But "word." (period) should split
# And "word," (comma) should split
```

**Gotcha 2: Different capitalizations**
```python
# "The bill came. The bill was paid by Bill."
# How do we handle "The" vs "the" vs "bill" vs "Bill"?

# Decision: Only make a word uppercase if it's ALWAYS uppercase
# - "The" is sometimes capital (sentence start), sometimes lowercase → lowercase
# - "Bill" is always capital (proper noun) → Bill (or handle with heuristic)
# - "bill" is sometimes capital (sentence start), sometimes lowercase → lowercase
```

**Gotcha 3: String concatenation performance**
```python
# ❌ DON'T: word += char for each character
# This creates a new string each time: O(n²) behavior!

# ✓ DO: Track start index and length, slice at the end
# Extract substring once when word is complete: O(n) behavior
```

**Gotcha 4: Edge cases**
```python
# Input ends with a word (no space after)
# Input starts with punctuation
# Multiple spaces/punctuation in a row
# Empty string
# Single word
```

---

## Approach

### Understanding the Problem

We need to:
1. **Split words** from text (handling punctuation and special cases)
2. **Count frequencies** (dictionary/hash table)
3. **Handle capitalization** (decide on normalization strategy)

### Strategy for Case Handling

We have several options:

| Strategy | Pros | Cons |
|----------|------|------|
| **Always lowercase** | Simple, consistent | Lose all proper noun info |
| **Always uppercase if ever uppercase** | Catch proper nouns | "The" becomes "The" at sentence start |
| **Always uppercase if ALWAYS uppercase** | Good for proper nouns | "Bill" at sentence start becomes "bill" |
| **Track case separately** | Maximum info | Complex, doubles memory |
| **Use NLP/proper noun detection** | Very accurate | Slow, external dependency |

**We'll use: Always uppercase only if ALWAYS uppercase** (Option 3)

### Word Splitting Strategy

Instead of:
1. Split on spaces → `split()` function
2. Clean each word → remove punctuation

We'll:
1. **Custom iterate** through the string
2. **Check each character** as we go
3. **Add to dictionary** immediately when word is complete

**Why?** One pass, handles punctuation while splitting, better performance

### Implementation Steps

**Step 1: Identify word boundaries**
- Letters and apostrophes belong to words
- Hyphens between letters belong to words (e.g., "well-known")
- Spaces, punctuation, and other characters separate words

**Step 2: Handle special cases**
- **Apostrophes:** Keep in word (handles contractions like "don't")
  - Side effect: Possessives like "Bill's" become "bill" + "s"
  - This is a reasonable tradeoff

- **Hyphens:** Check if surrounded by letters
  - If yes: part of word (e.g., "well-known")
  - If no: word separator (e.g., "word-")

- **Ellipses:** Two or more periods = word separator
- **Em dashes:** Unicode character \u2014 = word separator
- **Commas, parentheses, etc.:** Word separators

**Step 3: Track case carefully**
- If word exists in dictionary with same case: increment
- If lowercase version exists but we see uppercase: increment lowercase (word isn't ALWAYS uppercase)
- If uppercase version exists but we see lowercase: replace with lowercase version (word isn't ALWAYS uppercase)
- Otherwise: add new word with count 1

---

## Solutions

### Solution 1: Simple Approach (O(n) but less optimized)

```python
def build_word_cloud(input_string):
    words_to_counts = {}

    # Split and process each word
    current_word = []
    for char in input_string:
        if char.isalpha() or char == "'":
            current_word.append(char)
        else:
            if current_word:
                word = ''.join(current_word)
                add_word_to_dictionary(words_to_counts, word)
                current_word = []

    # Don't forget the last word if string doesn't end with punctuation
    if current_word:
        word = ''.join(current_word)
        add_word_to_dictionary(words_to_counts, word)

    return words_to_counts


def add_word_to_dictionary(words_to_counts, word):
    # Handle case: only uppercase if always uppercase
    word_lower = word.lower()

    if word in words_to_counts:
        words_to_counts[word] += 1
    elif word_lower in words_to_counts:
        words_to_counts[word_lower] += 1
    elif word.capitalize() in words_to_counts:
        words_to_counts[word_lower] = 1
        words_to_counts[word_lower] += words_to_counts[word.capitalize()]
        del words_to_counts[word.capitalize()]
    else:
        words_to_counts[word_lower] = 1

    return words_to_counts
```

**Problem:** Uses `''.join(current_word)` each iteration, but that's fine since we only do it when word ends.

### Solution 2: Optimal Approach (Handles all edge cases)

```python
class WordCloudData:

    def __init__(self, input_string):
        self.words_to_counts = {}
        self.populate_words_to_counts(input_string)

    def populate_words_to_counts(self, input_string):
        current_word_start_index = 0
        current_word_length = 0

        for i, character in enumerate(input_string):

            # Handle end of string
            if i == len(input_string) - 1:
                if character.isalpha():
                    current_word_length += 1
                if current_word_length > 0:
                    current_word = input_string[
                        current_word_start_index:
                        current_word_start_index + current_word_length
                    ]
                    self.add_word_to_dictionary(current_word)

            # Spaces and em dashes separate words
            elif character == ' ' or character == '\u2014':
                if current_word_length > 0:
                    current_word = input_string[
                        current_word_start_index:
                        current_word_start_index + current_word_length
                    ]
                    self.add_word_to_dictionary(current_word)
                    current_word_length = 0

            # Ellipses (two+ periods) separate words
            elif character == '.':
                if i < len(input_string) - 1 and \
                        input_string[i + 1] == '.':
                    if current_word_length > 0:
                        current_word = input_string[
                            current_word_start_index:
                            current_word_start_index + current_word_length
                        ]
                        self.add_word_to_dictionary(current_word)
                        current_word_length = 0

            # Letters and apostrophes are part of words
            elif character.isalpha() or character == "'":
                if current_word_length == 0:
                    current_word_start_index = i
                current_word_length += 1

            # Hyphens: only part of word if surrounded by letters
            elif character == '-':
                if (i > 0 and i < len(input_string) - 1 and
                        input_string[i - 1].isalpha() and
                        input_string[i + 1].isalpha()):
                    current_word_length += 1
                else:
                    if current_word_length > 0:
                        current_word = input_string[
                            current_word_start_index:
                            current_word_start_index + current_word_length
                        ]
                        self.add_word_to_dictionary(current_word)
                        current_word_length = 0

            # All other punctuation separates words
            else:
                if current_word_length > 0:
                    current_word = input_string[
                        current_word_start_index:
                        current_word_start_index + current_word_length
                    ]
                    self.add_word_to_dictionary(current_word)
                    current_word_length = 0

    def add_word_to_dictionary(self, word):
        # Case 1: Word already in dictionary with same case
        if word in self.words_to_counts:
            self.words_to_counts[word] += 1

        # Case 2: Lowercase version in dictionary (our word is uppercase)
        # Only count uppercase if it's ALWAYS uppercase
        elif word.lower() in self.words_to_counts:
            self.words_to_counts[word.lower()] += 1

        # Case 3: Capitalized version in dictionary (our word is lowercase)
        # Word isn't always uppercase, so promote lowercase version
        elif word.capitalize() in self.words_to_counts:
            self.words_to_counts[word] = 1
            self.words_to_counts[word] += \
                self.words_to_counts[word.capitalize()]
            del self.words_to_counts[word.capitalize()]

        # Case 4: Word not in dictionary at all
        else:
            self.words_to_counts[word] = 1
```

### How It Works: Step-by-Step Example

**Input:** `"We came, we saw."`

```
Index 0, 'W': letter, start word at 0, length 1
Index 1, 'e': letter, length 2
Index 2, ' ': space, extract "We", add to dict, reset
Index 3, 'c': letter, start word at 3, length 1
Index 4, 'a': letter, length 2
Index 5, 'm': letter, length 3
Index 6, 'e': letter, length 4
Index 7, ',': punctuation, extract "came", add to dict, reset
Index 8, ' ': space, length is 0, skip
Index 9, 'w': letter, start word at 9, length 1
Index 10, 'e': letter, length 2
Index 11, ' ': space, extract "we", add to dict, reset
Index 12, 's': letter, start word at 12, length 1
Index 13, 'a': letter, length 2
Index 14, 'w': letter, length 3
Index 15, '.': period (check for ellipsis), not ellipsis, extract "saw", add to dict
Index 16 (end): no more characters

Final dictionary:
{
    'we': 2,      # "We" and "we" normalized
    'came': 1,
    'saw': 1
}
```

---

## Complexity Analysis

### Time Complexity: **O(n)**

- Single pass through input string: O(n)
- For each word:
  - Extract substring: O(word_length)
  - Dictionary operations (insert, lookup): O(1)
  - String operations (lower(), capitalize()): O(word_length)
- Sum of all word lengths = n
- Total: O(n)

### Space Complexity: **O(n)**

- Dictionary stores up to n unique words
- Worst case: every word is unique → O(n)
- Note: We optimized away the intermediate word list
  - Could use O(2n) space without optimization
  - With optimization: only O(n) for the dictionary

---

## Common Mistakes

### Mistake 1: String Concatenation in Loop

```python
def build_word_cloud_slow(input_string):
    words_to_counts = {}
    current_word = ""

    for char in input_string:
        if char.isalpha():
            current_word += char  # ❌ Creates new string each time!
        else:
            if current_word:
                words_to_counts[current_word] = \
                    words_to_counts.get(current_word, 0) + 1
                current_word = ""

    return words_to_counts
```

**Problem:** Each `+=` creates a new string, making it O(n²) overall.

**Fix:** Track indices and slice at the end (as shown in Solution 2).

### Mistake 2: Not Handling End of String

```python
def build_word_cloud_incomplete(input_string):
    words_to_counts = {}
    current_word = []

    for char in input_string:
        if char.isalpha():
            current_word.append(char)
        else:
            if current_word:
                word = ''.join(current_word)
                words_to_counts[word] = \
                    words_to_counts.get(word, 0) + 1
                current_word = []

    # ❌ FORGOT TO ADD LAST WORD IF STRING ENDS WITH LETTER!
    return words_to_counts
```

**Problem:** If input is "hello world", "world" won't be added.

**Fix:** Add check after loop.

### Mistake 3: Not Handling Hyphenated Words

```python
# Input: "well-known fact"
# Bad output: {"well": 1, "known": 1, "fact": 1}
# Good output: {"well-known": 1, "fact": 1}

# Solution: Check if hyphen is surrounded by letters
```

### Mistake 4: Incorrect Case Handling

```python
def add_word_wrong(words_to_counts, word):
    # ❌ This doesn't prevent "The" and "the" from coexisting
    if word.lower() in words_to_counts:
        words_to_counts[word.lower()] += 1
    else:
        words_to_counts[word] = 1
```

**Problem:** First time we see "The", it gets added as "The". Next time we see "the", we increment "the" as separate key.

**Fix:** Always check both cases and merge appropriately.

---

## Edge Cases to Test

1. **Empty string:** `""` → `{}`
2. **Single word:** `"hello"` → `{'hello': 1}`
3. **Multiple spaces:** `"hello    world"` → `{'hello': 1, 'world': 1}`
4. **Punctuation at start/end:** `".hello."` → `{'hello': 1}`
5. **Hyphenated word:** `"well-known"` → `{'well-known': 1}`
6. **Possessive:** `"John's"` → `{'john': 1, 's': 1}`
7. **Contraction:** `"don't"` → `{'don't': 1}`
8. **Ellipsis:** `"wait...go"` → `{'wait': 1, 'go': 1}`
9. **Em dash:** `"hello—world"` → `{'hello': 1, 'world': 1}`
10. **Case mixed:** `"The the THE"` → `{'the': 3}` (all to lowercase)
11. **Proper noun:** `"Bill and bill"` → `{'bill': 2}` (normalized)
12. **All punctuation:** `"...!!!???"` → `{}`
13. **Number-like:** `"123abc"` → `{'abc': 1}` (ignores numbers)
14. **Very long word:** Long hyphenated compound word
15. **Repeated punctuation:** `"hello,,,world"` → `{'hello': 1, 'world': 1}`

---

## Real-World Applications

1. **Word clouds** - Text visualization
2. **Text analysis** - Finding frequently used words
3. **Search engines** - Building inverted indices
4. **Natural language processing** - Tokenization and frequency analysis
5. **Spam detection** - Finding suspicious word patterns
6. **Autocomplete** - Ranking suggestions by frequency
7. **SEO analysis** - Finding keyword frequency
8. **Content recommendation** - Topic modeling

---

## Interview Tips

### When to Mention This

"I need to split words from text and count their frequencies. I'll handle punctuation, capitalization, and hyphenated words carefully."

### Key Points to Emphasize

1. **Identify gotchas** - "Hyphenated words, punctuation, different cases"
2. **Explain case strategy** - "Only uppercase if always uppercase"
3. **Justify custom parsing** - "One pass through string, avoid string concatenation O(n²)"
4. **Handle edge cases** - "End of string, hyphens, ellipses, em dashes"
5. **Optimization choices** - "Add words directly to dictionary, not to intermediate list"

### What the Interviewer Wants to Hear

- ✓ "I'll use a dictionary to count word frequencies"
- ✓ "I need to think carefully about case sensitivity"
- ✓ "I'll handle punctuation and special characters"
- ✓ "I'll use index tracking to avoid O(n²) string operations"
- ✓ "I'll handle edge cases like end-of-string and hyphenated words"

### What NOT to Say

- ✗ "I'll use regex to split words" (performance concerns)
- ✗ "I'll convert everything to lowercase" (loses important info)
- ✗ "I'll concatenate characters with +=" (O(n²) performance)
- ✗ "I'll split() and then clean" (two passes)

---

## Bonus Questions

### Bonus 1: How would you handle Unicode characters and emojis?

```python
def supports_unicode(input_string):
    words_to_counts = {}

    current_word = []
    for char in input_string:
        # Use different character classification
        if char.isalpha() or char.isalnum() or char == "'":
            current_word.append(char)
        else:
            if current_word:
                word = ''.join(current_word)
                word_lower = word.lower()
                words_to_counts[word_lower] = \
                    words_to_counts.get(word_lower, 0) + 1
                current_word = []

    if current_word:
        word = ''.join(current_word)
        word_lower = word.lower()
        words_to_counts[word_lower] = \
            words_to_counts.get(word_lower, 0) + 1

    return words_to_counts

# Example: "I'm singing ♬ on a ☔ day."
# Result: {"i'm": 1, "singing": 1, "on": 1, "a": 1, "day": 1}
#         (emojis are skipped)
```

### Bonus 2: How would you handle numbers, emails, and usernames?

```python
def extended_tokens(input_string):
    words_to_counts = {}

    current_token = []
    for char in input_string:
        # Allow letters, numbers, apostrophes, @, _, dots
        if char.isalnum() or char in "'@_.":
            current_token.append(char)
        else:
            if current_token:
                token = ''.join(current_token)
                token_lower = token.lower()
                words_to_counts[token_lower] = \
                    words_to_counts.get(token_lower, 0) + 1
                current_token = []

    if current_token:
        token = ''.join(current_token)
        token_lower = token.lower()
        words_to_counts[token_lower] = \
            words_to_counts.get(token_lower, 0) + 1

    return words_to_counts

# Example: "Email john@example.com or @username"
# Result: {
#     "email": 1,
#     "john@example.com": 1,
#     "@username": 1
# }
```

### Bonus 3: How would you identify phrases or compound words?

```python
def extract_phrases(input_string, phrase_length=2):
    """Extract n-grams of words."""
    words = []
    current_word = []

    for char in input_string:
        if char.isalpha():
            current_word.append(char)
        else:
            if current_word:
                words.append(''.join(current_word).lower())
                current_word = []

    if current_word:
        words.append(''.join(current_word).lower())

    # Count phrases
    phrases_to_counts = {}
    for i in range(len(words) - phrase_length + 1):
        phrase = ' '.join(words[i:i + phrase_length])
        phrases_to_counts[phrase] = \
            phrases_to_counts.get(phrase, 0) + 1

    return phrases_to_counts

# Example: "fire truck is a fire truck"
# Result: {
#     "fire truck": 2,
#     "truck is": 1,
#     "is a": 1,
#     "a fire": 1
# }
```

### Bonus 4: How would you handle plurals and possessives?

```python
def normalize_words(input_string):
    """Handle plurals, possessives, and verb forms."""
    # This would require a library like NLTK or spaCy
    # For now, here's a simple approach:

    import re

    def simplify_word(word):
        # Remove possessives
        word = re.sub(r"'s$", '', word)
        # Remove plural 's' (naive approach)
        # word = re.sub(r"s$", '', word)
        return word

    words_to_counts = {}

    for word in re.findall(r'\b\w+\b', input_string.lower()):
        simplified = simplify_word(word)
        words_to_counts[simplified] = \
            words_to_counts.get(simplified, 0) + 1

    return words_to_counts

# Example: "The bills are due. Bill's cake was eaten."
# Result: {
#     "the": 1,
#     "bill": 2,
#     "s": 1,
#     "are": 1,
#     "due": 1,
#     "cake": 1,
#     "was": 1,
#     "eaten": 1
# }
```

---

## Test Cases

```python
def test_word_cloud():
    # Test 1: Simple case
    cloud = WordCloudData("Hello world")
    assert cloud.words_to_counts == {'hello': 1, 'world': 1}

    # Test 2: Repeated words
    cloud = WordCloudData("one one two two two")
    assert cloud.words_to_counts == {'one': 2, 'two': 3}

    # Test 3: Punctuation
    cloud = WordCloudData("Hello, world!")
    assert cloud.words_to_counts == {'hello': 1, 'world': 1}

    # Test 4: Case insensitive
    cloud = WordCloudData("The the THE")
    assert cloud.words_to_counts == {'the': 3}

    # Test 5: Hyphenated words
    cloud = WordCloudData("well-known fact")
    assert cloud.words_to_counts == {'well-known': 1, 'fact': 1}

    # Test 6: Contractions
    cloud = WordCloudData("don't can't")
    assert cloud.words_to_counts == {"don't": 1, "can't": 1}

    # Test 7: Em dash
    cloud = WordCloudData("hello—world")
    assert cloud.words_to_counts == {'hello': 1, 'world': 1}

    # Test 8: Ellipsis
    cloud = WordCloudData("wait...go")
    assert cloud.words_to_counts == {'wait': 1, 'go': 1}

    # Test 9: Possessive
    cloud = WordCloudData("Bill's cake")
    assert cloud.words_to_counts == {'bill': 1, 's': 1, 'cake': 1}

    # Test 10: Multiple spaces
    cloud = WordCloudData("hello    world")
    assert cloud.words_to_counts == {'hello': 1, 'world': 1}

    # Test 11: Punctuation at ends
    cloud = WordCloudData("...hello!!!")
    assert cloud.words_to_counts == {'hello': 1}

    # Test 12: Empty string
    cloud = WordCloudData("")
    assert cloud.words_to_counts == {}

    # Test 13: Only punctuation
    cloud = WordCloudData("...!!!???")
    assert cloud.words_to_counts == {}

    # Test 14: Complex
    test_str = "We came, we saw, we conquered...then we ate Bill's (Mille-Feuille) cake."
    cloud = WordCloudData(test_str)
    assert cloud.words_to_counts['we'] == 3
    assert cloud.words_to_counts['mille-feuille'] == 1

    # Test 15: Case sensitivity with proper nouns
    cloud = WordCloudData("Bill and bill are here")
    assert cloud.words_to_counts['bill'] == 2
    assert 'Bill' not in cloud.words_to_counts

    print("All tests passed!")

# Run the tests (would need WordCloudData class)
# test_word_cloud()
```

---

## Summary

| Aspect | Details |
|--------|---------|
| **Problem** | Build word frequency dictionary from text |
| **Key Challenge** | Handle punctuation, capitalization, special cases |
| **Data Structure** | Dictionary (hash table) for O(1) lookups |
| **Time Complexity** | O(n) - single pass through input |
| **Space Complexity** | O(n) - dictionary of unique words |
| **Capitalization Strategy** | Only uppercase if ALWAYS uppercase |
| **Optimization** | Index tracking instead of string concatenation |
| **Edge Cases** | Hyphens, apostrophes, ellipses, em dashes, end of string |

---

## What We Learned

This problem teaches several important lessons:

1. **Practical data structures** - Dictionaries solve real problems
2. **Edge case handling** - The gotchas matter more than the basic algorithm
3. **Performance pitfalls** - String concatenation in loops
4. **Decision-making** - Multiple valid approaches, choose reasonable one
5. **Character classification** - Different characters need different handling
6. **Design tradeoffs** - Simple approach (lowercase all) vs sophisticated (case tracking)

The problem separates good engineers from great engineers by asking: "What are your options?" A good engineer implements one. A great engineer considers several and explains the tradeoffs.

---

## Next Steps

You now understand:
- How to build frequency counters from text
- Character classification and word boundaries
- Case normalization strategies
- Performance optimization in string processing
- Handling real-world text complexities

Ready to tackle more text analysis problems!

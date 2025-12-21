# Hash Table

## Overview

A **hash table** organizes data so you can quickly look up values for a given key.

It's one of the most important data structures in computer science, appearing in nearly every technical interview.

---

## Quick Reference: Big O Complexity

| Operation | Average Case | Worst Case |
|-----------|--------------|-----------|
| Space     | O(n)         | O(n)      |
| Insert    | O(1)         | O(n)      |
| Lookup    | O(1)         | O(n)      |
| Delete    | O(1)         | O(n)      |

---

## Strengths

### Fast Lookups
Lookups take **O(1) time on average**. This is the killer feature that makes hash tables so useful.

You can find a value in constant time if you know the key, no matter how large the hash table is.

### Flexible Keys
Most data types can be used for keys, as long as they're hashable (can be converted to a hash).

Unlike arrays where keys must be sequential integers (0, 1, 2...), hash tables let you use:
- Strings: `"apple"`, `"banana"`
- Numbers: `42`, `3.14`
- Tuples: `(1, 2)`, `("a", "b")`
- Objects: Custom classes (if they implement `__hash__`)

---

## Weaknesses

### Slow Worst-Case Lookups
In the worst case, lookups take **O(n) time**.

This happens when:
- Many keys hash to the same index (hash collisions)
- The hash function is poor
- We get unlucky with the data distribution

### Unordered
Keys aren't stored in a special order. If you need:
- The smallest key
- The largest key
- All keys in a range

...you'll need to loop through every key: **O(n) time**.

**Use an ordered data structure (like a BST) if you need ordering.**

### Single-Directional Lookups
You can look up the **value for a given key** in O(1) time.

But looking up **keys for a given value** requires looping through everything: **O(n) time**.

### Not Cache-Friendly
Many hash table implementations use linked lists to handle collisions.

Linked lists scatter data throughout memory, which is bad for CPU caches.

Arrays store data contiguously, which is better for caching.

---

## How Hash Tables Work

### The Basic Idea

Hash tables are built on **arrays**. We use a hash function to convert keys into array indices.

**Three steps:**
1. Take a key (like `"apple"`)
2. Pass it through a hash function
3. Get an array index (like `9`)
4. Store the value at that index

### Example: Simple Hash Function

**Goal:** Convert the word `"lies"` into an array index

**Step 1: Convert characters to numbers**
```
"lies"
 l = 108
 i = 105
 e = 101
 s = 115
```

**Step 2: Sum them up**
```
108 + 105 + 101 + 115 = 429
```

**Step 3: Use modulus to fit in array**

If our array has 30 slots:
```
429 % 30 = 9
```

**Step 4: Store value at index 9**

Now when we look up `"lies"`, we:
1. Hash it: `"lies"` → 9
2. Go to index 9
3. Get the value

### Visual Representation

```
Key: "lies"
       ↓
   [Hash Function]
       ↓
   429 % 30
       ↓
    Index: 9
       ↓
  Array[9] = value
```

---

## Hash Collisions

### What is a Hash Collision?

A **hash collision** occurs when two different keys hash to the same index.

### Example: Collision

```
"lies" → sum = 429 → 429 % 30 = 9
"foes" → sum = 429 → 429 % 30 = 9

Both keys hash to the same index!
```

Characters:
```
l(108) + i(105) + e(101) + s(115) = 429
f(102) + o(111) + e(101) + s(115) = 429
```

### Collision Resolution: Separate Chaining

One common strategy is **separate chaining**: store a linked list at each array index.

**Before collision:**
```
Array[9] → value for "lies"
```

**After collision (separate chaining):**
```
Array[9] → Linked List:
             ["lies" → value1] → ["foes" → value2]
```

**Important:** We store both the key and the value! Otherwise we wouldn't know which value belongs to which key.

### Other Collision Strategies

1. **Linear Probing** - Find the next empty slot
   ```
   Collision at index 9? Try 10, 11, 12...
   ```

2. **Quadratic Probing** - Skip by increasing amounts
   ```
   Collision at index 9? Try 9+1, 9+4, 9+9...
   ```

3. **Double Hashing** - Use a second hash function
   ```
   Collision? Use hash2(key) to find next position
   ```

---

## When Operations Cost O(n) Time

### Scenario 1: Hash Collisions

If all keys cause collisions, we'd have one long linked list:

```
Array[5] → Linked List with ALL keys

Lookup: must walk through entire list → O(n)
```

This is unlikely with a good hash function, but possible in the worst case.

### Scenario 2: Dynamic Array Resizing

As we add more items, the array fills up and collisions become more frequent.

**Solution:** Expand the array when it gets too full (load factor > threshold).

**Cost:** Expanding requires:
1. Allocating a larger array
2. Rehashing all existing keys
3. Reinsertong all values at new positions

Total: **O(n) time**

We do this rarely (amortized), so total time is still acceptable.

---

## Example: Python Dictionary

In Python, hash tables are called **dictionaries**:

```python
# Create a hash table
light_bulb_to_hours = {
    'incandescent': 1200,
    'compact fluorescent': 10000,
    'LED': 50000,
}

# O(1) lookup
hours = light_bulb_to_hours['LED']  # 50000

# O(1) insert
light_bulb_to_hours['halogen'] = 2000

# O(1) delete
del light_bulb_to_hours['incandescent']

# O(1) membership check
if 'LED' in light_bulb_to_hours:
    print("We have LEDs!")
```

---

## Sets: Hash Tables Without Values

A **set** is like a hash table but only stores keys, not values.

**Use sets when you only care about membership** (is something in the set or not?):

```python
visited_nodes = set()

visited_nodes.add('node_a')
visited_nodes.add('node_b')
visited_nodes.add('node_c')

if 'node_a' in visited_nodes:  # O(1)
    print("Already visited!")

'node_d' in visited_nodes  # False
```

### Common Set Use Cases

1. **Graph traversal** - Track visited nodes
2. **String problems** - Track seen characters
3. **Duplicate detection** - Check if we've seen a value before
4. **Deduplication** - Remove duplicates from a list

```python
# Remove duplicates from a list
numbers = [1, 2, 2, 3, 3, 3, 4]
unique = list(set(numbers))  # [1, 2, 3, 4]
```

---

## Hash Table vs Other Data Structures

### Hash Table vs Array

| Operation | Hash Table | Array |
|-----------|-----------|-------|
| Lookup by key | O(1) avg | O(n) |
| Lookup by index | - | O(1) |
| Insert | O(1) avg | O(n) |
| Delete | O(1) avg | O(n) |
| Ordered? | No | N/A |

**Use array if:** You need ordered data or index-based access
**Use hash table if:** You need fast lookups by key

### Hash Table vs Linked List

| Operation | Hash Table | Linked List |
|-----------|-----------|-------------|
| Lookup | O(1) avg | O(n) |
| Insert | O(1) avg | O(n) |
| Delete | O(1) avg | O(n) |
| Ordered? | No | N/A |
| Cache-friendly? | No | No |

**Use linked list if:** You need O(1) prepend/append and don't need fast lookups

### Hash Table vs Binary Search Tree

| Operation | Hash Table | BST |
|-----------|-----------|-----|
| Lookup | O(1) avg | O(log n) |
| Insert | O(1) avg | O(log n) |
| Delete | O(1) avg | O(log n) |
| Ordered? | No | Yes |
| Min/Max | O(n) | O(log n) |
| Range | O(n) | O(k + log n) |

**Use hash table if:** You need fast lookups and don't need ordering
**Use BST if:** You need ordering and range queries

---

## Implementation Details

### Load Factor

**Load factor** = number of items / array size

```
If we have 20 items and array size is 100:
Load factor = 20/100 = 0.2
```

**Why it matters:**
- Low load factor: Few collisions, fast operations
- High load factor: Many collisions, slow operations

**Typical strategy:** Resize when load factor > 0.7

### Rehashing

When we expand the array, we must **rehash all existing keys**:

```python
def resize_and_rehash(old_table, new_size):
    new_table = create_array(new_size)

    # For each key in old table
    for key, value in old_table.items():
        # Hash the key with new array size
        index = hash_function(key) % new_size
        # Insert into new table
        new_table[index] = value

    return new_table
```

---

## Common Hash Table Patterns

### Pattern 1: Counting Occurrences

```python
# Count frequency of each character
def count_chars(string):
    char_count = {}
    for char in string:
        char_count[char] = char_count.get(char, 0) + 1
    return char_count

# Result: {'h': 1, 'e': 1, 'l': 2, 'o': 1}
count_chars("hello")
```

### Pattern 2: Finding Pairs

```python
# Find two numbers that sum to target (two-sum)
def find_sum_pair(numbers, target):
    seen = set()
    for num in numbers:
        complement = target - num
        if complement in seen:
            return (complement, num)
        seen.add(num)
    return None

find_sum_pair([2, 3, 5, 7], 10)  # (3, 7)
```

### Pattern 3: Deduplication

```python
# Remove duplicates while preserving order
def unique_ordered(items):
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

unique_ordered([1, 2, 2, 3, 1, 4])  # [1, 2, 3, 4]
```

### Pattern 4: Inverse Mapping

```python
# Build reverse mapping (value → key)
def invert_dict(mapping):
    inverse = {}
    for key, value in mapping.items():
        inverse[value] = key
    return inverse

phone_to_name = {"Alice": "555-1234", "Bob": "555-5678"}
name_to_phone = invert_dict(phone_to_name)
# {"555-1234": "Alice", "555-5678": "Bob"}
```

---

## Key Takeaways

1. **Hash tables provide O(1) average lookups** - The main advantage
2. **Built on arrays with hashing functions** - Hash converts keys to indices
3. **Collisions are handled** - Usually with separate chaining or open addressing
4. **Worst case is O(n)** - But rare with good hash functions
5. **Trade-offs exist** - Fast lookups but unordered, not cache-friendly
6. **Sets are hash tables** - Just storing keys, no values
7. **Appear everywhere** - Caches, databases, compilers, real-world systems

---

## Interview Tips

### When to Use Hash Tables
- You need fast key-value lookups
- You need to track membership (with sets)
- You need to count occurrences
- You need to find pairs or complements
- The order of keys doesn't matter

### When NOT to Use Hash Tables
- You need ordered data → Use BST
- You need range queries → Use BST
- You need sequential access → Use array/linked list
- You need minimal space and small datasets → Consider alternatives

### Common Interview Questions
- "Why is hash table lookup O(1) on average?"
- "What happens with hash collisions?"
- "What's the difference between a set and a hash table?"
- "When would you use a hash table instead of an array?"
- "How do you handle collisions?"

---

## Summary

| Aspect | Details |
|--------|---------|
| **Purpose** | Fast key-value lookups |
| **Average Lookup** | O(1) |
| **Worst Case** | O(n) (many collisions) |
| **Implementation** | Array + hash function |
| **Collision Handling** | Separate chaining, open addressing |
| **Space** | O(n) |
| **Best For** | Fast lookups by key |
| **Not Good For** | Ordered data, range queries, value-based lookup |
| **Real-World Use** | Caches, databases, compilers, indexing |

Hash tables are one of the most important data structures. Master them, and you'll solve many interview problems!


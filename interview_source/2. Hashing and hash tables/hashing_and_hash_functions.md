# Hashing and Hash Functions

## What is a Hash Function?

A **hash function** takes data (like a string, a file's contents, or any input) and outputs a **hash** — a fixed-size string or number that uniquely represents that data.

The hash function is **deterministic**: the same input always produces the same hash output.

---

## Examples

### Example 1: Simple Text

**File contents:** `"cake"`
**MD5 Hash:** `DF7CE038E2FA96EDF39206F898DF134D`

### Example 2: Similar Input, Different Hash

**File contents:** `"cakes"` (just added an 's')
**MD5 Hash:** `0E9091167610558FDAE6F69BD6716771`

Notice: Even though the inputs are very similar, the hashes are completely different!

### Example 3: Large File, Same Hash Size

**File contents:** A 461 MB film
**MD5 Hash:** `664f67364296d08f31aec6fea4e9b83f`

Even though the file is massive, the hash is still the same fixed length as our simple text examples.

---

## Key Properties of Hash Functions

### Property 1: Deterministic
The same input always produces the same output:

```python
hash("apple") = 5381  # Always the same
hash("apple") = 5381  # Always the same
hash("apple") = 5381  # Always the same
```

### Property 2: Fixed Output Size
Regardless of input size, the output is always the same fixed length:

```python
hash("a")              = 5381
hash("apple")          = 3344
hash("the quick brown fox...") = 8472
```

The output size is determined by the hash function, not the input size.

### Property 3: Irreversible
You cannot recover the original input from the hash:

```python
hash_value = 5381
# Can't get "apple" back from 5381
# The function only goes one way!
```

### Property 4: Deterministic Uniqueness
Different inputs should produce different hashes (ideally):

```python
hash("apple")  = 5381
hash("orange") = 3344
hash("banana") = 8472
```

But we can't guarantee this—see hash collisions below.

---

## Hash Collisions

A **hash collision** occurs when two different inputs produce the same hash output.

### Example Collision

```python
hash("apple")  = 5381
hash("pale")   = 5381  # ← Different input, same hash!
```

This is unavoidable mathematically because:
- Input space: Infinite (any possible string)
- Output space: Finite (fixed-size hash)

By the **pigeonhole principle**, collisions must occur.

### Why Collisions Matter

In a dictionary/hash table, if two keys hash to the same position, we have a problem! We need strategies to handle this:

1. **Separate chaining** - Store multiple values in a list at that position
2. **Open addressing** - Find another empty position
3. **Linear probing** - Check the next positions sequentially

---

## What is a Hash Fingerprint?

We think of a hash as a **"fingerprint"** of the data:

- **Same data** → Always same fingerprint
- **Different data** → Almost always different fingerprint
- **Can't recover original** → Like a fingerprint, you can't reconstruct a person from their fingerprint alone

This makes hashes useful for:
- Detecting if data has changed
- Identifying files without comparing entire contents
- Quick comparisons and lookups

---

## Common Hash Functions

### MD5 (Message Digest 5)
- Output: 128-bit (32 hexadecimal characters)
- **Status:** DEPRECATED (vulnerable to collision attacks)
- **Use:** File integrity checks (not for security)

```
MD5("hello") = 5d41402abc4b2a76b9719d911017c592
```

### SHA-1 (Secure Hash Algorithm 1)
- Output: 160-bit (40 hexadecimal characters)
- **Status:** DEPRECATED (for cryptographic use)
- **Use:** Legacy systems only

```
SHA-1("hello") = aaf4c61ddcc5e8a2dabede0f3b482cd9aea9434d
```

### SHA-256 (Part of SHA-2)
- Output: 256-bit (64 hexadecimal characters)
- **Status:** SECURE (current standard)
- **Use:** Modern cryptographic applications, blockchain

```
SHA-256("hello") = 2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824
```

### Custom Hash Functions
For non-cryptographic uses (like dictionaries), simple custom functions are often used:

```python
def simple_hash(string):
    """Simple hash function for demonstration"""
    hash_value = 0
    for char in string:
        hash_value = (hash_value * 31 + ord(char)) % 1000000
    return hash_value
```

This is fast but has more collisions than cryptographic functions.

---

## Use Cases for Hashing

### Use Case 1: Dictionaries and Hash Tables

Create fast O(1) lookups using arbitrary keys:

```python
# Without hashing: need to search linearly
users = [("alice", 25), ("bob", 30), ("charlie", 35)]
# Finding bob: O(n) search

# With hashing: use key as lookup
users_dict = {
    "alice": 25,
    "bob": 30,
    "charlie": 35
}
# Finding bob: hash("bob") → index → O(1) lookup!
```

**How it works:**
1. Hash the key: `hash("bob") = 12345`
2. Use hash as array index: `users_array[12345 % array_size]`
3. Store value there
4. Lookup is instant!

### Use Case 2: Detecting Tampering / Man-in-the-Middle Attacks

Download sites publish file hashes to verify integrity:

```
File: awesome_game.exe (500 MB)
Expected SHA-256: a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6

Steps:
1. Download the file
2. Hash it on your computer
3. Compare your hash to expected hash
4. If they match: ✓ File is safe, not modified
5. If they differ: ✗ Someone injected malware!
```

ISPs or attackers can't intercept and modify the file without changing the hash (that's how good hashing is!).

### Use Case 3: Digital Signatures and Authentication

Hash a message, sign the hash with a private key:

```
Message: "Transfer $100 to Alice"
Hash: 4f3e2d1c0b9a8f7e6d5c4b3a

Sign with private key:
Signature: (encrypted hash)

Verification:
1. Hash the message
2. Decrypt signature with public key
3. Compare: if they match, message is authentic and unmodified
```

### Use Case 4: Password Storage

Don't store passwords directly. Store their hashes:

```python
# During signup
password = "MyPassword123"
stored_hash = hash(password)  # Store this, not the password

# During login
user_input = "MyPassword123"
if hash(user_input) == stored_hash:
    print("Login successful!")
else:
    print("Wrong password")
```

Even if the database is hacked, attackers get hashes, not passwords!

---

## Properties of Good Hash Functions

### For Dictionaries/Hash Tables

**Fast:** Should compute quickly, not slowly
```python
# Good: O(1) computation
def hash_simple(key):
    return sum(ord(c) for c in key) % 1000

# Bad: O(n) computation
def hash_slow(key):
    total = 0
    for c in key:
        time.sleep(1)  # Very slow!
        total += ord(c)
    return total
```

**Uniform Distribution:** Should spread keys evenly across hash space
```python
# Good: keys distributed evenly
keys = ["a", "b", "c", "d", "e"]
hashes = [1, 200, 401, 602, 803]  # Spread out!

# Bad: keys clustered
hashes = [1, 2, 3, 4, 5]  # All in one area, collisions!
```

**Deterministic:** Same input always gives same output
```python
hash("apple") = 5381  # Always
hash("apple") = 5381  # Always
hash("apple") = 5381  # Always
```

### For Cryptographic Use

**One-way:** Cannot reverse to get original
**Collision-resistant:** Hard to find two inputs with same hash
**Avalanche effect:** Small change in input causes large change in hash

```python
hash("cat")  = abc123def456
hash("cats") = xyz789uvw012  # Completely different!
```

---

## Hash Tables Under the Hood

A simple hash table implementation:

```python
class SimpleHashTable:
    def __init__(self, size=100):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        """Convert key to index"""
        return hash(key) % self.size

    def set(self, key, value):
        """Store key-value pair"""
        index = self.hash_function(key)
        self.table[index] = value

    def get(self, key):
        """Retrieve value by key"""
        index = self.hash_function(key)
        return self.table[index]

# Usage
ht = SimpleHashTable()
ht.set("name", "Alice")
ht.set("age", 30)

print(ht.get("name"))  # "Alice" - O(1) lookup!
print(ht.get("age"))   # 30 - O(1) lookup!
```

---

## Common Hash Function Attacks

### Birthday Attack (Collision Finding)

Even with 256-bit hashes, you only need ~2^128 attempts to find a collision (not 2^256).

This is why hash functions need sufficient output size.

### Rainbow Tables (Password Cracking)

Pre-compute hashes of common passwords:

```
Dictionary of hashes:
"password" → 5f4dcc3b5aa765d61d8327deb882cf99
"123456"   → e06d9c8aac409b9e8e3a7c5e8a7f47d0
"qwerty"   → 6512bd43d9caa6e02c990b0a82652dca
...
```

**Defense:** Use **salts** (random data added to password before hashing)

```python
# Without salt
hash("password") = 5f4dcc3b5aa765d61d8327deb882cf99
# Vulnerable to rainbow tables

# With salt
salt = "random_salt_123"
hash("password" + salt) = a9b3c8d1e5f7g9h2j4k6m8n0
# Different salt = different hash, rainbow tables useless!
```

---

## Real-World Applications

### 1. Blockchain / Bitcoin
Uses SHA-256 to hash blocks and maintain chain integrity

### 2. Git Version Control
Uses SHA-1 to identify commits uniquely

### 3. Database Indexing
Uses hashing for fast lookups on primary keys

### 4. Content Delivery Networks (CDNs)
Hashes requests to distribute load across servers

### 5. Caching
Hashes are used to determine which cache to store data in

### 6. Deduplication
Uses hashing to find and eliminate duplicate files

---

## Hash Function Performance

### Time Complexity

For hash-based data structures:
- **Insert:** O(1) average case, O(n) worst case (many collisions)
- **Lookup:** O(1) average case, O(n) worst case
- **Delete:** O(1) average case, O(n) worst case

### Space Complexity

- **Space:** O(n) for storing n key-value pairs
- Additional space depends on collision resolution strategy

---

## Key Insights

1. **Fingerprints, not encryption** - Hashes are one-way functions
2. **Fast and fixed-size** - Quick to compute, output size is constant
3. **Collisions are inevitable** - But with good functions, they're rare
4. **Applications vary** - Security hashing differs from dictionary hashing
5. **Use with salt** - For passwords, always add a salt
6. **Choose wisely** - Use cryptographic hashes for security, simple ones for dicts

---

## Summary

| Aspect | Details |
|--------|---------|
| **Input** | Any data (string, file, number, etc.) |
| **Output** | Fixed-size string/number (fingerprint) |
| **Deterministic** | Same input → same output |
| **One-way** | Can't reverse to get original |
| **Fast** | Should compute in O(1) or O(k) where k is input size |
| **Collision Risk** | Different inputs can have same hash (rare with good functions) |
| **Main Uses** | Dictionaries, security, verification, deduplication |

---

## Next Steps

Now that you understand hashing and hash functions, the next reading will dive into:
- **Hash Tables** - The actual data structure
- Implementation details
- Collision handling strategies
- Performance characteristics
- When to use hash tables vs other structures


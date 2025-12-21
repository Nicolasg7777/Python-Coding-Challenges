# ===================================================================
# PROBLEM: Sum of Squares (HARD - 15 XP)
# ===================================================================
#
# A number is "squared" when it is multiplied by itself or taken to
# the second power (e.g., 4² = 4 x 4 = 16).
#
# Calculate the total of the squares of all integers from 1 to a
# user-provided number.
#
# REQUIREMENTS:
# 1. Ask the user for an integer with int(input())
# 2. Store the input in a 'number' variable
# 3. Define a 'total' variable with initial value of 0
# 4. Use a for loop and range() to calculate squares
# 5. Print the output as an integer value
#
# EXAMPLE:
# If number is 5, the total should be 55 because:
# 1² + 2² + 3² + 4² + 5² = 1 + 4 + 9 + 16 + 25 = 55
#
# KEY LEARNING:
# - The power operator: ** (NOT ^)
# - Accumulation: adding values to a running total
# - How variables persist across loop iterations
# - Understanding loop variable scope
# - Building mathematical calculations with loops
#
# ===================================================================
# UNDERSTANDING ACCUMULATION
# ===================================================================
#
# This problem teaches a CRITICAL concept: ACCUMULATION
#
# Accumulation is when you:
# 1. Start with an initial value (total = 0)
# 2. In each iteration, ADD something to that value
# 3. The value persists and grows with each iteration
#
# THIS IS NOT LIKE RESETTING:
# ❌ WRONG: total = 0 every iteration (starts over each time)
# ✅ RIGHT: total = 0 ONCE before loop, then accumulates
#
# EXAMPLE WITH number = 5:
#
# ITERATION 1: i = 1
#   Calculate: 1² = 1
#   Add to total: total = 0 + 1 = 1
#   total NOW equals 1 (and stays 1 until next iteration)
#
# ITERATION 2: i = 2
#   Calculate: 2² = 4
#   Add to total: total = 1 + 4 = 5  ← Notice: total started at 1, not 0!
#   total NOW equals 5
#
# ITERATION 3: i = 3
#   Calculate: 3² = 9
#   Add to total: total = 5 + 9 = 14  ← total started at 5, not 0!
#   total NOW equals 14
#
# ITERATION 4: i = 4
#   Calculate: 4² = 16
#   Add to total: total = 14 + 16 = 30  ← total started at 14, not 0!
#   total NOW equals 30
#
# ITERATION 5: i = 5
#   Calculate: 5² = 25
#   Add to total: total = 30 + 25 = 55  ← total started at 30, not 0!
#   total NOW equals 55
#
# THE KEY INSIGHT:
# total CARRIES OVER from one iteration to the next!
# It doesn't reset. It grows. That's accumulation.
#
# ===================================================================
# THE POWER OPERATOR: **
# ===================================================================
#
# Python uses ** for exponentiation (power)
# NOT ^ (which is XOR/bitwise operation)
#
# Examples:
# 2 ** 2 = 4    (2 to the power of 2)
# 3 ** 2 = 9    (3 to the power of 2)
# 5 ** 3 = 125  (5 to the power of 3)
# 10 ** 2 = 100 (10 squared)
#
# COMMON MISTAKE:
# ❌ 2 ^ 2 = 0  (This is XOR, NOT exponentiation!)
# ✅ 2 ** 2 = 4 (This IS exponentiation!)
#
# ===================================================================

user = int(input('give me a number: '))

total = 0

for i in range(1, user + 1):
  total = total + i**2

print(total)

# ===================================================================
# HOW THIS CODE WORKS:
# ===================================================================
#
# 1. user = int(input('give me a number: '))
#    - Asks the user for a number
#    - Converts it to an integer
#    - Stores in 'user' variable
#
# 2. total = 0
#    - Initialize accumulator to 0
#    - This only happens ONCE before the loop
#
# 3. for i in range(1, user + 1):
#    - Loop from 1 to user (inclusive)
#    - If user = 5, loop from 1 to 5
#
# 4. total = total + i**2
#    - Calculate i squared (i ** 2)
#    - Add it to the existing total
#    - Store the new sum back in total
#    - Example: if total=14 and i=4, then total = 14 + 16 = 30
#
# 5. print(total)
#    - After loop completes, print the final total
#    - For user=5, this prints 55
#
# ===================================================================
# VARIABLE PERSISTENCE ACROSS ITERATIONS
# ===================================================================
#
# One of the hardest concepts to understand is that variables
# keep their values between iterations!
#
# WRONG THINKING:
# "In each iteration, total resets to 0"
# ❌ NO! total only equals 0 ONCE at the very beginning
#
# CORRECT THINKING:
# "total starts at 0, then grows by adding squares each iteration"
# ✅ YES! Each iteration adds to the existing value
#
# This is why we call it ACCUMULATION - it accumulates!
#
# ===================================================================

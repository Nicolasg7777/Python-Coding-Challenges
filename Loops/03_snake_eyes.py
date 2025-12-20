# ===================================================================
# PROBLEM: Snake Eyes (MEDIUM - 10 XP)
# ===================================================================
#
# In dice games, "snake eyes" means rolling two 1s. Why is it called
# that? Because two small dots look like a pair of snake eyes. 🐍👀
#
# It's the lowest possible roll (1 + 1 = 2) and is seen as bad luck.
# Let's keep rerolling two dice until we get snake eyes.
#
# EXPECTED OUTPUT (example):
# Nope
# Nope
# Nope
# Nope
# Snake eyes!
#
# REQUIREMENTS:
# 1. Import the random module
# 2. Use random to "roll" two dice (die1 and die2)
#    Each die should be a random integer from 1 to 6
# 3. Store the sum in a variable named total
# 4. Use a while loop to keep rolling until total equals 2
# 5. While total is NOT 2, print 'Nope' and re-roll
# 6. When total IS 2, exit the loop and print 'Snake eyes!'
#
# KEY LEARNING:
# - While loops with condition checking
# - The CRITICAL importance of updating variables inside loops
# - Simulating dice rolls with random.randint()
# - Understanding when to re-run code in a loop
# - How changing variables affects loop conditions
#
# ===================================================================
# CRITICAL CONCEPT: WHY YOU MUST UPDATE VARIABLES IN THE LOOP
# ===================================================================
#
# This problem teaches one of the MOST IMPORTANT loop concepts!
#
# COMMON MISTAKE (INFINITE LOOP):
# ----
# die1 = random.randint(1, 6)
# die2 = random.randint(1, 6)
# total = die1 + die2
#
# while total != 2:
#     print("Nope")
#     # OOPS! We forgot to re-roll the dice!
#
# ----
#
# What happens?
# 1. Roll dice once: die1=3, die2=5, total=8
# 2. Check: Is 8 != 2? YES → Enter loop
# 3. Print "Nope"
# 4. Loop back to condition: Is 8 != 2? YES (still!)
# 5. Print "Nope" again
# 6. ... This repeats forever because total never changes!
# 7. INFINITE LOOP! 😱
#
# THE FIX: RE-ROLL INSIDE THE LOOP!
# ----
# while total != 2:
#     print("Nope")
#     die1 = random.randint(1, 6)    # ← RE-ROLL
#     die2 = random.randint(1, 6)    # ← RE-ROLL
#     total = die1 + die2             # ← RECALCULATE
#
# ----
#
# Now:
# 1. Roll dice once: die1=3, die2=5, total=8
# 2. Check: Is 8 != 2? YES → Enter loop
# 3. Print "Nope"
# 4. RE-ROLL dice: die1=2, die2=1, total=3
# 5. Loop back: Is 3 != 2? YES → Continue
# 6. Print "Nope"
# 7. RE-ROLL dice: die1=1, die2=1, total=2
# 8. Loop back: Is 2 != 2? NO → Exit loop
# 9. Print "Snake eyes!"
#
# This time the loop STOPS because total finally equals 2!
#
# ===================================================================
# UNDERSTANDING THE DICE ROLLS
# ===================================================================
#
# Snake Eyes = Rolling two 1s
#
# Possible dice outcomes:
# Die 1 can be: 1, 2, 3, 4, 5, or 6
# Die 2 can be: 1, 2, 3, 4, 5, or 6
#
# Total can range from 2 (1+1) to 12 (6+6)
#
# We want: die1 = 1 AND die2 = 1, so total = 2
#
# Why is this rare?
# - Probability: 1 in 36 (only 1 combination out of 36 possibilities)
# - That's why the program keeps rolling!
#
# ===================================================================
# STEP-BY-STEP EXECUTION EXAMPLE
# ===================================================================
#
# Let's trace through a possible execution:
#
# INITIAL ROLL:
# die1 = 4 (random)
# die2 = 3 (random)
# total = 7
#
# CONDITION CHECK: while 7 != 2: TRUE → Enter loop
#
# ITERATION 1:
#   print("Nope")
#   die1 = 2 (new random roll)
#   die2 = 5 (new random roll)
#   total = 7
#   Condition: while 7 != 2: TRUE → Continue
#
# ITERATION 2:
#   print("Nope")
#   die1 = 6 (new random roll)
#   die2 = 4 (new random roll)
#   total = 10
#   Condition: while 10 != 2: TRUE → Continue
#
# ITERATION 3:
#   print("Nope")
#   die1 = 1 (new random roll)
#   die2 = 1 (new random roll) ← FINALLY!
#   total = 2
#   Condition: while 2 != 2: FALSE → Exit loop
#
# print("Snake eyes!")
#
# Output:
# Nope
# Nope
# Nope
# Snake eyes!
#
# ===================================================================

import random

# assign value die1 and die 2 to a random dice roll
die1 = random.randint(1, 6)
die2 = random.randint(1, 6)
# add the random die rolls to a total value
total = die1 + die2

# while loop, while total is not equal to 2 give me Nope!
while total != 2:
  print("Nope")
  # assign value die1 and die 2 to a random dice roll
  die1 = random.randint(1, 6)
  die2 = random.randint(1, 6)
  # add the random die rolls to a total value
  total = die1 + die2

# once the answer is 2 exit the while loop and give me snake eyes!
print("Snake eyes!")

# ===================================================================
# KEY TAKEAWAYS:
# ===================================================================
#
# 1. INITIALIZATION: Roll the dice once BEFORE the loop
#    This gives the condition something to check
#
# 2. CONDITION: Check if total != 2
#    While total is NOT 2, keep looping
#
# 3. INSIDE THE LOOP - THE CRITICAL PART:
#    a) Print "Nope"
#    b) Re-roll die1
#    c) Re-roll die2
#    d) Recalculate total
#    All four steps are essential!
#
# 4. LOOP EXITS: When total == 2 (snake eyes!), the condition
#    becomes False and we exit the loop
#
# 5. AFTER THE LOOP: Print "Snake eyes!" - this runs once,
#    after the loop has completely finished
#
# 6. COMMON ERROR: If you forget to re-roll or recalculate inside
#    the loop, you create an INFINITE LOOP that never stops!
#
# ===================================================================

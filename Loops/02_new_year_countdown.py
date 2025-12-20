# ===================================================================
# PROBLEM: New Year Countdown (MEDIUM - 10 XP)
# ===================================================================
#
# Ring in the New Year! A New Year's Eve party doesn't feel complete
# without a countdown from 10 to 1.
#
# REQUIREMENTS:
# 1. Use a for loop that counts down from 10 to 1
# 2. Use the "step" value in range() to count backwards
# 3. Print the numbers from 10 to 1, each on its own line
# 4. When the loop finishes, print "Happy New Year! 🥳"
#
# EXPECTED OUTPUT:
# 10
# 9
# 8
# 7
# 6
# 5
# 4
# 3
# 2
# 1
# Happy New Year! 🥳
#
# KEY LEARNING:
# - FOR LOOPS: A different way to repeat code (compared to while loops)
# - RANGE FUNCTION: range(start, stop, step)
#   - start: where to begin
#   - stop: where to end (NOT inclusive - doesn't include this number)
#   - step: how much to change each iteration (negative = count backwards)
# - INDENTATION: Controls what code is inside vs outside the loop
# - Loop execution: What happens after the loop ends
#
# ===================================================================
# DETAILED EXPLANATION: FOR LOOPS vs WHILE LOOPS
# ===================================================================
#
# WHILE LOOP (from previous challenge):
#   - Repeats while a condition is True
#   - You manually update the loop variable
#   - Example: while answer != 'Yes': answer = input(...)
#
# FOR LOOP (this challenge):
#   - Repeats a specific number of times
#   - The loop variable is automatically updated
#   - Used when you know HOW MANY times to repeat
#   - Iterates through a sequence of values
#
# WHY USE A FOR LOOP HERE?
# We know exactly how many times to repeat: from 10 down to 1 (10 times)
# A for loop is perfect for this!
#
# ===================================================================
# UNDERSTANDING range(10, 0, -1)
# ===================================================================
#
# range() generates a sequence of numbers. It takes three parameters:
#
# range(start, stop, step)
#
# START (10):
#   - Where the counting begins
#   - The first value that n will have is 10
#
# STOP (0):
#   - Where the counting ends
#   - IMPORTANT: The stop value is NOT included!
#   - So range(10, 0, -1) goes 10, 9, 8, ..., 2, 1 (NOT 0)
#
# STEP (-1):
#   - How much to change n after each iteration
#   - Positive step: counts UP (1, 2, 3, ...)
#   - Negative step: counts DOWN (-1, -2, -3, ...)
#   - We use -1 to countdown by 1 each time
#
# VISUALIZING range(10, 0, -1):
#
# Iteration 1: n = 10 (start here)
# Iteration 2: n = 9  (step by -1)
# Iteration 3: n = 8  (step by -1)
# Iteration 4: n = 7  (step by -1)
# Iteration 5: n = 6  (step by -1)
# Iteration 6: n = 5  (step by -1)
# Iteration 7: n = 4  (step by -1)
# Iteration 8: n = 3  (step by -1)
# Iteration 9: n = 2  (step by -1)
# Iteration 10: n = 1 (step by -1)
# Loop ends (n would be 0, but 0 is the stop value so we don't go there)
#
# ===================================================================
# UNDERSTANDING INDENTATION
# ===================================================================
#
# This is CRITICAL and often causes confusion!
#
# Code INSIDE the loop (indented):
#   for n in range(10, 0, -1):
#     print(n)              ← This is INSIDE the loop (indented)
#
# This code runs EVERY time through the loop (10 times in this case)
#
# Code OUTSIDE the loop (NOT indented):
#   for n in range(10, 0, -1):
#     print(n)
#   print("Happy New Year! 🥳")  ← This is OUTSIDE the loop (not indented)
#
# This code runs ONCE after the loop finishes
#
# WHY IS THIS IMPORTANT?
# If you indented the Happy New Year message, it would print 10 times!
# (Once for each iteration of the loop)
#
# By keeping it at the same level as 'for', it only prints once,
# after all 10 iterations are complete.
#
# ===================================================================
# THE LOOP VARIABLE AND WHAT HAPPENS AFTER
# ===================================================================
#
# In: for n in range(10, 0, -1):
# The variable 'n' is automatically updated by the for loop
#
# - You don't need to manually update it like in while loops
# - Each iteration, n takes the next value from range(10, 0, -1)
# - You just use n inside the loop - don't reassign it!
#
# AFTER THE LOOP FINISHES:
# - The variable n still exists and still has the last value it had
# - In this case, n would be 1 (the last value in the countdown)
# - The Happy New Year message prints using whatever comes after
#
# ===================================================================

# For loop: 'n' takes each value from range(10, 0, -1)
# This means n will be: 10, 9, 8, 7, 6, 5, 4, 3, 2, 1
for n in range(10, 0, -1):
    # Inside the loop: print each number
    # This line runs 10 times, once for each value of n
    print(n)

# Outside the loop: print the celebration message
# This line runs ONCE, after the loop has finished all iterations
# Notice: No indentation before this line (same level as 'for')
print("Happy New Year! 🥳")

# ===================================================================
# KEY TAKEAWAYS:
# ===================================================================
#
# 1. FOR LOOPS are used when you know how many times to repeat
#    while LOOPS are used when you repeat until a condition is met
#
# 2. range(start, stop, step) generates a sequence:
#    - start: where to begin
#    - stop: where to end (NOT included)
#    - step: how much to change (negative to count down)
#
# 3. INDENTATION determines if code is INSIDE or OUTSIDE the loop:
#    - Indented code runs every iteration
#    - Non-indented code runs once, after the loop finishes
#
# 4. The loop variable (n) is automatically updated by the for loop
#    You don't need to manually update it!
#
# 5. COMMON MISTAKES:
#    - Indenting the "Happy New Year" message (makes it print 10 times)
#    - Using range(10, 11, -1) instead of range(10, 0, -1)
#      (The stop value must be less than start when counting down)
#    - Forgetting that range's stop value is NOT included
#
# ===================================================================

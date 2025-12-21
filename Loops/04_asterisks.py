# ===================================================================
# PROBLEM: Asterisks (MEDIUM - 10 XP)
# ===================================================================
#
# Use only a for loop with range() and print() to display a staircase
# of asterisks in the terminal.
#
# REQUIREMENTS:
# 1. Use a for loop with range()
# 2. Start with a single * in the first line
# 3. End with 24 total asterisks on the last line
# 4. Each * should have a space after it so they're spread out
# 5. Display a staircase pattern
#
# EXPECTED OUTPUT:
# *
# * *
# * * *
# * * * *
# * * * * *
# ... (continues)
# * * * * * * * * * * * * * * * * * * * * * * * *  (24 asterisks)
#
# KEY LEARNING:
# - Using for loops to create patterns
# - Understanding all three parameters of range()
# - String multiplication in Python
# - Building output dynamically based on loop variable
#
# ===================================================================
# UNDERSTANDING range(start, stop, step)
# ===================================================================
#
# The range() function has THREE parameters:
#
# range(start, stop, step)
#
# START:
#   - Where the counting begins
#   - In this problem: 1 (we start with 1 asterisk)
#
# STOP:
#   - Where the counting ends (NOT inclusive - doesn't include this)
#   - In this problem: 25 (we want to go up to 24, so stop at 25)
#   - Why 25? Because we want the last value to be 24
#   - range(1, 25) gives us: 1, 2, 3, ..., 23, 24
#
# STEP:
#   - How much to increment after each iteration
#   - Default is 1 (if you don't specify it)
#   - In this problem: 1 (count by 1s)
#
# EXAMPLES:
# range(1, 5)        → 1, 2, 3, 4
# range(1, 5, 1)     → 1, 2, 3, 4 (same as above, step=1 is default)
# range(1, 10, 2)    → 1, 3, 5, 7, 9 (count by 2s)
# range(10, 0, -1)   → 10, 9, 8, 7, 6, 5, 4, 3, 2, 1 (count backwards)
#
# ===================================================================
# STRING MULTIPLICATION - A POWERFUL PYTHON FEATURE
# ===================================================================
#
# In Python, you can multiply a string by an integer!
# This repeats (replicates) the string that many times.
#
# SYNTAX: string * number
#
# EXAMPLES:
# "* " * 1  → "* "           (1 asterisk with space)
# "* " * 2  → "* * "         (2 asterisks with space)
# "* " * 3  → "* * * "       (3 asterisks with space)
# "* " * 5  → "* * * * * "   (5 asterisks with space)
#
# How it works:
# "* " is a string containing one asterisk and one space
# When you multiply it by n, you get that string repeated n times
#
# This is PERFECT for our problem because:
# - We need 1 asterisk on line 1
# - We need 2 asterisks on line 2
# - We need n asterisks on line n
# - We can use "* " * n to create exactly that!
#
# ===================================================================
# HOW THE SOLUTION WORKS
# ===================================================================
#
# for n in range(1, 25, 1):
#     print("* " * n)
#
# ITERATION 1: n = 1
#   "* " * 1 = "* "
#   Output: *
#
# ITERATION 2: n = 2
#   "* " * 2 = "* * "
#   Output: * *
#
# ITERATION 3: n = 3
#   "* " * 3 = "* * * "
#   Output: * * *
#
# ITERATION 4: n = 4
#   "* " * 4 = "* * * * "
#   Output: * * * *
#
# ... continues ...
#
# ITERATION 24: n = 24
#   "* " * 24 = "* * * * * * * * * * * * * * * * * * * * * * * * "
#   Output: * * * * * * * * * * * * * * * * * * * * * * * *
#
# ===================================================================
# WHY EXPLICITLY WRITE range(1, 25, 1)?
# ===================================================================
#
# Technically, range(1, 25) works the same as range(1, 25, 1)
# because step=1 is the DEFAULT.
#
# But writing range(1, 25, 1) explicitly shows you understand
# that range() has THREE parameters: start, stop, and step.
#
# It's good practice to be explicit when learning, even if
# you can rely on defaults. This shows you understand the syntax!
#
# ===================================================================

for n in range(1, 25, 1):
  print('* ' * n)

# EXPLANATION:
# Each iteration goes is multiplied '* ' * n which would look like:
# * times n = *
# * times n = **
# * times n = ***
# * times n = ****
# and so on

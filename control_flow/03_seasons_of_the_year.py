# ===================================================================
# PROBLEM: Seasons of the Year (MEDIUM - 10 XP)
# ===================================================================
#
# Ah, the four seasons in the year — winter, spring, summer, or fall;
# all you have to do is call!
#
# REQUIREMENTS:
# 1. Ask the user the month number using the input() function
# 2. Check for the four seasons using if/elif/else with logical operators:
#    - month is 1, 2, 3 → print 'Winter 🌨️'
#    - month is 4, 5, 6 → print 'Spring 🌱'
#    - month is 7, 8, 9 → print 'Summer 🌞'
#    - month is 10, 11, 12 → print 'Autumn 🍂'
#    - Everything else → print 'Invalid'
#
# KEY LEARNING:
# - Using logical operators (or and and) in conditional statements
# - The 'or' operator: True if ANY condition is true
# - The 'and' operator: True if ALL conditions are true
# - When to use each operator based on your logic
# - Including emoji characters in Python strings
#
# LOGICAL OPERATORS - WHEN TO USE WHICH:
#
# OR (or):
#   - Use when you want to check if ANY of multiple conditions is true
#   - Example: "Is this January OR February OR March?"
#   - Syntax: if condition1 or condition2 or condition3:
#   - In this problem: if month == 1 or month == 2 or month == 3:
#   - This checks "Is month equal to 1 OR 2 OR 3?"
#
# AND (and):
#   - Use when you want to check if ALL conditions are true at the same time
#   - Example: "Is the age >= 18 AND have a valid ID?"
#   - Syntax: if condition1 and condition2:
#   - We DON'T use 'and' here because month can't be 1 AND 2 at same time!
#
# COMPARISON:
#   OR: Returns True if at least ONE condition is true
#   AND: Returns True only if ALL conditions are true
#
# EXAMPLES:
#   - OR: (5 == 5) or (5 == 6) → True (first condition is true)
#   - OR: (5 == 4) or (5 == 6) → False (both are false)
#   - AND: (5 == 5) and (5 < 10) → True (both conditions are true)
#   - AND: (5 == 5) and (5 > 10) → False (second condition is false)
#
# ===================================================================

# Prompt the user to enter a month number (1-12)
# The month represents which month of the year they want to check
month = int(input("Enter in a month number to get the season: "))

# Check if the month is in the winter months (1, 2, or 3)
# The 'or' operator checks if ANY of these conditions is true
# If month is 1 OR month is 2 OR month is 3, this block executes
if month == 1 or month == 2 or month == 3:
    print("Winter 🌨️")
# Check if the month is in the spring months (4, 5, or 6)
elif month == 4 or month == 5 or month == 6:
    print("Spring 🌱")
# Check if the month is in the summer months (7, 8, or 9)
elif month == 7 or month == 8 or month == 9:
    print("Summer 🌞")
# Check if the month is in the autumn/fall months (10, 11, or 12)
elif month == 10 or month == 11 or month == 12:
    print("Autumn 🍂")
# If none of the above conditions are true (month is not 1-12)
# This handles invalid inputs like 13, 0, -5, etc.
else:
    print("Invalid")

# ===================================================================
# BONUS: There's a more elegant way to write this using 'in' operator!
# You could write: if month in [1, 2, 3]: instead of chaining 'or'
# But using 'or' is perfectly fine and shows you understand logical ops!
# ===================================================================

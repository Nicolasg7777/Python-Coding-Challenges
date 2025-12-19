# ===================================================================
# PROBLEM: Snapple Facts (MEDIUM - 10 XP)
# ===================================================================
#
# Snapple is a famous tea drink brand from Queens, New York. Each
# bottle cap comes with a silly fun fact.
#
# REQUIREMENTS:
# 1. Use the random module to create a number from 0 to 5
# 2. Use an if/elif/else statement to print one of six random facts:
#    - 0: 'Flamingos turn pink from eating shrimp.'
#    - 1: 'The only food that doesn't spoil is honey.'
#    - 2: 'Shrimp can only swim backwards.'
#    - 3: 'A taste bud's life span is about 10 days.'
#    - 4: 'It is impossible to sneeze while sleeping.'
#    - 5: 'It is illegal to sing off-key in North Carolina.'
#
# KEY LEARNING:
# - Importing the random module with 'import random'
# - Using random.randint(a, b) to generate random integers
# - random.randint() includes BOTH endpoints (inclusive)
#    Example: random.randint(0, 5) generates 0, 1, 2, 3, 4, or 5
# - Using if/elif/else with multiple conditions
# - Comparing numbers with == operator
#
# RESEARCH NOTES:
# The Python random module provides several functions for generating
# random numbers. For generating random integers, the main options are:
# - randint(a, b): Returns random integer N where a <= N <= b
# - randrange(stop): Returns random from range(stop)
# - randrange(start, stop): Returns random from range(start, stop)
#
# We used randint(0, 5) because:
# 1. It's simple and readable
# 2. It generates integers between 0-5 inclusive
# 3. It matches our needs perfectly
#
# Reference: https://docs.python.org/3/library/random.html
#
# ===================================================================

# Import the random module to use its random number functions
import random

# Generate a random integer between 0 and 5 (inclusive)
# randint(0, 5) means the result can be 0, 1, 2, 3, 4, or 5
# Each number has an equal chance of being selected (1 in 6 chance)
number = random.randint(0, 5)

# Check if the random number is 0
if number == 0:
    print('Flamingos turn pink from eating shrimp.')
# Check if the random number is 1
elif number == 1:
    print('The only food that doesn\'t spoil is honey.')
# Check if the random number is 2
elif number == 2:
    print('Shrimp can only swim backwards.')
# Check if the random number is 3
elif number == 3:
    print('A taste bud\'s life span is about 10 days.')
# Check if the random number is 4
elif number == 4:
    print('It is impossible to sneeze while sleeping.')
# Check if the random number is 5
elif number == 5:
    print('It is illegal to sing off-key in North Carolina.')
# This else statement should never execute because randint(0,5)
# always returns a number between 0-5, but it's good practice to
# include it as a safety net for unexpected values
else:
    print('not a number from 0 to 5')

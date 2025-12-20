# ===================================================================
# PROBLEM: Planet Weights (HARD - 15 XP)
# ===================================================================
#
# The year is 2199... we have become an interplanetary species and
# can travel to other planets in the solar system! 🚀
#
# REQUIREMENTS:
# 1. Ask the user what their Earth weight is (as a float)
# 2. Ask the user for a planet number (as an int)
# 3. Use an if/elif/else statement to calculate the user's weight
#    on the destination planet using:
#    destination weight = Earth weight × relative gravity
#
# 4. Planet data (Number, Name, Relative Gravity):
#    1 - Mercury - 0.38
#    2 - Venus - 0.91
#    3 - Mars - 0.38
#    4 - Jupiter - 2.53
#    5 - Saturn - 1.07
#    6 - Uranus - 0.89
#    7 - Neptune - 1.14
#
# 5. If the user enters a planet number outside of 1-7,
#    print 'Invalid planet number'
#
# KEY LEARNING:
# - Using float() for decimal number input
# - Using int() for integer input
# - Multiple if/elif/else branches for different conditions
# - Calculating values based on user input
# - Using f-strings to format output with calculated values
# - IMPORTANT: Calculate the result in a variable FIRST,
#   then use it in the print statement (not inline)
#
# WHY CALCULATE IN A VARIABLE FIRST?
# Good practice reasons:
# 1. Makes the calculation explicit and easier to read
# 2. Separates the calculation from the output
# 3. Makes debugging easier if something goes wrong
# 4. Allows you to reuse the calculated value if needed
# 5. Shows you understand each step of the problem
#
# F-STRINGS:
# An f-string (formatted string literal) allows you to embed
# expressions inside curly braces {} within a string prefixed with 'f'
# Example: f'Value: {variable}' or f'Result: {5 * 3}'
# This makes it easy to include calculated values in output
#
# PHYSICS NOTE:
# Relative gravity represents how strong gravity is on each planet
# compared to Earth. A value of 0.38 means gravity is 38% as strong
# as Earth, so you'd weigh less. A value of 2.53 means gravity is
# 2.53 times stronger, so you'd weigh much more!
#
# ===================================================================

# Prompt the user to enter their weight on Earth as a float
# float() allows decimal numbers like 150.5, not just whole numbers
user = float(input("what is your weight in decimals: "))

# Prompt the user to choose a destination planet (1-7)
# int() converts it to a whole number for comparison
destination = int(input("give me your destination planet: "))

# Check if the user selected Mercury (planet 1)
if destination == 1:
    # Calculate the weight on Mercury (38% of Earth weight)
    # Storing in a variable makes the calculation explicit
    weight = user * 0.38
    # Use the calculated weight in the output
    print(f'this is your weight in Mercury: {weight}')
# Check if the user selected Venus (planet 2)
elif destination == 2:
    # Calculate the weight on Venus (91% of Earth weight)
    weight = user * 0.91
    print(f'this is your weight in Venus: {weight}')
# Check if the user selected Mars (planet 3)
elif destination == 3:
    # Calculate the weight on Mars (38% of Earth weight, same as Mercury!)
    weight = user * 0.38
    print(f'this is your weight in Mars:{weight}')
# Check if the user selected Jupiter (planet 4)
elif destination == 4:
    # Calculate the weight on Jupiter (253% of Earth weight - very heavy!)
    weight = user * 2.53
    print(f'this is your weight in Jupiter:{weight}')
# Check if the user selected Saturn (planet 5)
elif destination == 5:
    # Calculate the weight on Saturn (107% of Earth weight)
    weight = user * 1.07
    print(f'this is your weight in Saturn:{weight}')
# Check if the user selected Uranus (planet 6)
elif destination == 6:
    # Calculate the weight on Uranus (89% of Earth weight)
    weight = user * 0.89
    print(f'this is your weight in Uranus:{weight}')
# Check if the user selected Neptune (planet 7)
elif destination == 7:
    # Calculate the weight on Neptune (114% of Earth weight)
    weight = user * 1.14
    print(f'this is your weight in Neptune:{weight}')
# Handle invalid planet numbers (anything other than 1-7)
else:
    print('Invalid planet number')

# ===================================================================
# CHALLENGE: Try to refactor this code to reduce repetition!
# Hint: Could you use a dictionary to store planet data?
# Example approach:
#   planets = {1: ('Mercury', 0.38), 2: ('Venus', 0.91), ...}
#   Then check: if destination in planets:
# This would eliminate all the repetitive if/elif blocks!
# ===================================================================

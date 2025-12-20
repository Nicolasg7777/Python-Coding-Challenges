# ===================================================================
# PROBLEM: Are We There Yet? (MEDIUM - 10 XP)
# ===================================================================
#
# "Are we there yet?" is a phrase that has existed for as long as
# there are children, vehicles, and road trips.
#
# REQUIREMENTS:
# 1. Ask the user "Are we there yet?" using the input() function
# 2. Create a while loop that asks "Are we there yet?" again
# 3. Keep asking them over and over until they respond with "Yes"
# 4. When they answer "Yes", the program should stop
#
# EXAMPLE OUTPUT:
# Are we there yet? One more hour
# Are we there yet? Almost there
# Are we there yet? Don't make me pull over
# Are we there yet? Yes
#
# KEY LEARNING:
# - Understanding while loops and conditions
# - How conditions are evaluated (True/False)
# - Loop control: when loops start and when they stop
# - The importance of updating variables inside loops
# - The != operator (not equal to)
#
# ===================================================================
# DETAILED EXPLANATION OF WHILE LOOPS:
# ===================================================================
#
# A while loop repeats a block of code as long as a condition is True.
# When the condition becomes False, the loop stops.
#
# SYNTAX:
# while condition:
#     code to repeat
#
# HOW IT WORKS (STEP-BY-STEP):
#
# Step 1: Check the condition
#   - Python evaluates: Is the condition True or False?
#
# Step 2: If True, run the loop body
#   - Execute all the code inside the loop
#   - Then go back to Step 1
#
# Step 3: If False, skip the loop
#   - Jump to the code after the loop (if any)
#
# IMPORTANT: The condition is re-checked AFTER EACH LOOP!
# This is crucial - the variables inside the loop can change the
# condition, which determines if the loop continues or stops.
#
# IN THIS PROBLEM:
#
# Line 1: answer = ''
#   - Set answer to an empty string ''
#   - Why? Because we need a starting value BEFORE checking condition
#   - An empty string is NOT equal to 'Yes', so '' != 'Yes' is True
#
# Line 2: while answer != 'Yes':
#   - Read this as: "While answer is NOT equal to 'Yes'..."
#   - The != operator means "not equal to"
#   - This condition is True as long as the user hasn't typed 'Yes'
#
# Line 3: answer = input("Are we there yet? ")
#   - Ask the user for input
#   - Store their response in the answer variable
#   - This UPDATES answer with new information
#
# EXECUTION FLOW EXAMPLE:
#
# 1st check:  answer = '' → Is '' != 'Yes'? YES (True) → Ask user
#   User types: "One more hour" → answer = "One more hour"
#
# 2nd check:  answer = "One more hour" → Is "One more hour" != 'Yes'? YES (True) → Ask again
#   User types: "Almost there" → answer = "Almost there"
#
# 3rd check:  answer = "Almost there" → Is "Almost there" != 'Yes'? YES (True) → Ask again
#   User types: "Don't make me pull over" → answer = "Don't make me pull over"
#
# 4th check:  answer = "Don't make me pull over" → Is "Don't make me pull over" != 'Yes'? YES (True) → Ask again
#   User types: "Yes" → answer = "Yes"
#
# 5th check:  answer = "Yes" → Is 'Yes' != 'Yes'? NO (False) → STOP the loop!
#
# The loop stops because the condition is now False.
# Python moves past the while loop and the program ends.
#
# COMMON MISTAKE: What if you forgot to update answer inside the loop?
# If you didn't have: answer = input(...) inside the loop,
# then answer would stay as '' forever, and the loop would never stop!
# This creates an "infinite loop" - a loop that never ends.
#
# ===================================================================

# Initialize answer as an empty string before the loop
# This is necessary so the condition has a value to check
# An empty string '' is NOT equal to 'Yes', so the loop will run
answer = ''

# While loop: Keep running as long as answer is NOT 'Yes'
# This condition is re-checked after each iteration
while answer != 'Yes':
    # Ask the user "Are we there yet?" and store their response
    # This line is inside the loop, so it runs repeatedly
    # The response replaces the old value of answer
    answer = input("Are we there yet? ")

# After the loop ends (when user typed 'Yes'), the program continues here
# In this case, the program just ends since there's no more code

# ===================================================================
# KEY TAKEAWAYS:
# ===================================================================
#
# 1. INITIALIZATION: Set the variable BEFORE the loop
#    answer = '' gives it a starting value
#
# 2. CONDITION: The while condition is checked BEFORE each loop
#    while answer != 'Yes': reads "while answer is not 'Yes'"
#
# 3. UPDATE: Change the variable INSIDE the loop
#    answer = input(...) updates answer with new user input
#
# 4. LOOP STOPS WHEN: The condition becomes False
#    When answer == 'Yes', the condition answer != 'Yes' is False
#
# 5. COMMON ERROR: If you don't update the variable in the loop,
#    it will loop forever (infinite loop)!
#
# ===================================================================

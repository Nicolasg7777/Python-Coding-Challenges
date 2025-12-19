# ===================================================================
# PROBLEM: High School Grades (EASY - 5 XP)
# ===================================================================
#
# U.S. high schools typically last for four years, from freshman year
# to senior year.
#
# REQUIREMENTS:
# 1. Ask the user to enter their grade as an integer
# 2. Create a four-year high school grade system using if/elif/else:
#    - grade is 9, print 'Freshman'
#    - grade is 10, print 'Sophomore'
#    - grade is 11, print 'Junior'
#    - grade is 12, print 'Senior'
#    - Everything else is 'TBD'
#
# KEY LEARNING:
# - Input/output with int() and print()
# - If/elif/else conditional statements
# - String comparison with ==
# - IMPORTANT: Watch out for spelling! 'Sophomore' not 'Sophmore'
#
# ===================================================================

# Prompt the user to enter their grade and convert it to an integer
# int() converts the text input to a whole number so we can compare it
grade = int(input("give me your grade: "))

# Check if the grade is 9 (Freshman)
if grade == 9:
    print('Freshman')
# Check if the grade is 10 (Sophomore)
# Note: Use 'Sophomore' with correct spelling - this is what the problem expects!
elif grade == 10:
    print('Sophomore')
# Check if the grade is 11 (Junior)
elif grade == 11:
    print('Junior')
# Check if the grade is 12 (Senior)
elif grade == 12:
    print('Senior')
# If none of the above conditions are true, print TBD
# The 'else' statement catches any grade that isn't 9, 10, 11, or 12
else:
    print('TBD')

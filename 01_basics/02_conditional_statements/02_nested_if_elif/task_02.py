# Problem:
# An integer representing a person's age is given as input.
#
# Read the age and classify the person into one of the following groups:
#
# - If the age is less than 0 or greater than 120:
#     Output:
#     "Error: invalid age"
#
# - If the age is from 0 to 2 (inclusive):
#     Output:
#     "Infant"
#
# - If the age is from 3 to 12 (inclusive):
#     Output:
#     "Child"
#
# - If the age is from 13 to 17 (inclusive):
#     Output:
#     "Teenager"
#
# - If the age is from 18 to 64 (inclusive):
#     Output:
#     "Adult"
#
# - If the age is greater than 64:
#     Output:
#     "Senior"
#
# Example:
#
# Input:
# 0
#
# Output:
# Infant

age = int(input())

if age < 0 or age > 120:
    print("Error: invalid age")
elif age <= 2:
    print("Infant")
elif age <= 12:
    print("Child")
elif age <= 17:
    print("Teenager")
elif age <= 64:
    print("Adult")
else:
    print("Senior")
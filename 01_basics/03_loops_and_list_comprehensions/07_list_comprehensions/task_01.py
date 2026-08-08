# Input:
# Floating-point numbers separated by spaces.
#
# Task:
# Read the numbers and store them in a list named `lst`.
#
# Using list comprehension,
# create a new list named `lst_abs`
# containing the absolute values
# of all numbers from `lst`.
#
# The elements of `lst_abs`
# must be numbers, not strings.
#
# Print the resulting list:
#
# print(lst_abs)
#
# Example:
#
# Input:
# 5.56 -8.7 1.0 3.14 77.845
#
# Output:
# [5.56, 8.7, 1.0, 3.14, 77.845]

lst = list(map(float, input().split()))

lst_abs = [abs(value) for value in lst]

print(lst_abs)
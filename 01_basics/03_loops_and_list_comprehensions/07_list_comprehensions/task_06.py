# Input:
# Floating-point numbers separated by spaces.
#
# Task:
# Read the numbers and store them in a list named `lst`.
#
# Using list comprehension,
# create a new list named `lst_res`.
#
# The new list must contain only elements
# from `lst` whose integer part is even
# (divisible by 2).
#
# The original values must be kept unchanged.
#
# Print the elements of `lst_res`
# in one line separated by spaces.
#
# Example:
#
# Input:
# 5.3 -2.1 10.5 11.64 0.2
#
# Output:
# -2.1 10.5 0.2

lst = list(map(float, input().split()))

lst_res = [value for value in lst if int(value) % 2 == 0]

print(*lst_res)
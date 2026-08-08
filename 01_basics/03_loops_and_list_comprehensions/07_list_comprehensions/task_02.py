# Input:
# A seven-digit positive integer.
#
# Task:
# Read the number.
#
# Using list comprehension,
# create a list named `lst`
# containing all digits of the number.
#
# The elements of `lst`
# must be integers, not strings.
#
# Print the resulting list:
#
# print(lst)
#
# Example:
#
# Input:
# 4567397
#
# Output:
# [4, 5, 6, 7, 3, 9, 7]

N = str(input())

lst = [int(value) for value in N]

print(lst)
# Problem:
# Three integers are given as input on a single line,
# separated by spaces.
# Read these numbers and create a list named `lst`
# containing the values in the same order they were entered.
#
# Display the resulting list using:
#
# print(lst)
#
# Input:
# Three integers separated by spaces.
#
# Output:
# A list containing the input values in the same order.
#
# Example:
# Input:
# 8 11 3
#
# Output:
# [8, 11, 3]

lst = list(map(int, input().split()))

print(lst)
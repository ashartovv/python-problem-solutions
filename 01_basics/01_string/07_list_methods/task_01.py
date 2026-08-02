# Problem:
# A string containing integers separated by spaces is given as input.
#
# Read these numbers and store them in a list named `lst`
# as integers in the same order as they appear in the input.
#
# Check whether the first number of the list is not equal to the last number.
#
# If they are different, append `True` to the list.
# Otherwise, append `False`.
#
# The solution must be implemented without using conditional statements.
#
# Display the resulting list using:
#
# print(*lst)
#
# Input:
# A sequence of integers separated by spaces.
#
# Output:
# The original numbers followed by `True` or `False`.
#
# Example:
# Input:
# 8 12 2 -10 6
#
# Output:
# 8 12 2 -10 6 True

lst = list(map(int, input().split()))
lst.append(lst[0] != lst[-1])

print(*lst)
# Problem:
# A sequence of integers separated by spaces is given as input.
#
# Read these numbers and store them in a list named `lst`.
#
# Remove the last value from the list.
# If the removed value is odd, append the boolean value `True`
# to the end of the list; otherwise, append `False`.
#
# Display the resulting list using:
#
# print(*lst)
#
# The program must be implemented without using conditional statements.
#
# Input:
# A sequence of integers separated by spaces.
#
# Output:
# The modified list with True or False added at the end.
#
# Example:
# Input:
# 8 11 0 3 5 6
#
# Output:
# 8 11 0 3 5 False

lst = list(map(int, input().split()))

lst.append(lst[-1] % 2 != 0)
lst.pop(-2)

print(*lst)
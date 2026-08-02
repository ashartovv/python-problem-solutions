# Problem:
# A string containing the number of new channel subscribers
# for each day is given as input, with values separated by spaces.
#
# Read these numbers and store them in a list named `lst`
# as integers in the same order as they appear in the input.
#
# Then sort the elements of the list in descending order
# and display the result using:
#
# print(*lst)
#
# Input:
# A sequence of integers separated by spaces.
#
# Output:
# The list elements sorted in descending order,
# separated by spaces.
#
# Example:
# Input:
# 52 65 64 54 68 59 42 63
#
# Output:
# 68 65 64 63 59 54 52 42

lst = list(map(int, input().split()))
lst.sort(reverse = True)

print(*lst)
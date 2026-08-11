# Input:
#
# Two lists of integers are given, each on a separate line.
# The numbers in each line are separated by spaces.
#
# Read both sets of numbers and store them as separate lists or tuples.
#
# Using sets, select the unique numbers that are present in either
# the first or the second list, but not in both lists simultaneously.
#
# Display the result in ascending order, separated by spaces,
# using:
#
# print(*sorted(s))
#
# Here, s is the set containing the unique numbers that occur
# in only one of the two lists.
#
# Test data
#
# Input:
# 1 2 3 4 5
# 4 5 6 7 8
#
# Output:
# 1 2 3 6 7 8

A = tuple(map(int, input().split()))
B = tuple(map(int, input().split()))

s = set(A) ^ set(B)

print(*sorted(s))
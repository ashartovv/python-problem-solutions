# Input:
#
# Two lists of integers are given, each on a separate line.
# The numbers in each line are separated by spaces.
#
# Read both sets of numbers and store them as separate lists or tuples.
#
# Using sets, select the unique numbers that are present in the first
# list but absent from the second list.
#
# Display the result in ascending order, separated by spaces,
# using:
#
# print(*sorted(s))
#
# Here, s is the set containing the unique numbers from the first list
# that are not present in the second list.
#
# Test data
#
# Input:
# 8 5 3 5 -3 1
# 1 2 3 4
#
# Output:
# -3 5 8

A = tuple(map(int, input().split()))
B = tuple(map(int, input().split()))

s = set(A) - set(B)

print(*sorted(s))
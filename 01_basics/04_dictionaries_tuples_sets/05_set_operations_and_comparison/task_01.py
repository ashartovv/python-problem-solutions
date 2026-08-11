# Input:
#
# Two lists of integers are given, each on a separate line.
# The numbers in each line are separated by spaces.
#
# Read both sets of numbers and store them as separate lists or tuples
# of integers.
#
# Using sets, select only the unique numbers that are present
# in both lists simultaneously.
#
# Display the result in ascending order, separated by spaces,
# using:
#
# print(*sorted(s))
#
# Here, s is the set containing the unique numbers present
# in both lists.
#
# Note:
# The sorted() function and the * operator will be discussed later.
# For now, just remember this way of sorting and displaying collections.
#
# Test data
#
# Input:
# 8 11 12 15 -2
# 4 11 10 15 -5 1 -2
#
# Output:
# -2 11 15

A = tuple(map(int, input().split()))
B = tuple(map(int, input().split()))

s = set(A) & set(B)

print(*sorted(s))
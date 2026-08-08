# Input:
# A positive integer `N`.
#
# Task:
# Read the number.
#
# Using list comprehension,
# generate a nested list
# of size `N × N`.
#
# The first row
# must contain only 0s,
# the second row only 1s,
# the third row only 2s,
# and so on
# until the last row.
#
# Print the resulting matrix
# as a table of numbers.
#
# Example:
#
# Input:
# 4
#
# Output:
# 0 0 0 0
# 1 1 1 1
# 2 2 2 2
# 3 3 3 3

N = int(input())

[print(*[lst] * N) for lst in range(N)]
# Problem:
# A matrix of numbers consisting of three rows is given as input.
# The numbers in each row are separated by spaces.
#
# Read the rows using:
#
# r1 = input()  # first row
# r2 = input()  # second row
# r3 = input()  # third row
#
# Convert each row into a list of integers.
#
# Store these three lists, in order, inside a single
# two-dimensional (nested) list.
#
# Then display the last column of the matrix
# as three numbers separated by spaces.
#
# Input:
# Three rows of integers separated by spaces.
#
# Output:
# The last element from each row, separated by spaces.
#
# Example:
# Input:
# 8 11 12 1
# 9 4 36 -4
# 1 12 49 5
#
# Output:
# 1 -4 5

r1 = input().split()
r2 = input().split()
r3 = input().split()

print(r1[-1], r2[-1], r3[-1])

# Input:
#
# A list of integers is given on one line, separated by spaces.
# Read the numbers and store them in a list.
#
# Then, using a dictionary, select only the unique numbers.
# Create another list containing these unique numbers.
#
# The numbers in the new list must remain in the same order
# in which they appeared in the input.
#
# Print the unique numbers on one line, separated by spaces.
#
# Note:
# This task is usually solved using sets,
# but sets have not been covered yet, so use a dictionary instead.
#
# Test data
#
# Input:
# 8 11 -4 5 2 11 4 8
#
# Output:
# 8 11 -4 5 2 4

N = list(map(int, input().split()))

d = dict.fromkeys(N)

print(*d)
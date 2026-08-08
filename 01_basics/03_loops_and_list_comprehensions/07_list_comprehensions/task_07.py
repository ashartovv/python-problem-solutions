# Input:
# Two lists of integers of the same length.
# Each list is given on a separate line.
#
# Task:
# Read both lists and store them
# in two separate variables.
#
# Using list comprehension,
# create a third list containing
# the sum of corresponding elements
# from the two input lists.
#
# Print the elements of the resulting list
# in one line separated by spaces.
#
# Example:
#
# Input:
# 1 2 3 4 5
# 6 7 8 9 10
#
# Output:
# 7 9 11 13 15

lst_1 = list(map(int, input().split()))
lst_2 = list(map(int, input().split()))

lst_3 = [value + lst_2[index] for index, value in enumerate(lst_1)]

print(*lst_3)
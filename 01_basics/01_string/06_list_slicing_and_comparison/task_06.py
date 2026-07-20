# Problem:
# Declare the following list containing student grades:
#
# m = [2, 3, 5, 5, 2, 2, 3, 3, 4, 5, 4, 4]
#
# Using list slicing, select every other element starting from the last one.
#
# Display the resulting slice as a list.
#
# Input:
# No input.
#
# Output:
# The elements selected from the list starting from the end with a step of -2.
#
# Example:
# Output:
# [4, 4, 5, 3, 2, 5]

m = [2, 3, 5, 5, 2, 2, 3, 3, 4, 5, 4, 4]

print(m[::-2])
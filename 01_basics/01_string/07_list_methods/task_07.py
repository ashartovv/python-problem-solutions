# Problem:
# Student grades (numbers from 2 to 5) are given as input,
# separated by spaces.
#
# Read these numbers and save them in a list.
#
# Determine how many times the grade 2 appears in the list
# and display this number.
#
# Input:
# A sequence of grades separated by spaces.
#
# Output:
# The number of occurrences of the grade 2.
#
# Example:
# Input:
# 2 3 5 2 4 2 2 5
#
# Output:
# 4

grades = list(map(int, input().split()))

print(grades.count(2))
# Problem:
# Student grades (integers from 2 to 5) are given as input
# on a single line, separated by spaces.
# Read the grades and store them in a list using the following statement:
#
# marks = list(map(int, input().split()))
#
# Calculate the average grade of the `marks` list and display
# the result rounded to one decimal place.
#
# Input:
# Student grades separated by spaces.
#
# Output:
# The average grade rounded to one decimal place.
#
# Example:
# Input:
# 3 3 2 4 4 5 4 3 2
#
# Output:
# 3.3

marks = list(map(int, input().split()))

print(round(sum(marks) / len(marks), 1))
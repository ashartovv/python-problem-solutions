# Problem:
# Two integers are given as input, written on one line separated by a space.
# Read these numbers and create a new f-string containing the values
# in ascending order separated by a space.
# Display the resulting string.
#
# Note:
# Solve the task without using conditional statements.
#
# Input:
# Two integers separated by a space.
#
# Output:
# The two numbers in ascending order separated by a space.
#
# Example:
# Input:
# 15 8
#
# Output:
# 8 15

numbers = list(map(int, input().split()))

print(min(numbers), max(numbers))
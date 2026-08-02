# Problem:
# Two floating-point numbers are given in one line,
# separated by a space.
#
# Read these numbers and output the larger of the two.
#
# Solve the problem using a conditional statement (`if`).
#
# Input:
# Two floating-point numbers separated by a space.
#
# Output:
# The larger of the two numbers.
#
# Example:
# Input:
# 8.7 11.0
#
# Output:
# 11.0

num_1, num_2 = map(float, input().split())

if num_1 > num_2:
    print(num_1)
else:
    print(num_2)
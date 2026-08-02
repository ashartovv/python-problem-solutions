# Problem:
# Two real numbers are given, each on a separate line.
#
# Read these numbers and use the ternary conditional operator
# to find the largest one and assign it to the variable d.
#
# Output the value of the variable d.
#
# Example:
#
# Input:
# 5.4
# -3.8
#
# Output:
# 5.4

num_1 = float(input())
num_2 = float(input())

d = num_1 if num_1 > num_2 else num_2

print(d)
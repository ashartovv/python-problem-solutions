# Input:
#
# Declare the following tuple:
#
# t = (3.4, -56.7)
#
# A sequence of integers separated by spaces is given as input.
#
# Read these integers and add them to the end of the tuple t.
#
# The added numbers must appear in the tuple in the same order
# in which they were read.
#
# Print the resulting tuple using:
#
# print(t)
#
# Test data
#
# Input:
# 8 11 -5 2
#
# Output:
# (3.4, -56.7, 8, 11, -5, 2)

t = (3.4, -56.7)
t = t + tuple(map(int, input().split()))

print(t)
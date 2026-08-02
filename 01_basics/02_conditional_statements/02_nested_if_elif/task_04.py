# Problem:
# Three integers are given in one line separated by spaces.
#
# Read these numbers and find the smallest one.
#
# Output the smallest value.
#
# Requirements:
# Use a conditional operator.
# Do not use the built-in min() function.
#
# Example:
#
# Input:
# 8 11 -1
#
# Output:
# -1

a, b, c = map(int, input().split())

if a <= c and a <= b:
    print(a)
elif b <= a and b <= c:
    print(b)
else:
    print(c)
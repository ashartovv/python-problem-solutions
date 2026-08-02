# Problem:
# Three integers (the lengths of a triangle's sides) are given in one line.
#
# Read them using:
#
# a, b, c = map(int, input().split())
#
# Determine:
#
# 1. Whether the lengths a, b, c can form a triangle.
#
# If they cannot form a triangle, output:
#
# "This is not a triangle"
#
# 2. If they can form a triangle, perform additional checks:
#
# - If all three sides are equal:
#     Output:
#     "Equilateral triangle"
#
# - If exactly two sides are equal:
#     Output:
#     "Isosceles triangle"
#
# - If all three sides are different:
#     Output:
#     "Scalene triangle"
#
# Example:
#
# Input:
# 10 2 4
#
# Output:
# This is not a triangle

a, b, c = map(int, input().split())

if a + b <= c or a + c <= b or c + b <= a:
    print("This is not a triangle")
elif a == b  == c:
    print("Equilateral triangle")
elif a == b or a == c or b == c:
    print("Isosceles triangle")
else:
    print("Scalene triangle")
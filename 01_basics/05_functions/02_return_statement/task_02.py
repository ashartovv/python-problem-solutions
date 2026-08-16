# Input:
# Three integer values representing the three sides of a triangle.
#
# Output:
# Declare a function named is_triangle that accepts three parameters.
# Check whether a triangle can be formed from these three sides.
# For a valid triangle, return True.
# Otherwise, return False.
#
# The function must not be called.
#
# Input:
# 3 4 5
#
# Output:
#

def is_triangle(a, b, c):
    side1 = (a + b) > c
    side2 = (b + c) > a
    side3 = (c + a) > b
    return side1 and side2 and side3
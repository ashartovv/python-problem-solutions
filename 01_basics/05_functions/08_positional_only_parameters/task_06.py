# Input:
# A single line containing the coordinates of four points of a quadrilateral.
#
# The coordinates are given in order and have the following format:
# x0=y0 x1=y1 x2=y2 x3=y3
#
# Define a function named is_right_rect with the following parameters:
# a, b, c, d — coordinates of the four vertices of a quadrilateral;
# positional arguments only.
# precision=0.001 — the allowed precision for determining whether
# the quadrilateral is a rectangle; keyword arguments only.
#
# The function must determine whether the quadrilateral formed by
# points a, b, c, d is a rectangle.
#
# The function should use the scalar product of vectors.
# For two vectors A = [a0, a1] and B = [b0, b1],
# their scalar product is:
# a0 * b0 + a1 * b1
#
# The length of a vector [a0, a1] is:
# sqrt(a0 ** 2 + a1 ** 2)
#
# The cosine of the angle between two vectors is:
# (a0 * b0 + a1 * b1) / (|A| * |B|)
#
# If two vectors are perpendicular, their cosine is 0.
# Therefore, two vectors are considered perpendicular if:
# abs(cos(alpha)) < precision
#
# Use this property to determine whether the quadrilateral
# is a rectangle with the given precision.
#
# Call is_right_rect using the four coordinates stored in rect_coords.
# Store the returned value in result.
#
# Test data:
#
# Input:
# 3=1 6=7 10=5 7=-1
#
# Output:
# No output.
import math

def is_right_rect(a, b, c, d, /, *, precision=0.001):
    for value in ((a, b, c), (b, c, d), (c, d, a), (d, a, b)):
        vector0 = (value[1][0] - value[0][0], value[1][1] - value[0][1])
        vector1 = (value[2][0] - value[1][0], value[2][1] - value[1][1])

        len0 = math.sqrt(vector0[0] ** 2 + vector0[1] ** 2)
        len1 = math.sqrt(vector1[0] ** 2 + vector1[1] ** 2)

        cos_a = (vector0[0] * vector1[0] + vector0[1] * vector1[1]) / (len0 * len1)

        if abs(cos_a) >= precision:
            return False

    return True


rect_coords = [(float(x.split('=')[0]), float(x.split('=')[1])) for x in input().split()]

result = is_right_rect(*rect_coords)
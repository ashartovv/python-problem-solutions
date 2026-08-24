# Input:
# Three floating-point numbers representing the side lengths of a triangle.
#
# Define the function is_right_tr(a, b, c, /, precision=0.001).
# Parameters a, b, and c must accept only positional arguments.
# precision must accept both positional and keyword arguments.
# Return True if the triangle is right-angled within the given precision,
# otherwise return False.
#
# A triangle is right-angled if at least one side satisfies the Pythagorean
# theorem within the allowed precision.
#
# Test data:
#
# Input:
# 3 4 5
#
# Output:
# No output.

def is_right_tr(a, b, c, /, precision=0.001):
    if abs(c ** 2 - (a ** 2 + b ** 2)) < precision:
        return True
    elif abs(a ** 2 - (b ** 2 + c ** 2)) < precision:
        return True
    elif abs(b ** 2 - (a ** 2 + c ** 2)) < precision:
        return True
    else:
        return False


side_a, side_b, side_c = map(float, input().split())
result = is_right_tr(side_a, side_b, side_c)
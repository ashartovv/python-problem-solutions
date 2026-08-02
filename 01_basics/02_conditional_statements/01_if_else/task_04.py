# Problem:
# Three positive integers are given in one line,
# separated by spaces.
#
# Read these numbers and check whether:
#
# - the first two numbers are the legs of a right triangle;
# - the third number is the hypotenuse.
#
# Use the Pythagorean theorem for the check:
#
# c² = a² + b²
#
# If the condition is true, output:
#
# YES
#
# Otherwise, output:
#
# NO
#
# Example:
#
# Input:
# 3 4 5
#
# Output:
# YES

leg_1, leg_2, hypotenuse = map(int, input().split())

if hypotenuse ** 2 == leg_1 ** 2 + leg_2 ** 2:
    print("YES")
else:
    print("NO")
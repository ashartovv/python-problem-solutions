# Input:
# A real number is given as input.
# Read the number, import only the floor() function from the math module,
# call it with the input number, and display the result.
#
# Test data:
# Input:
# 5.8
#
# Output:
# 5

from math import floor

value = float(input())
print(floor(value))
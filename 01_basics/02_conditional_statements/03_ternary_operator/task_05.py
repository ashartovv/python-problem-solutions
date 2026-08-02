# Problem:
# An integer is given as input: the current time in seconds
# in the range [0; 59].
#
# Read this value and calculate the next value in seconds,
# taking into account the range boundaries [0; 59].
#
# If the input value is 59, the next value should be 0.
# The process repeats cyclically.
#
# Implement the program using the ternary conditional operator.
#
# Output the resulting next value.
#
# Example:
#
# Input:
# 55
#
# Output:
# 56

number_1 = int(input())
seconds = 0 if number_1 >= 59 else number_1 + 1

print(seconds)


# Solution using only arithmetic operations.

number_2 = int(input())
second = (number_2 + 1) % 60

print(second)
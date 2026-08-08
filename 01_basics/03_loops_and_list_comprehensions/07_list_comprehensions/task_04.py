# Input:
# A positive integer `n`.
#
# Task:
# Read the number.
#
# Using list comprehension,
# create a list containing
# all divisors of `n`
# (including `n` itself).
#
# A divisor of `n`
# is an integer that divides `n`
# without a remainder.
#
# Print the elements
# of the resulting list
# in one line separated by spaces.
#
# Example:
#
# Input:
# 10
#
# Output:
# 1 2 5 10

n = int(input())

dividers = [value for value in range(1, n + 1) if n % value == 0]

print(*dividers)
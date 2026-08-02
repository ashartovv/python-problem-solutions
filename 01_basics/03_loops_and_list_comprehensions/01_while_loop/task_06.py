# Problem:
# A natural number (a positive integer) with three or more digits
# is given as input.
#
# Read this number and find the product of all its digits.
#
# Output the result (the product).
#
# Implement the program using a while loop.
#
# Example:
#
# Input:
# 821
#
# Output:
# 16

n = int(input())
summ = 1

while n:
    summ *= n % 10
    n //= 10

print(summ)

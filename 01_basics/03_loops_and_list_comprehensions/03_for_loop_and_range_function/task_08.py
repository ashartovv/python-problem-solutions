# Problem:
# A natural number n is given as input.
#
# Read this number and, using a for loop, find all divisors of this number
# (that is, integers from 1 to n that divide n without a remainder).
#
# Print the found divisors immediately, one per line,
# without creating a list.
#
# Example:
#
# Input:
# 12
#
# Output:
# 1
# 2
# 3
# 4
# 6
# 12

n = int(input())

for x in range(1, n + 1):
    if n % x == 0:
        print(x)
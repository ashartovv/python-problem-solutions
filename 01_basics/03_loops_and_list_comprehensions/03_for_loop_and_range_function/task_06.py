# Problem:
# A natural number n is given as input.
#
# Read this number and calculate the sum of all natural numbers
# less than n that are multiples of either 3 or 5.
#
# Output the resulting sum.
#
# Example:
#
# Input:
# n = 10
#
# The numbers are:
# 3, 5, 6, 9
#
# Their sum is:
# 23
#
# Output:
# 23

n = int(input())
s = 0

for x in range(1, n):
    if x % 3 == 0 or x % 5 == 0:
        s += x

print(s)
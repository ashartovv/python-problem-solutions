# Problem:
# A natural number n is given as input.
#
# Read this number and, using a for loop, determine whether it is prime
# (that is, it is divisible only by itself and by 1).
#
# Output:
# "YES" if n is prime,
# "NO" otherwise.
#
# Example:
#
# Input:
# 11
#
# Output:
# YES

n = int(input())
result = "NO"
count = 0

for x in range(1, n + 1):
    if n % x == 0:
        count += 1

if count == 2:
    result = "YES"

print(result)
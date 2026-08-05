# Input: a positive integer n.
#
# Read n and find all prime numbers
# in the range [2, n).
#
# A prime number is a number greater than 1
# that is divisible only by 1 and itself.
#
# Print all found prime numbers
# on one line separated by spaces.
#
# Example:
#
# Input:
# 11
#
# Output:
# 2 3 5 7

n = int(input())


for index in range(2, n):
    is_prime = True
    for prime in range(2, index):
        if index % prime == 0:
            is_prime = False
            break
    if is_prime:
        print(index, end=' ')
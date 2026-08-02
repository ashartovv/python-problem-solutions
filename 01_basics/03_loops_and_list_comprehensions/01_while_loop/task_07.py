# Problem:
# The Fibonacci sequence is formed as follows:
# the first two numbers are equal to 1 and 1,
# and each next number is the sum of the two previous numbers.
#
# The sequence looks like:
# 1, 1, 2, 3, 5, 8, 13, ...
#
# A positive integer n (n >= 2) is given as input.
#
# Read this number and create a Fibonacci sequence of length n.
#
# Output the sequence as a string of numbers separated by spaces.
#
# Implement the program using a while loop.
#
# Example:
#
# Input:
# 8
#
# Output:
# 1 1 2 3 5 8 13 21

n = int(input())
fibonacci = [1, 1]
i = 2

while i < n:
    fibonacci.append(fibonacci[-2] + fibonacci [-1])
    i += 1

print(*fibonacci)
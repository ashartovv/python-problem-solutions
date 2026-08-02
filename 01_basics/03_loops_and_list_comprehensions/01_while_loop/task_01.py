# Problem:
# Two positive integers n and m are given as input,
# written in one line separated by a space, where n < m.
#
# Read these numbers and output, in one line separated by spaces,
# the squares of all integers in the range [n; m].
#
# Implement the program using a while loop.
#
# Example:
#
# Input:
# 2 4
#
# Output:
# 4 9 16

n, m = map(int, input().split())
square = []
i = n

while i <= m:
    square.append(i**2)
    i += 1

print(*square)
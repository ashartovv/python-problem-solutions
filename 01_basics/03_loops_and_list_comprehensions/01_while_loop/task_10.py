# Problem:
# Two positive integers n and m are given in one line separated by a space,
# where n < m.
#
# Read these numbers and print all odd numbers
# from the interval [n, m].
#
# Solve the problem without using any conditional statements.
#
# Output the numbers in one line separated by spaces.
#
# Implement the program using a while loop.
#
# Example:
#
# Input:
# 2 10
#
# Output:
# 3 5 7 9

n, m = map(int, input().split())

n += (n + 1) % 2

while n <= m:
    print(n, end=" ")
    n += 2
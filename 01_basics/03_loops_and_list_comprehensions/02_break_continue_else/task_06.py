# Problem:
# A natural number n is given as input.
#
# Read this number and find the first natural number
# (starting the search from 1) whose square is greater than n.
#
# Output the found number.
#
# Implement the program using a while loop.
#
# Example:
#
# Input:
# 10
#
# Output:
# 4

n = int(input())
i = 0

while i <= n:
    if (i + 1) ** 2 > n:
        print(i + 1)
        break

    i += 1
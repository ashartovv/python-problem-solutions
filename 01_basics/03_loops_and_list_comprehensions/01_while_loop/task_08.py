# Problem:
# A positive integer n (the number of hours) is given as input.
#
# Read this number and save it in the variable n.
#
# A single-celled amoeba divides into 2 cells every 3 hours.
# Determine how many cells there will be after n hours.
#
# Assume that initially there was 1 amoeba.
#
# Output the final number of cells.
#
# Implement the program using a while loop.
#
# Example:
#
# Input:
# 11
#
# Output:
# 8

n = int(input())
cycles = n // 3
cells = 1
i = 0
while i < cycles:
    i += 1
    cells *= 2

print(cells)
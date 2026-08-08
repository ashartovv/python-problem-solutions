# Input:
# A positive integer N.
#
# Task:
# Read N.
#
# Using list comprehension,
# create an N × N matrix.
#
# Fill the matrix with 0s,
# but place 1s on the main diagonal.
#
# (The main diagonal consists of elements
# from the top-left corner to the bottom-right corner.)
#
# Print the matrix as a table of numbers.
#
# Example:
#
# Input:
# 4
#
# Output:
# 1 0 0 0
# 0 1 0 0
# 0 0 1 0
# 0 0 0 1

N = int(input())

matrix = [
    [1 if col == row else 0 * col
    for col in range(N)]
    for row in range(N)
]

for row in matrix:
    print(*row)
# Input: a positive integer N.
#
# Read N and create a two-dimensional (nested) list
# of size N x N filled with 1s.
#
# Then replace all elements in the last column with 5s.
#
# Print the resulting matrix as a table of numbers.
#
# There must be no trailing spaces at the end of each line.
#
# Example:
#
# Input:
# 4
#
# Output:
# 1 1 1 5
# 1 1 1 5
# 1 1 1 5
# 1 1 1 5

N = int(input())

matrix = [[1] * N for _ in range(N)]

for row in range(N):
    for column in range(N):
        if column == N - 1:
            matrix[row][column] = 5
            print(matrix[row][column])
        else:
            print(matrix[row][column], end=' ')
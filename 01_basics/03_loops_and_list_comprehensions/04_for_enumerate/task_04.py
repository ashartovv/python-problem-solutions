# Create a square two-dimensional table `matrix` of size N x N,
# where N is a positive integer read from input:
#
# N = int(input())
#
# The matrix must be represented as a nested list and contain integers
# starting from 1 in increasing order, arranged in a spiral ("snake") pattern.
#
# Example for N = 5:
#
# matrix = [
#     [1, 2, 3, 4, 5],
#     [16, 17, 18, 19, 6],
#     [15, 24, 25, 20, 7],
#     [14, 23, 22, 21, 8],
#     [13, 12, 11, 10, 9]
# ]
#
# Print the matrix:
#
# for row in matrix:
#     print(' '.join(str(num) for num in row))

N = int(input())

matrix = [[0] * N for _ in range(N)]

count = 1

top = 0
bottom = N - 1
left = 0
right = N - 1

while top <= bottom and left <= right:

    # right
    for col in range(left, right + 1):
        matrix[top][col] = count
        count += 1
    top += 1

    # down
    for row in range(top, bottom + 1):
        matrix[row][right] = count
        count += 1
    right -= 1

    # left
    if top <= bottom:
        for col in range(right, left - 1, -1):
            matrix[bottom][col] = count
            count += 1
        bottom -= 1

    # up
    if left <= right:
        for row in range(bottom, top - 1, -1):
            matrix[row][left] = count
            count += 1
        left += 1


for row in matrix:
    print(' '.join(str(num) for num in row))
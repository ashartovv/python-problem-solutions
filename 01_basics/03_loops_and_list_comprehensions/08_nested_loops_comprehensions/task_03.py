# Input:
# A sequence of integers separated by spaces.
#
# Task:
# Read the numbers and store them in a list.
#
# Using list comprehension,
# create a two-dimensional list `lst`
# with size N × N (a square matrix).
#
# It is guaranteed that the amount of input numbers
# can be arranged into a square matrix.
#
# Print the resulting nested list:
#
# print(lst)
#
# Example:
#
# Input:
# 1 2 3 4 5 6 7 8 9
#
# Output:
# [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

import math

N = list(map(int, input().split()))

matrix_len = math.sqrt(len(N))

lst = [
    [
        N[row * int(matrix_len) + col]
        for col in range(int(matrix_len))
    ]
    for row in range(int(matrix_len))
]

print(lst)
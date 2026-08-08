# Input:
# A two-dimensional table of integers.
#
# The input is already read and stored in the nested list `lst_in`:
#
# s = sys.stdin.readlines()
# lst_in = [list(map(int, x.strip().split())) for x in s]
#
# Task:
# Transpose the matrix `lst_in`
# (replace rows with columns and columns with rows).
#
# Save the resulting matrix in the list `A`.
#
# Display the resulting matrix using:
#
# for row in A:
#     print(*row)
#
# Try to solve the task using list comprehension
# without rewatching the lesson.
#
# Example:
#
# Input:
# 1 2 3
# 4 5 6
# 7 8 9
# 5 4 3
#
# Output:
#1 4 7 5
#2 5 8 4
#3 6 9 3

import sys

s = sys.stdin.readlines()
lst_in = [list(map(int, x.strip().split())) for x in s]

A = [
    [
        lst_in[col][row]
        for col in range(len(lst_in))
    ]
    for row in range(len(lst_in[0]))
]

for row in A:
    print(*row)
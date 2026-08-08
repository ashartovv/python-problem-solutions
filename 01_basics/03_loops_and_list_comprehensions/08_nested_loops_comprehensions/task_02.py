# Input:
# A two-dimensional table of integers.
#
# The table is already read and stored
# in a nested list named `lst_in`:
#
# s = sys.stdin.readlines()
# lst_in = [list(map(int, x.strip().split())) for x in s]
#
# Task:
# Using list comprehension,
# convert the two-dimensional list `lst_in`
# into a one-dimensional list.
#
# The elements must appear
# in reverse order.
#
# Print the resulting sequence
# in one line separated by spaces.
#
# Example:
#
# Input:
# 1 2 3 4
# 5 6 7 8
# 9 8 7 6
# 5 4 3 2
#
# Output:
# 2 3 4 5 6 7 8 9 8 7 6 5 4 3 2 1

import sys

s = sys.stdin.readlines()
lst_in = [list(map(int, x.strip().split())) for x in s]


one_dim = [
    value
    for row in lst_in[::-1]
    for value in row[::-1]
]

print(*one_dim)
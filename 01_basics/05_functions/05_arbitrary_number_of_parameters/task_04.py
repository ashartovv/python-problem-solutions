# Input:
# A table of integers is given as a two-dimensional nested list lst2D
# of size N x N. N is determined from the input data.
#
# The table contains zeros and some ones.
#
# Using a function named verify, which receives the two-dimensional
# list lst2D as its first parameter, check whether all ones are isolated
# from each other.
#
# A one is considered isolated if all cells surrounding it contain zeros.
#
# Recommended algorithm:
# In verify, iterate through the two-dimensional list.
# For every element with the value 1, call an auxiliary function
# named is_isolate to check whether this one is isolated.
#
# The is_isolate function must return True if the one is isolated
# and False otherwise.
#
# As soon as a non-isolated one is found, verify must return False.
# If all ones are isolated, verify must return True.
#
# Do not call verify, only define the required functions.
#
# Test data:
#
# Input:
# 1 0 0 0 0
# 0 0 1 0 0
# 0 0 0 0 0
# 0 1 0 1 0
# 0 0 0 0 0
#
# Output:
# No output.

import sys


def is_isolate(lst, row, col):
    checking_coords = [
        (row - 1, col - 1), (row - 1, col), (row - 1, col + 1),
        (row, col - 1),                         (row, col + 1),
        (row + 1, col - 1), (row + 1, col), (row + 1, col + 1)
    ]
    for coord in checking_coords:
        if (0 <= coord[0] < len(lst)) and (0 <= coord[1] < len(lst)):
            if lst[coord[0]][coord[1]] == 1:
                return False

    return True


def verify(lst):
    result = True
    for row_i, row in enumerate(lst):
        for col_i, col_v in enumerate(row):
            if (col_v == 1) and (is_isolate(lst, row_i, col_i) == False):
                result = False
                break
    return result


lines = sys.stdin.readlines()
lst2D = [list(map(int, x.strip().split())) for x in lines]
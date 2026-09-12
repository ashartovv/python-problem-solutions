# Input:
# The program receives a table of integers.
# Each row of the table is read as a separate line.
#
# The input lines are stored in the list lst_in using:
# lst_in = list(map(str.strip, sys.stdin.readlines()))
#
# Use the map() function and a list comprehension
# to convert the strings in lst_in into a two-dimensional list
# named lst2D containing integers instead of strings.
#
# The original list lst_in must remain unchanged.
#
# Do not display anything on the screen.
# Only create the list lst2D based on the input data.
#
# Example:
#
# Input:
# 8 11 -5
# 3 4 10
# -1 -2 3
# 4 5 6
#
# Result:
# lst2D = [[8, 11, -5], [3, 4, 10], [-1, -2, 3], [4, 5, 6]]
#
# Input:
# 8 11 -5
# 3 4 10
# -1 -2 3

import sys

lst_in = list(map(str.strip, sys.stdin.readlines()))
lst2D = list(map(lambda x:list(map(int, x.split())), lst_in))
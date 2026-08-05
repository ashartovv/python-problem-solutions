# Input: a 5 × 5 matrix consisting of 0s and 1s.
#
# The input is already read and stored in:
# s = sys.stdin.readlines()
# lst_in = [list(map(int, x.strip().split())) for x in s]
#
# Check whether any 1s touch each other
# horizontally, vertically, or diagonally.
#
# Every 1 must be surrounded only by 0s.
#
# Print:
# "YES" if the condition is satisfied,
# otherwise print "NO".
#
# Example:
#
# Input:
# 1 0 0 0 0
# 0 0 1 0 1
# 0 0 0 0 0
# 0 1 0 1 0
# 0 0 0 0 0
#
# Output:
# YES

import sys

s = sys.stdin.readlines()
lst_in = [list(map(int, x.strip().split())) for x in s]

units = []
result = "YES"

for row in range(len(lst_in)):
    for col in range(len(lst_in)):
        if lst_in[row][col] == 1:
            units.append([row, col])


for i in units:
    row = i[0]
    col = i[1]
    for rc in range(-1, 2):
        for cc in range(-1, 2):
            new_row = row + rc
            new_col = col + cc

            if 0 <= new_row < 5 and 0 <= new_col < 5:
                if (new_row != row or new_col != col) and lst_in[new_row][new_col] == 1:
                    result = "NO"

print(result)
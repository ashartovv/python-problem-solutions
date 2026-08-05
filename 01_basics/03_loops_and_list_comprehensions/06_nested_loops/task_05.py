# Input: a 5 × 5 matrix of integers.
#
# The input is already read and stored in:
# s = sys.stdin.readlines()
# lst_in = [list(map(int, x.strip().split())) for x in s]
#
# Check whether the matrix is symmetric
# with respect to the main diagonal.
#
# The main diagonal runs from the top-left corner
# to the bottom-right corner of the matrix.
#
# Print:
# "YES" if the matrix is symmetric,
# otherwise print "NO".
#
# Example:
#
# Input:
# 2 3 4 5 6
# 3 2 7 8 9
# 4 7 2 0 4
# 5 8 0 2 1
# 6 9 4 1 2
#
# Output:
# YES

import sys

s = sys.stdin.readlines()
lst_in = [list(map(int, x.strip().split())) for x in s]

result = "YES"

for row in range(5):
    for col in range(5):
        if lst_in[row][col] != lst_in[col][row]:
            result = "NO"

print(result)
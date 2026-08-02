# Problem:
# A two-dimensional list of numbers with size n x m is read in the program:
#
# s = sys.stdin.readlines()
# lst2D = [list(map(int, x.strip().split())) for x in s]
#
# The list lst2D has the following format (example):
#
# lst2D = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
#
# It is necessary to traverse the elements of this list in a snake pattern,
# that is, in the order shown in the picture,
# and output them sequentially in one line separated by spaces.
#
# For example, the output for the given list lst2D should be:
#
# 1 2 3 6 5 4 7 8 9
#
# Test data:
#
# Input:
# -3 0 10 11
# 1 2 8 4
# 5 3 6 7
#
# Output:
# -3 0 10 11 4 8 2 1 5 3 6 7

import sys
s = sys.stdin.readlines()
lst2D = [list(map(int, x.strip().split())) for x in s]
result = []

for i, num in enumerate(lst2D):
    if i % 2 == 1:
        lst2D[i] = lst2D[i][::-1]
        result.extend(lst2D[i])
    else:
        result.extend(num)

print(*result)
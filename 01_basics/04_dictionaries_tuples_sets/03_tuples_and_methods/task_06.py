# Input:
#
# Declare the following two-dimensional tuple with a size of 5 x 5 elements:
#
# t = ((1, 0, 0, 0, 0),
#      (0, 1, 0, 0, 0),
#      (0, 0, 1, 0, 0),
#      (0, 0, 0, 1, 0),
#      (0, 0, 0, 0, 1))
#
# A natural number N (N < 5) is given as input.
#
# Based on the tuple t, create a new analogous tuple t2
# with a size of N x N by discarding the last rows and columns.
#
# Display the result as a table of numbers.
#
# Note:
# When displaying the table, there must be no spaces at the end of the lines.
#
# Test data
#
# Input:
# 3
#
# Output:
# 1 0 0
# 0 1 0
# 0 0 1

t = ((1, 0, 0, 0, 0),
     (0, 1, 0, 0, 0),
     (0, 0, 1, 0, 0),
     (0, 0, 0, 1, 0),
     (0, 0, 0, 0, 1))

N = int(input())

t2 = tuple(
    tuple(col for col in row[:N])
    for row in t[:N]
)

for row in t2:
    print(*row)
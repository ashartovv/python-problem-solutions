# Input:
# Seven integers are given in one line, separated by spaces.
#
# Read them and put the first four numbers into the list lst,
# and the remaining three numbers into separate variables x, y, z.
# Use the packing operator *.
#
# Print lst using:
# print(*lst)
#
# Test data:
#
# Input:
# 56 4 -23 2 0 3 5
#
# Output:
# 56 4 -23 2

*lst, x, y, z = list(map(int, input().split()))

print(*lst)
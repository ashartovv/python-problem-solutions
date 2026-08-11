# Input:
#
# A sequence of integers separated by spaces is given in one line.
#
# Read these integers and store them in a tuple.
#
# Then, find and print, on one line and separated by spaces,
# all indices of non-unique (repeated) values in the tuple.
#
# The indices must be printed in their original order.
#
# Test data
#
# Input:
# 5 4 -3 2 4 5 10 11
#
# Output:
# 0 1 4 5

numbers = tuple(map(int, input().split()))
non_unique = tuple()

for index, value in enumerate(numbers):
    if numbers.count(value) > 1:
        non_unique += (index, )

print(*non_unique)
# Input:
#
# Continue the program where the input data (integers) has already been read
# and stored as a tuple t:
#
# t = tuple(map(int, input().split()))  # tuple of integers
# s = 0  # initial sum of the elements
#
# Using the walrus operator and the variable s, create a new list lst
# with a list comprehension.
#
# Each element of lst must be the sum of the current value and all
# previous values from the tuple t.
#
# For example, for:
#
# t = (1, 2, 3, 4, 5, 6)
#
# the resulting list must be:
#
# lst = [1, 3, 6, 10, 15, 21]
#
# Print the elements of lst on one line, separated by spaces.
#
# Test data:
#
# Input:
# 1 2 3 4 5 6
#
# Output:
# 1 3 6 10 15 21

t = tuple(map(int, input().split()))
s = 0

lst = [
    s := s + value
    for value in t
]

print(*lst)
# Input:
# The program receives a string containing integers separated by spaces.
# Read this string from the input.
#
# Then, using the map function, convert the string into a list
# of integers taken by their absolute values.
#
# Create exactly one list named lst containing these numbers.
#
# Display the list on the screen using:
# print(*lst)
#
# Tests:
#
# Test #1
# Input: -5 6 8 11 -10 0
# Output: 5 6 8 11 10 0
#
# Test #2
# Input: 1 2 3 -1 -2 -3
# Output: 1 2 3 1 2 3

lst = list(map(abs, map(int, input().split())))

print(*lst)
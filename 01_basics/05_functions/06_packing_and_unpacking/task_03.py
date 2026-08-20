# Input:
# Two integers a and b (a < b) are given in one line, separated by a space.
# Read them and create a list lst containing all integers from a to b
# inclusive, with a step of 1.
# Use the range function, [] operator, and unpacking operator *.
# Print the resulting list using print(*lst).
#
# Test data:
#
# Input:
# 3 11
#
# Output:
# 3 4 5 6 7 8 9 10 11

numbers = list(map(int, input().split()))

lst = [value for value in range(numbers[0], numbers[1]+1, 1)]

print(*lst)
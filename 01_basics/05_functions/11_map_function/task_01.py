# Input:
# The program receives a string containing real numbers separated by spaces.
# Read this string from the input.
#
# Then, using the map function, convert the numbers in the string
# to their floating-point representation.
#
# Display the first three numbers.
# Extract the numbers using the next function.
#
# It is guaranteed that at least three real numbers are provided.
#
# Display the result on one line, separated by spaces.
#
# Tests:
#
# Test #1
# Input: 4.35 -10.6 1.0 200.34 0.56
# Output: 4.35 -10.6 1.0
#
# Test #2
# Input: 1.2 3.4 -5.6 7.8
# Output: 1.2 3.4 -5.6

lst = map(str, input().split())

for _ in range(3):
    print(next(lst), end=" ")
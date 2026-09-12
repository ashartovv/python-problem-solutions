# Input:
# The program receives a string containing integers separated by spaces.
# Read this string from the input.
#
# Using map() and list(), convert the input string into a list named digits
# containing integers in the same order as they appear in the input.
#
# The list digits must remain unchanged.
#
# Then, using the list digits, create another list named result
# containing Boolean values True or False:
#
# True - if the current number in digits is divisible by 7;
# False - otherwise.
#
# Display the resulting list using:
# print(*result)
#
# Tests:
#
# Test #1
# Input: 5 3 10 17 21 78 -54 -20
# Output: False False False False True False False False
#
# Test #2
# Input: -7 21 14 77 -35
# Output: True True True True True
#
# Test #3
# Input: 55 20 1 5 81 4
# Output: False False False False False False

digits = list(map(int, input().split()))
result = list(map(lambda s: s % 7 == 0, digits))

print(*result)
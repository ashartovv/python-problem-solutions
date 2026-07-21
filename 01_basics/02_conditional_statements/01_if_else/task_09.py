# Problem:
# A six-digit number is given as input.
#
# Read the number and determine whether it is a lucky number.
#
# A lucky number is a six-digit number where the sum of the first
# three digits is equal to the sum of the last three digits.
#
# If the number is lucky, output:
#
# YES
#
# Otherwise, output:
#
# NO
#
# Example:
#
# Input:
# 811235
#
# Output:
# YES

number = list(map(int, input()))

if sum(number[:3]) == sum(number[-3:]):
    print("YES")
else:
    print("NO")
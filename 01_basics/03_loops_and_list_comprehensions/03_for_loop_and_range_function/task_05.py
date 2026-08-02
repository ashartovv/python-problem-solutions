# Problem:
# A sequence of integers is given as input, written in one line
# separated by spaces.
#
# Read these numbers and store them in a list (as numbers, not strings).
#
# Then, using a for loop, go through the list and calculate
# the sum of all odd values.
#
# Output the resulting sum.
#
# Example:
#
# Input:
# 8 11 -2 4 0 13 19 12 7
#
# Output:
# 50

numbers = list(map(int, input().split()))
s = 0

for x in numbers:
    if x % 2 != 0:
        s += x

print(s)
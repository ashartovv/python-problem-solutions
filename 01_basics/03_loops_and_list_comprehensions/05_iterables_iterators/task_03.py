# Input: a four-digit positive integer.
#
# Read the number and determine how to create an iterator
# for traversing its digits.
#
# Using the iterator, print all digits of the number
# on one line separated by spaces.
#
# Example:
#
# Input:
# 4387
#
# Output:
# 4 3 8 7

numbers = str(input())

it_numbers = iter(numbers)

for index, value in enumerate(numbers):
     print(next(it_numbers), end=" ")
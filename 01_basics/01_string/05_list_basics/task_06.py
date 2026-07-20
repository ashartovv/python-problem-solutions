# Problem:
# A string containing the number of new channel subscribers
# for each day is given as input, with values separated by spaces.
#
# Read these numbers and store them in a list as integers
# in the same order as they appear in the input.
#
# Then display the maximum value, minimum value, and the sum
# of all values in the list, separated by spaces.
#
# Input:
# A sequence of integers separated by spaces.
#
# Output:
# The maximum value, minimum value, and total sum of the list,
# separated by spaces.
#
# Example:
# Input:
# 52 65 64 54 68 59 42 63
#
# Output:
# 68 42 467

daily_subscribers = list(map(int, input().split()))

print( max(daily_subscribers), min(daily_subscribers), sum(daily_subscribers))
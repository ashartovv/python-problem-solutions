# Input:
#
# Real numbers separated by spaces are given in one line.
#
# Read these numbers and store them in the set s.
#
# Display the values of the set s in ascending order,
# on one line separated by spaces, using:
#
# print(*sorted(s))
#
# Note:
# The sorted() function and the * operator will be discussed later.
# For now, just remember that collections can be sorted and printed
# in this way.
#
# Test data
#
# Input:
# -5.1 -3.0 7.6 10.3 -4.6 2.78
#
# Output:
# -5.1 -4.6 -3.0 2.78 7.6 10.3

s = set(map(float, input().split()))

print(*sorted(s))
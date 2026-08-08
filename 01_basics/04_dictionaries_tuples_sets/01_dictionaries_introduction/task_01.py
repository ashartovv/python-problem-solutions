# Input:
# A line is given containing key=value pairs separated by spaces.
# The values are integers.
#
# Task:
# Read the line and create a dictionary `d` from these key=value pairs
# using the `dict()` function.
#
# Display the resulting dictionary using:
#
# print(*sorted(d.items()))
#
# Example:
#
# Input:
# one=1 two=2 three=3
#
# Output:
# ('one', 1) ('three', 3) ('two', 2)

lst = input().split()

pairs = [
    [value for value in pair.split('=')]
    for pair in lst
]

d = dict(pairs)

print(*sorted(d.items()))
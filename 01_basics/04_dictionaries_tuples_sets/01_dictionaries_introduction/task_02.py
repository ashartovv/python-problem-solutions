# Input:
# A set of lines is given in the following format:
#
# key1=value1
# key2=value2
# ...
# keyN=valueN
#
# The keys are integers.
#
# The input is already read and stored as a list:
#
# lst_in = list(map(str.strip, sys.stdin.readlines()))
#
# Task:
# Convert the list `lst_in` into a dictionary `d`.
#
# Do not use the `dict()` function.
#
# Display the resulting dictionary using:
#
# print(*sorted(d.items()))
#
# Example:
#
# Input:
# 5=excellent
# 4=good
# 3=satisfactory
#
# Output:
# (3, 'satisfactory') (4, 'good') (5, 'excellent')

import sys

lst_in = list(map(str.strip, sys.stdin.readlines()))

d = {}

lst = [
    [int(value) if value.isdigit() else value for value in row.split('=')]
    for row in lst_in
]

for l in lst:
    d[l[0]] = l[1]

print(*sorted(d.items()))
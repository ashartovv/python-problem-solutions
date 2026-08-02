# Problem:
# Declare the following one-dimensional list of 10 elements,
# initially filled with zeros:
#
# p = [0] * 10
#
# On each iteration of the loop, ask the user to enter
# an integer — the index of an element in the list.
#
# Write the value 1 to that index if it is not already there.
#
# If there is already a 1 at the entered index,
# do not change the list.
# Use the continue statement to skip the rest of the current
# iteration and request another index.
#
# Continue until exactly five ones have been placed in the list.
# Then terminate the loop.
#
# Output the resulting list as numbers separated by spaces.
#
# Example:
#
# Input:
# 1
# 2
# 2
# 5
# 7
# 5
# 9
#
# Output:
# 0 1 1 0 0 1 0 1 0 1

p = [0] * 10
i = 0

while i < 5:
    n = int(input())
    if p[n] != 1:
        p[n] = 1
        i += 1
    else:
        continue

print(*p)
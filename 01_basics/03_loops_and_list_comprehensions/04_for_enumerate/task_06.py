# Input: real numbers separated by spaces.
# Read the numbers and store them in a list.
#
# Using a `for` loop, find the smallest number in the list.
#
# Do NOT use the built-in functions `min()`, `max()`, or sorting.
#
# Example:
#
# Input:
# 8.6 9.11 -4.567 -10.0 1.45
#
# Output:
# -10.0

N = list(map(float, input().split()))

result = 0

for index, value in enumerate(N):
        if N[index - 1] >= value:
            result = value

print(result)
# Input: real numbers separated by spaces.
# Read the numbers and store them in a list.
#
# Replace every negative value in the list with -1.0.
#
# The program must use the `enumerate()` function.
#
# Print the modified list as numbers separated by spaces.
#
# Example:
#
# Input:
# -5.67 3.5 6.89 -3.0
#
# Output:
# -1.0 3.5 6.89 -1.0

N = list(map(float, input().split()))

for index, value in enumerate(N):
    if value < 0:
        N[index] = -1.0

print(*N)
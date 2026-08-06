# Input: a sequence of integers separated by spaces.
#
# Read the numbers and store them in a list.
#
# Sort the list in ascending (non-decreasing) order
# using the Bubble Sort algorithm.
#
# Algorithm:
# - Compare each pair of adjacent elements.
# - If the left element is greater than the right one,
#   swap them.
# - After each pass, the largest unsorted element
#   moves to its correct position at the end of the list.
# - Repeat the process for N - 1 passes,
#   where N is the length of the list.
#
# Do NOT use built-in sorting functions.
#
# Print the sorted list on one line,
# with elements separated by spaces.
#
# Example:
#
# Input:
# 4 5 2 0 6 3 -56 3 -1
#
# Output:
# -56 -1 0 2 3 3 4 5 6

N = list(map(int, input().split()))

swapped = True
index = 0

while swapped:
    swapped = False

    for loop in range(len(N) - 1 - index):
        if N[loop] <= N[loop + 1]:
            continue
        else:
            N[loop + 1], N[loop] = N[loop], N[loop + 1]
            swapped = True

    index += 1

print(*N)
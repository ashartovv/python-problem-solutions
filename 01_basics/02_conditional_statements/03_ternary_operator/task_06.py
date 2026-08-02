# Problem:
# Declare the following list of note names:
#
# m = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
#
# Three integers in the range from 1 to 7 are given as input
# in one line separated by spaces: note numbers.
#
# Read these numbers and create a string containing the names
# of the corresponding notes, separated by spaces.
#
# Additionally, add the sharp symbol '#' before the notes:
# "C" and "F".
#
# Implement the program using the ternary conditional operator
# (it can be used multiple times).
#
# Example:
#
# Input:
# 1 6 7
#
# Output:
# #C A B

m = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
numbers = list(map(int, input().split()))

a = "#" + m[numbers[0] - 1] if numbers[0] == 1 or numbers[0] == 4 else m[numbers[0] - 1]
b = "#" + m[numbers[1] - 1] if numbers[1] == 1 or numbers[1] == 4 else m[numbers[1] - 1]
c = "#" + m[numbers[2] - 1] if numbers[2] == 1 or numbers[2] == 4 else m[numbers[2] - 1]

print(a, b, c)
# Problem:
# The user must enter an integer on each iteration of the loop (while).
#
# The loop should continue until the user enters the number 0.
#
# Calculate the sum of all numbers entered during the loop
# and output the result (the sum).
#
# Implement the program using a while loop.
#
# Example:
#
# Input:
# 8
# 11
# 2
# -4
# 0
#
# Output:
# 17

s = 0
number = 1

while  number != 0:
    number = int(input())
    s += number

print(s)
# Input:
#
# Read integers from the keyboard using int(input()).
#
# Use the walrus operator and a while loop.
#
# The while loop must continue until the number 0 is entered.
#
# Calculate the sum of all even numbers entered before 0.
#
# The int(input()) command must appear only once in the program.
#
# Print the resulting sum.

s = 0

while (value := int(input())) != 0:
    if value % 2 == 0:
        s += value

print(s)
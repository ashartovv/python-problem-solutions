# Problem:
# Write a program to find all three-digit numbers
# that leave a remainder of 43 when divided by 47
# and are divisible by 3.
#
# Output the found numbers in ascending order,
# separated by spaces.
#
# Implement the program using a while loop.

i = 100
while i < 1000:
    if i % 47 == 43 and i % 3 == 0:
        print(i, end=" ")
        i += 3
    else:
        i += 1
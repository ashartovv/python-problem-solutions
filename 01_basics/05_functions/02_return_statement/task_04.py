# Input:
# Integer numbers are read one by one from the input stream.
# Reading continues until the value 1 is encountered.
#
# Output:
# Declare a function with one parameter that checks whether a number is even.
# The function must return True if the number is even and False otherwise.
#
# After declaring the function, repeatedly read an integer using:
# x = int(input())
#
# If x is even, print it on a separate line.
# Stop reading when x becomes 1.
#
# Test #1
# Input:
# 2 -4 5 7 10 1
#
# Output:
# 2 -4 10

def is_even(x):
    return x % 2 == 0


while (value := int(input())) != 1:
    if is_even(value):
        print(value)
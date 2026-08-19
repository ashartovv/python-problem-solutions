# Input:
# No input is required.
#
# Output:
# Declare a function named get_even that can accept an arbitrary number
# of numbers as arguments.
#
# For example:
# get_even(1, 2, 3, -5, 10, 8)
#
# The function must return a list containing only the even values
# passed to it.
#
# Do not call the function, only define it.
#
# Test data:
#
# Input:
# 45 4 8 11 12 0
#
# Output:
# No output.

def get_even(*args):
    evens = [
        value for value in args
        if value % 2 == 0
    ]
    return evens
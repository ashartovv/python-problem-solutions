# Input:
# Define a function named create_global with the following signature:
#
# def create_global(x): ...
#
# The function must create a global variable named TOTAL
# and assign it the value of x.
# The function should not print anything to the screen.
# It should only create the variable.
#
# Do not call the function. Only define it.

def create_global(x):
    global TOTAL
    TOTAL = x
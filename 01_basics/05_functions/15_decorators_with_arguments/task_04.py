# Input:
# Declare a function named get_list with one parameter.
# Add the following docstring inside the function:
# """Function for creating a list of integer values"""
#
# The function must form and return a list of integers.
# The input is given as a string containing integers separated by spaces.
#
# Define a decorator that sums all values in the list returned
# by the decorated function and returns the resulting sum.
#
# Inside the decorator, use @wraps to preserve the original
# get_list function's local properties:
# __name__ and __doc__.
#
# Import wraps with:
# from functools import wraps
#
# Apply the decorator to get_list.
# Do not call the decorated function.

from functools import wraps

def get_summed(func):
    @wraps(func)
    def wrapper(s):
        return sum(func(s))
    return wrapper


@get_summed
def get_list(s):
    """Function for creating a list of integer values"""
    return list(map(int, s.split()))
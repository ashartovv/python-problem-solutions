# Input:
# Read a line containing integers separated by spaces
# and store it in a variable.
#
# Define a function with one parameter.
# The function must convert the passed string into a list of numbers
# and return their sum.
#
# Define a decorator for this function with one parameter start,
# which represents the initial value of the sum.
#
# Apply the decorator with start=5 to the function.
#
# Call the decorated function with the input string
# and print the resulting sum.
#
# Tests:
#
# Test #1
# Input: 5 6 3 6 -4 6 -1
# Output: 26
#
# Test #2
# Input: 45 3 -100 34 33
# Output: 20
#
# Test #3
# Input: 1 -1
# Output: 5

def deco_start(start=0):
    def sum_deco(func):
        def wrapper(s):
            return func(f'{start} {s}')

        return wrapper

    return sum_deco


@deco_start(start=5)
def get_sum(s):
    lst = list(map(int, s.split()))
    return sum(lst)


str_in = input()
print(get_sum(str_in))
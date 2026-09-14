# Input:
# A string of integers separated by spaces is given.
# Read this string and store it in a variable.
#
# Define a function get_list with one parameter that converts
# the string into a list of integers and returns it.
#
# Define a decorator for get_list that sorts the resulting list
# of numbers in ascending order.
#
# The sorted list must be returned when the decorated get_list
# function is called.
#
# Call the decorated get_list function and display the resulting
# sorted list lst using:
# print(*lst)
#
# Test data:
# Input:
# 8 11 -5 4 3 10
# Output:
# -5 3 4 8 10 11

def sort_deco(func):
    def wrapper(lst):
        return sorted(func(lst))

    return wrapper


@sort_deco
def get_list(s):
    return list(map(int, s.split()))


N = input()
lst = get_list(N)
print(*lst)
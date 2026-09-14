# Input:
# Define an outer function with one parameter tp.
# The parameter tp specifies the type of collection as a string.
#
# Inside the outer function, define a nested function with one parameter.
# The nested function receives a string containing integers separated by spaces.
#
# The nested function must convert the input string into either a list
# or a tuple, depending on the value of tp:
# - if tp == 'list', create a list;
# - otherwise, create a tuple.
#
# The resulting collection must contain integers, not strings.
#
# The outer function must return a reference to the nested function.
#
# Then read two input lines:
# - the first line contains the value for tp;
# - the second line contains a sequence of integers separated by spaces.
#
# Use the implemented closure to convert the input data into the
# corresponding collection.
# Store the result in a variable named lst.
#
# Print the result using:
#
# print(lst)
#
# Tests:
#
# Test #1
# Input:
# list
# -5 6 8 11 0 111 -456 3
#
# Output:
# [-5, 6, 8, 11, 0, 111, -456, 3]

def outer(tp):
    def inner(text):
        if tp == 'list':
            return list(map(int, text.split()))

        return tuple(map(int, text.split()))

    return inner


tp = outer(input())
print(tp(input()))
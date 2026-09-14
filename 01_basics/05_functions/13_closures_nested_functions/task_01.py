# Input:
# Define an outer function named counter_add with the following signature:
#
# def counter_add(): ...
#
# Inside counter_add, define a nested function with one parameter.
# The outer function counter_add must return a reference to the nested function.
# This implements a closure.
#
# The nested function must increase the value passed through its
# only parameter by 5 and return the calculated result.
#
# Then call counter_add() and assign its result to a variable named cnt.
# The variable cnt must reference the nested function.
#
# Read an integer k from the input:
#
# k = int(input())
#
# Call the nested function through cnt using k as the argument
# and print the result.
#
# Tests:
#
# Test #1
# Input: 7
# Output: 12
#
# Test #2
# Input: -3
# Output: 2
#
# Test #3
# Input: 0
# Output: 5

def counter_add():
    def counter_increase(x):
        return x + 5
    return counter_increase


k = int(input())
cnt = counter_add()
print(cnt(k))
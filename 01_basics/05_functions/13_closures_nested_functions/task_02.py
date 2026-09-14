# Input:
# Define an outer function named counter_add with the following signature:
#
# def counter_add(n): ...
#
# Inside counter_add, define a nested function with one parameter.
# The nested function must increase the value of its parameter
# by n, where n is the parameter of the outer function.
#
# The outer function counter_add must return a reference to the nested function.
#
# Call counter_add() with the argument 2 and assign the result
# to a variable named cnt.
# The variable cnt must reference the nested function.
#
# Read an integer k from the input:
#
# k = int(input())
#
# Call the nested function through cnt using k as the argument.
# Print the result.
#
# Tests:
#
# Test #1
# Input: 5
# Output: 7
#
# Test #2
# Input: 0
# Output: 2
#
# Test #3
# Input: -2
# Output: 0
#
# Test #4
# Input: -4
# Output: -2

def counter_add(n):
    def counter_increase(x):
        x += n
        return x
    return counter_increase

k = int(input())
cnt = counter_add(2)
print(cnt(k))
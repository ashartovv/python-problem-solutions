# Input:
# The program reads the global variable WIDTH from the input stream.
# Complete the body of the function func1 with a command
# that allows the function to modify the global variable WIDTH.
#
# Tests:
#
# Test #1
# Input: 12
# Output: 13
#
# Test #2
# Input: -1
# Output: 0
#
# Test #3
# Input: 2
# Output: 3

WIDTH = int(input())


def func1():
    global WIDTH
    WIDTH += 1
    return WIDTH


print(func1())
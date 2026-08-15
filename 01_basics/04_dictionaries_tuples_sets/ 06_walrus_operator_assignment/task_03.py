# Input:
#
# A function f and a tuple t are already defined:
#
# def f(x):
#     return abs(x) ** 0.5 + 3.2 + x
#
# t = tuple(map(float, input().split()))
#
# Using a list comprehension and the walrus operator,
# create a two-dimensional list lst.
#
# For each value x from tuple t, the nested list must contain:
# f(x), f(x) ** 2, f(x) ** 3
#
# The function f(x) must be called exactly once for each value x.
#
# Do not print anything.
#
# Test data:
#
# Input:
# 4.4 -3.1 0.1 5.1
#
# Output:
#

def f(x):
    return abs(x) ** 0.5 + 3.2 + x

t = tuple(map(float, input().split()))

lst = [
    [y := f(x), y ** 2, y ** 3]
    for x in t
]
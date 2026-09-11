# Input:
# The program already contains a function filter_lst that selects elements
# from the iterable object passed to it and returns a tuple of selected values.
#
# Read a list of integers separated by spaces from the input
# and store them in the list digs.
#
# Then, call the function filter_lst several times to create:
#
# 1. A tuple containing all values from the list digs.
# 2. A tuple containing only negative numbers from digs.
# 3. A tuple containing only non-negative numbers from digs,
#    including 0.
# 4. A tuple containing only numbers in the range [3; 5] from digs.
#
# To select the required values, pass the corresponding anonymous
# (lambda) functions to the formal parameter key.
#
# Display each resulting tuple on a separate line using:
# print(*lst)
#
# Here, lst is the tuple returned by filter_lst.
#
# Tests:
#
# Test #1
# Input: 5 4 -3 4 5 -24 -6 9 0
# Output:
# 5 4 -3 4 5 -24 -6 9 0
# -3 -24 -6
# 5 4 4 5 9 0
# 5 4 4 5
#
# Test #2
# Input: 5 4 3 -1 0 -2
# Output:
# 5 4 3 -1 0 -2
# -1 -2
# 5 4 3 0
# 5 4 3
#
# Test #3
# Input: -5 -4 -1 0 -2 5
# Output:
# -5 -4 -1 0 -2 5
# -5 -4 -1 -2
# 0 5
# 5

def filter_lst(it, key=None):
    if key is None:
        return tuple(it)

    res = ()
    for x in it:
        if key(x):
            res += (x,)

    return res


digs = list(map(int, input().split()))

print(*filter_lst(digs))
print(*filter_lst(digs, lambda x: x < 0))
print(*filter_lst(digs, lambda x: x >= 0))
print(*filter_lst(digs, lambda x: 3 <= x <= 5))
# Input:
# Integer numbers are given on one line, separated by spaces.
# Read them and store them in a list named digs.
#
# Output:
# Declare a function with two parameters.
# The parameters will receive the maximum and minimum values
# from the created digs list.
# The function must return the product of the two passed arguments.
#
# Call this function, passing the minimum and maximum numerical values
# from the digs list as arguments.
# Display the value returned by the function.
#
# Hint:
# Use the standard Python functions max and min to pass the arguments
# to the function.
#
# Test #1
# Input:
# 56 34 -30 22 1 4 10
#
# Output:
# -1680
#
# Test #2
# Input:
# 1 2 3 4 5 -3 -2
#
# Output:
# -15
#
# Test #3
# Input:
# 1 2
#
# Output:
# 2
#
# Test data
#
# Input:
# 56 34 -30 22 1 4 10
#
# Output:
# -1680

def get_product(max, min):
    return max * min


digs = list(map(int, input().split()))

print(get_product(max(digs), min(digs)))
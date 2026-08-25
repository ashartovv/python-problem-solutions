# Input:
# A sequence of integers separated by spaces.
#
# Read the integers and store them in a list or tuple.
#
# Define a recursive function named get_rec_sum.
# The first parameter must be the list of numbers.
# Additional parameters may be chosen as needed.
#
# The function must recursively calculate and return
# the sum of all numbers.
#
# The function must not print anything.
#
# Call get_rec_sum and print the returned sum.
#
# Test input:
# 8 11 -5 4 3
#
# Test output:
# 21

def get_rec_sum(*values):
    values = list(values)
    n = 0
    n += values[0]
    del values[0]

    if len(values) != 0:
        n += get_rec_sum(*values)

    return n


N = list(map(int, input().split()))
result = get_rec_sum(*N)

print(result)
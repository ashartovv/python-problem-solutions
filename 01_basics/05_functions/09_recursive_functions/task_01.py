# Input:
# A single positive integer N.
#
# Define a recursive function named get_rec_N.
# The function takes one numeric parameter.
# It must display all integers from 1 to N inclusive,
# with each number printed on a separate line.
#
# The initial function call is already provided:
# get_rec_N(N)
#
# Test data:
#
# Input:
# 8
#
# Output:
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8

def get_rec_N(value):
    if value > 1:
        get_rec_N(value - 1)
    print(value)


N = int(input())
get_rec_N(N)
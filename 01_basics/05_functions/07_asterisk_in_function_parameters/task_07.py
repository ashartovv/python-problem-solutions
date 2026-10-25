# Input:
# Define a function named operator with the following parameters:
# - The first two parameters can accept both positional and keyword arguments.
# - The third parameter, opt, has a default value of 'sum'
#   and must accept keyword arguments only.
# - The fourth parameter, initial, has a default value of 0
#   and must accept keyword arguments only.
#
# The function must behave as follows:
# - If opt is 'sum', return the sum of the first two parameters plus initial.
# - If opt is 'mul', return the product of the first two parameters
#   multiplied by initial.
# - For any other value of opt, return 0.
#
# Read two integers a and b from input using:
# a, b = map(int, input().split())
#
# Call operator with a and b, opt='mul', and initial=2.
# Store the result in a variable named result and print its value.
#
# Test data:
# Input:
# 3 4
#
# Output:
# 24

def operator(a, b, *, opt='sum', initial=0):
    if opt == 'sum':
       return a + b + initial
    elif opt == 'mul':
        return (a*b)*initial
    else:
        return 0


a, b = map(int, input().split())
result = operator(a, b, opt='mul', initial=2)
print(result)

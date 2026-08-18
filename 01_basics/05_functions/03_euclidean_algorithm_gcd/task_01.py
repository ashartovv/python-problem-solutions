# Input:
# Repeat the fast Euclidean algorithm for finding the greatest common divisor
# (GCD) of two natural numbers a and b.
#
# Output:
# Declare a function named get_nod with two parameters a and b
# (natural numbers) that returns the value of GCD(a, b).
#
# Do not call the function, only define it.
#
# Test data:
#
# Input:
# 15 121050
#
# Output:
#

def get_nod(a, b):
    if a > b:
        a, b = b, a

    while b != 0:
        a, b = b, a % b

    return a
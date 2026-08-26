# Input:
# A non-negative integer n.
#
# Define a recursive function named fact_rec(n)
# to calculate the factorial of n.
#
# The function must return the calculated factorial value.
# Do not call the function.
#
# Factorial:
# n! = 1 * 2 * 3 * ... * n
#
# Test data:
#
# Input:
# 6
#
# Output:
# 720

def fact_rec(n, acc=1):
    if n <= 1:
        return acc

    return fact_rec(n - 1, acc * n)


n = int(input())
fact_rec(n)
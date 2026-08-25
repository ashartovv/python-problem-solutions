# Input:
# A natural number N (N >= 2).
#
# Define a recursive function with the signature:
# def fib_rec(N, f):
#     ...
#
# N is the total number of Fibonacci numbers to generate.
# f is the initial list containing the first two Fibonacci numbers.
#
# The first two Fibonacci numbers are 1 and 1.
# Each following number is the sum of the two previous numbers.
#
# The function must return a list containing exactly N Fibonacci numbers.
#
# The function is called as:
# result = fib_rec(N, [1, 1])
#
# Test input:
# 7
#
# Test output:
# No output.

def fib_rec(N, f):
    if len(f) != N:
        f = list(f)
        f.append(f[-2] + f[-1])

    if len(f) != N:
        f = fib_rec(N, f)

    return f


N = int(input())
result = fib_rec(N, [1, 1])  # эту строчку не менять
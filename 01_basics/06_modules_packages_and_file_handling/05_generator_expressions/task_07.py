# Read two integers a and b (a < b) from one line, separated by a space.
# Declare a generator that yields the values of the function
# f(x) = 0.5 * pow(x, 2) - 2.0
# for x in the inclusive range [a, b], with a step of 0.01.
# Print the first 20 function values generated, rounded to two decimal places.

a, b = map(int, input().split())

gen = (0.5 * pow(x/100, 2) - 2.0 for x in range(a * 100, b * 100 + 1))

for _ in range(20):
    print(round(next(gen), 2), end=' ')
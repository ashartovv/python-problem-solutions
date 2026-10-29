# Read two integers a and b (a < b) from one line, separated by a space.
# Create a generator expression that yields the squares of integers
# in the range [a, b], inclusive.
# Convert the generator into a tuple without using loops.
# Assign the resulting tuple to the variable tp.
# Do not print anything to the screen.

a, b = map(int, input().split())

gen = (x**2 for x in range(a, b+1))
tp = tuple(gen)
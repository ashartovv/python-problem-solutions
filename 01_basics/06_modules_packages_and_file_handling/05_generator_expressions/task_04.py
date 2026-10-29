# Read a positive integer a.
# Create a generator that yields the absolute values of integers
# in the range [-a, a], inclusive.
# Create another generator that yields the cubes of the values
# produced by the first generator.
# Print the first four values of the second generator on one line,
# separated by spaces.
# It is guaranteed that at least four values are available.

a = int(input())

gen = (x for x in range(-a, a+1))
cube = (abs(x**3) for x in gen)

for _ in range(4):
    print(next(cube), end=" ")
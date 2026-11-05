# Read two integers a and b (a < b) from one line, separated by a space.
# Define a generator that yields the absolute values of integers
# in the range [a, b], inclusive.
# Print the first five values of the generator, each on a new line.
# It is guaranteed that at least five values are available.

a, b = map(int, input().split())

gen = (x for x in range(a , b + 1))

for _ in range(5):
    print(abs(next(gen)))
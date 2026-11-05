# Define a generator function named counter(start=0, step=1) that yields
# an infinite sequence of numbers starting at start and increasing by step.
# Read two integers, start and step, from one line, separated by a space.
# Call counter with the given arguments and print the first three generated
# values on a single line, separated by spaces.

def counter(start=0, step=1):
    while True:
        yield start
        start += step


start, step = map(int, input().split())
numbers = counter(start, step)

for _ in range(3):
        print(next(numbers), end=' ')
# Import ascii_lowercase from the string module.
# Create a generator that yields all possible combinations of two lowercase
# Latin letters, using ascii_lowercase.
# Print the first 50 combinations on one line, separated by spaces.

from string import ascii_lowercase

gen = (x+y for x in ascii_lowercase for y in ascii_lowercase)

for _ in range(50):
    print(next(gen), end=' ')
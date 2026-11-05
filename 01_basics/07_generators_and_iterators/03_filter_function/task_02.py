# Convert lst_in into a tuple of tuples using map()
# and an anonymous function.
# Each inner tuple must contain the item name and its weight.

# Use filter() with an anonymous function to exclude
# items whose weight is less than 500.

# Extract only the names of the remaining items.

# Print the item names in one line, separated by spaces.

import sys

lst_in = list(map(str.strip, sys.stdin.readlines()))

t = tuple(map(lambda x: tuple(x.split('=')), lst_in))
result = filter(lambda x: int(x[1]) > 500, t)

for value in result:
    print(value[0], end=' ')
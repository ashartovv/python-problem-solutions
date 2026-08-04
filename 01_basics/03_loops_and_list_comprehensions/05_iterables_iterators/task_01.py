# Input: a string containing city names separated by spaces.
#
# Example:
# "Moscow London Berlin Beijing"
#
# Read the string and create a list of city names.
#
# Then create an iterator for the created list and use the iterator
# to print the first two city names, each on a separate line.
#
# Example:
#
# Input:
# Moscow London Berlin Beijing
#
# Output:
# Moscow
# London

cities = input().split()

it = iter(cities)

for i in range(2):
    print(next(it))
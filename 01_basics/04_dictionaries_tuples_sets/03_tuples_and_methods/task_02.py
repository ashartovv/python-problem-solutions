# Input:
#
# A string containing city names separated by spaces is given as input.
#
# Read this string and use it to create a tuple of city names.
#
# The city names in the tuple must be in the same order as in the
# original string.
#
# Check the resulting tuple:
# if the city "Moscow" is not present, add it to the end of the tuple.
#
# Print the city names from the tuple in their original order,
# separated by spaces on one line.
#
# Test data
#
# Input:
# Ufa Kazan Samara
#
# Output:
# Ufa Kazan Samara Moscow

cities = tuple(map(str, input().split()))

if "Moscow" not in cities:
    cities = cities + ("Moscow",)

print(*cities)
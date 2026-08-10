# Input:
#
# A string containing city names separated by spaces is given as input.
#
# Read this string and use it to create a tuple of city names.
#
# Then check the resulting tuple:
# if the city "Ulyanovsk" is present, remove this element
# by creating a new tuple.
#
# Print the city names from the resulting tuple in their original order,
# separated by spaces on one line.
#
# Test data
#
# Input:
# Voronezh Samara Tolyatti Ulyanovsk Perm
#
# Output:
# Voronezh Samara Tolyatti Perm

cities = tuple(map(str, input().split()))

if "Ulyanovsk" in cities:
    lst = list(cities)
    lst.remove("Ulyanovsk")
    cities = tuple(lst)

print(*cities)
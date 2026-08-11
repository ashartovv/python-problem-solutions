# Input:
#
# Two lines containing lists of city names are given.
# Each line contains city names separated by spaces.
#
# Read both lines and store them as separate lists or tuples.
#
# Using sets, compare the two collections by their unique city names.
#
# If both collections contain exactly the same unique cities,
# regardless of their order, display:
#
# YES
#
# Otherwise, display:
#
# NO
#
# Test data
#
# Input:
# Moscow Tver Ufa Kazan Ufa Moscow
# Ufa Tver Moscow Kazan
#
# Output:
# YES

cities_1 = tuple(input().split())
cities_2 = tuple(input().split())

if set(cities_1) == set(cities_2):
    print("YES")
else:
    print("NO")
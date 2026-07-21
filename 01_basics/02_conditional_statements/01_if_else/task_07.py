# Problem:
# A string containing city names separated by spaces is given as input.
#
# Read this string and create a list `cities` containing the city names.
#
# Then check whether the city "Moscow" is present in the list.
# If it is present, remove this element from the list.
#
# Output the resulting list `cities` using:
#
# print(*cities)
#
# Example:
#
# Input:
# Ufa Astrakhan Moscow Samara Kazan
#
# Output:
# Ufa Astrakhan Samara Kazan

cities = list(map(str, input().split()))

if "Moscow" in cities:
    cities.remove("Moscow")
    print(*cities)
else:
    print(*cities)
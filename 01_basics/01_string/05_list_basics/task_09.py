# Problem:
# A string containing city names separated by spaces is given as input.
# Read this string and create a list named `lst` from the city names.
#
# Add the following list `cities` to the end of `lst`:
#
# cities = ["Moscow", "Tver", "Vologda"]
#
# Display the resulting list using:
#
# print(*lst)
#
# Input:
# A string containing city names separated by spaces.
#
# Output:
# The input city names followed by the cities from `cities`,
# separated by spaces.
#
# Example:
# Input:
# Ufa Kazan Sevastopol
#
# Output:
# Ufa Kazan Sevastopol Moscow Tver Vologda

cities = ["Moscow", "Tver", "Vologda"]
lst = list(map(str, input().split())) + cities

print(*lst)

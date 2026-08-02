# Problem:
# A string containing city names separated by spaces is given as input.
# Read this string and create a list named `lst` from the city names.
#
# Add the following list `cities` to the beginning of `lst`:
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
# The city names from `cities` followed by the input cities,
# separated by spaces.
#
# Example:
# Input:
# Ufa Kazan Sevastopol
#
# Output:
# Moscow Tver Vologda Ufa Kazan Sevastopol

cities = ["Moscow", "Tver", "Vologda"]
lst = cities + list(map(str, input().split()))

print(*lst)
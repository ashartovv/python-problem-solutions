# Problem:
# Declare the following list of cities:
#
# cities = ["Moscow", "Kazan", "Yaroslavl"]
#
# Insert the string "Ulyanovsk" into the second position
# (as the second element) of this list.
#
# Display the resulting list using:
#
# print(*cities)
#
# Input:
# No input.
#
# Output:
# The list of cities with "Ulyanovsk" inserted as the second element.
#
# Example:
# Output:
# Moscow Ulyanovsk Kazan Yaroslavl

cities = ["Moscow", "Kazan", "Yaroslavl"]
cities.insert(1, "Ulyanovsk")

print(*cities)

# Problem:
# Declare the following list containing city names:
#
# c = ["Moscow", "Ulyanovsk", "Samara", "Tver",
#      "Vologda", "Omsk", "Ufa"]
#
# Using list slicing, select every other city from the list
# starting from the first city.
#
# Display the resulting slice as a list.
#
# Input:
# No input.
#
# Output:
# The list containing every other city starting from the first one.
#
# Example:
# Output:
# ['Moscow', 'Samara', 'Vologda', 'Ufa']

c = ["Moscow", "Ulyanovsk", "Samara", "Tver", "Vologda", "Omsk", "Ufa"]

print(c[::2])
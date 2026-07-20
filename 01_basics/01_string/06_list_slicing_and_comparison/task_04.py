# Problem:
# Declare the following list containing city names:
#
# c = ["Moscow", "Ulyanovsk", "Samara", "Tver",
#      "Vologda", "Omsk", "Ufa"]
#
# Using list slicing, select every other city from the list
# starting from the second city.
#
# Display the resulting slice as a list.
#
# Input:
# No input.
#
# Output:
# The list containing every other city starting from the second one.
#
# Example:
# Output:
# ['Ulyanovsk', 'Tver', 'Omsk']

c = ["Moscow", "Ulyanovsk", "Samara", "Tver", "Vologda", "Omsk", "Ufa"]

print(c[1::2])
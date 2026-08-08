# Input:
# A string containing city names
# separated by spaces.
#
# Task:
# Read the string.
#
# Using list comprehension,
# create a list containing
# only city names
# whose length is greater than 5 characters.
#
# Print the elements
# of the resulting list
# in one line separated by spaces.
#
# Example:
#
# Input:
# Kazan Ufa Moscow Chelyabinsk Omsk Tours Samara
#
# Output:
# Kazan Moscow Chelyabinsk Samara

cities = input().split()

lst = [city for city in cities if len(city) > 5]

print(*lst)
# Input:
# No input is required.
#
# Output:
# Declare a function named get_biggest_city that can accept an arbitrary
# number of city names (strings) as arguments.
#
# For example:
# get_biggest_city('City 1', 'City 2', 'City 3', 'City 4')
#
# The function must return the name of the city (string) with the greatest
# length. If several cities have the same greatest length, return the first
# one passed to the function.
#
# The program must be implemented without using sorting.
#
# Do not call the function, only define it.
#
# Test data:
#
# Input:
# Peter Moscow Samara Voronezh
#
# Output:
# No output.
def get_biggest_city(*cities):
    biggest_city = ""
    biggest_len = 0

    for city in cities:
        if len(city) > biggest_len:
            biggest_city = city
            biggest_len = len(city)

    return biggest_city
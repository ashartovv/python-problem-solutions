# Input:
# Declare a function that has one parameter accepting a string.
# The function must return two values as a tuple: the passed string and its length.
#
# After declaring the function, read from the input stream a string containing
# city names written on one line and separated by spaces.
# Form a list named cities from the read string containing the city names.
#
# Then, using a dictionary comprehension and the previously declared function,
# create a dictionary named d based on the cities list in the following format:
#
# d = {<city 1>: <number of characters>, ..., <city N>: <number of characters>}
#
# Display this dictionary's keys in ascending order of string lengths using
# the following commands:
#
# a = sorted(d, key=d.get)
# print(*a)
#
# Test #1
# Input:
# Voronezh London Tver Omsk Ufa
#
# Output:
# Ufa Omsk Tver London Voronezh
#
# Test #2
# Input:
# Moscow Ulyanovsk Vologda Ufa
#
# Output:
# Ufa Moscow Vologda Ulyanovsk
#
# Test data
#
# Input:
# Voronezh London Tver Omsk Ufa
#
# Output:
# Ufa Omsk Tver London Voronezh

def get_stats(text):
    return (text, len(text))


cities = input().split()

d = {
    get_stats(city)[0]: get_stats(city)[1]
    for city in cities
}

a = sorted(d, key=d.get)
print(*a)
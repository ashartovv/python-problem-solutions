# Input:
# A string in the format:
#
# <city 1> <population 1> <city 2> <population 2> ... <city N> <population N>
#
# Task:
# Read the string.
#
# Using list comprehension,
# create a list named `lst`
# containing nested lists of pairs:
#
# [
#   [<city 1>, <population 1>],
#   [<city 2>, <population 2>],
#   ...
# ]
#
# The population value is an integer
# representing thousands of people.
#
# Print the resulting list:
#
# print(lst)
#
# Example:
#
# Input:
# Moscow 15000 Ufa 1200 Samara 1090 Kazan 1300
#
# Output:
# [['Moscow', 15000], ['Ufa', 1200], ['Samara', 1090], ['Kazan', 1300]]

cities = input().split()

lst = [[cities[city], int(cities[city + 1])] for city in range(0, len(cities), 2)]

print(*lst)
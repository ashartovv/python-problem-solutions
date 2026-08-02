# Problem:
# A string containing city names separated by spaces is given.
#
# Read the string and create a list of city names from it.
#
# Determine whether every city name in the list
# has a length greater than 5 characters.
#
# If all city names satisfy this condition,
# output:
#
# YES
#
# otherwise output:
#
# NO
#
# Implement the solution using a while loop
# and the break statement.
#
# Example:
#
# Input:
# Samara, Ulyanovsk, Novgorod, Moscow
#
# Output:
# YES

cities = list(input().split())
result = "YES"
i = 0

while i < len(cities[:]):
    if len(cities[i]) <= 5:
        result = "NO"
        break

    i += 1

print(result)

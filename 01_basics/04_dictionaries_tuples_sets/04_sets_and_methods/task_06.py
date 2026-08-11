# Input:
#
# City names are given as input, each on a separate line.
#
# Read these city names in a loop until the string "q" is encountered.
#
# Using a set, determine the total number of unique cities
# that were read by the program, excluding "q".
#
# Display this number.
#
# Note:
# When implementing the program, use only sets from the collections.
#
# Test data
#
# Input:
# Ufa
# Moscow
# Tver
# Yekaterinburg
# Tomsk
# Ufa
# Moscow
# q
#
# Output:
# 5

cities = set()

while True:
    n = str(input())
    if n == 'q':
        break

    cities.add(n)

print(len(cities))
# Input:
# A string containing city names separated by spaces is given in one line.
# Read this string and create a list of city names from it.
# Then, using the unpacking operator *, convert this list into a tuple lst_c.
# Print the result using print(lst_c).
#
# Test data:
#
# Input:
# Moscow Ufa Tver Samara
#
# Output:
# ('Moscow', 'Ufa', 'Tver', 'Samara')

cities = input().split()
lst_c = (*cities,)

print(lst_c)
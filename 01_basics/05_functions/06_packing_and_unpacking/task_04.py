# Input:
# The first line contains floating-point numbers separated by spaces.
# The second line contains city names separated by spaces.
#
# Read the numbers and save them as a list.
# Then read the line with city names and create another list from it.
# Create a single list lst containing the numbers first,
# followed by the city names.
# Combine the lists using the unpacking operator *.
# Print the resulting list using print(*lst).
#
# Test data:
#
# Input:
# 5.8 11.0 4.3
# Ufa Omsk Tver Samara
#
# Output:
# 5.8 11.0 4.3 Ufa Omsk Tver Samara

numbers = list(map(float, input().split()))
cities = input().split()

lst = [*numbers, *cities]

print(*lst)
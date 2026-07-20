# Problem:
# A string containing city names separated by spaces is given as input.
# Read the input and create a list using the following statement:
#
# cities = input().split()
#
# Display the value of the last element in the `cities` list.
#
# Input:
# A string containing city names separated by spaces.
#
# Output:
# The last city in the list.
#
# Example:
# Input:
# London Paris Berlin Rome
#
# Output:
# Rome

cities = list(map(str, input().split()))

print(cities[-1])
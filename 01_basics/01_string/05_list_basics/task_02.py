# Problem:
# A string containing city names separated by spaces is given as input.
# Read the input and create a list using the following statement:
#
# cities = input().split()
#
# Then check whether the city "Moscow" is present in the list.
# Display True if it is present, otherwise display False.
#
# Note:
# Solve the task without using conditional statements.
#
# Input:
# A string containing city names separated by spaces.
#
# Output:
# True if "Moscow" is present in the list; otherwise False.
#
# Example:
# Input:
# Tver Ufa Moscow Kazan
#
# Output:
# True

cities = list(map(str, input().split()))

print("Moscow" in cities)
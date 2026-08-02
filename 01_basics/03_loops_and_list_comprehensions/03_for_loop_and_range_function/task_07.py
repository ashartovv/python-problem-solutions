# Problem:
# A string containing city names separated by spaces is given as input.
#
# Read this string and create a list of city names.
#
# Then, using a for loop, go through the list and replace the city names
# with the lengths of their strings.
#
# Output the result as a sequence of numbers separated by spaces on one line.
#
# Example:
#
# Input:
# Moscow Ufa Karaganda Tver Minsk Kazan
#
# Output:
# 6 3 9 5 5 6

cities = input().split()
arr = []

for x in cities:
    arr.append(len(x))

print(*arr)
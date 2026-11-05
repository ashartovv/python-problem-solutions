# Read the input string and split it into a list of city names.

# Use filter() with an anonymous function to select cities
# whose names contain more than 5 characters.

# Extract the first three cities using next().

# Print the three cities in one line, separated by spaces.

cities = input().split()

valid_cities = filter(lambda x: len(x) > 5, cities)

for _ in range(3):
    print(next(valid_cities), end=" ")
# Problem:
# A string consisting of city names separated by spaces is given as input.
# Read the string and transform it so that the city names
# are separated by semicolons without spaces.
# Display the resulting string.
#
# Input:
# A single string containing city names separated by spaces.
#
# Output:
# A string with city names separated by semicolons.
#
# Example:
# Input:
# Moscow London Paris
#
# Output:
# Moscow;London;Paris

text = str(input())

print(text.replace(" ", ";"))
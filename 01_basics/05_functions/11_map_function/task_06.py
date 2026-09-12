# Input:
# The program receives a string containing city names separated by spaces.
# Read this string from the input.
#
# Use the map() function so that city names with more than 5 characters
# remain unchanged.
#
# Replace all other city names with the string "-".
#
# Create a list from the resulting values.
# Display the list on one line, with values separated by spaces.
#
# Test #1
# Input:
# Moscow Ufa Vologda Tula Vladivostok Khabarovsk
# Output:
# Moscow - Vologda - Vladivostok Khabarovsk
#
# Test #2
# Input:
# Ufa Omsk Tula LeninoKamensk
# Output:
# - - - LeninoKamensk

lst = map(lambda x: '-' if len(x) <= 5 else x, input().split())

print(*lst)
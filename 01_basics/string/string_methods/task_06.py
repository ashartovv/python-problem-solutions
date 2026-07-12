# Problem:
# A string consisting of words separated by spaces is given as input.
# Read the string and determine the number of words it contains.
# Display the result.
#
# Input:
# A single string containing words separated by spaces.
#
# Output:
# The number of words in the given string.
#
# Example:
# Input:
# I love Python
#
# Output:
# 3

text = str(input())

print(text.count(" ") + 1)
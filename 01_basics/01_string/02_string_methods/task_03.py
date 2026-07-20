# Problem:
# A string is given as input.
# Read the string and use the String.find() method to find
# the index of the first occurrence of the substring "ra".
# Display the resulting index.
#
# Input:
# A single string.
#
# Output:
# The index of the first occurrence of the substring "ra".
#
# Example:
# Input:
# abrakadabra
#
# Output:
# 2

text = str(input())

print(text.find("ra"))
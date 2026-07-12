# Problem:
# A string is given as input.
# Read the string and display its first five characters in reverse order.
# It is guaranteed that the string length is at least five characters.
#
# Input:
# A single string.
#
# Output:
# The first five characters of the string written in reverse order.
#
# Example:
# Input:
# abrakadabra
#
# Output:
# karba

text = input()

print(text[4::-1])
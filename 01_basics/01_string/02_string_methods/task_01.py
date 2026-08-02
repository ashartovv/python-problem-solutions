# Problem:
# A word is given as input.
# Read the word and convert its second character to uppercase,
# while converting all other characters to lowercase.
# Display the resulting word.
#
# Input:
# A single word.
#
# Output:
# The word with its second character in uppercase
# and all remaining characters in lowercase.
#
# Example:
# Input:
# HELLO
#
# Output:
# hEllo

text = str(input())

print(text.lower()[0] + text[1:].capitalize())
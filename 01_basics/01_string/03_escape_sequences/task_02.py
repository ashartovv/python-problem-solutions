# Problem:
# A string consisting of two words separated by a space is given as input.
# Read the string and replace the space between the words
# with a backslash character ('\').
# Display the resulting string.
#
# Note:
# Solve the task without using f-strings.
#
# Input:
# A single string containing two words separated by a space.
#
# Output:
# The resulting string with a backslash instead of the space.
#
# Example:
# Input:
# Hello Balakirev!
#
# Output:
# Hello\Balakirev!

text_1, text_2 = map(str, input().split())

print(text_1, text_2, sep="\\")
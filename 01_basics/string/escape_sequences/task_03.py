# Problem:
# A string consisting of one or more words separated by single spaces is given as input.
# Read the string and replace the first space (if present)
# with a single quotation mark ('), and all remaining spaces
# with double quotation marks (").
# Display the resulting string.
#
# Input:
# A single string containing one or more words separated by spaces.
#
# Output:
# The transformed string with the first space replaced by a single quotation mark
# and all remaining spaces replaced by double quotation marks.
#
# Example:
# Input:
# My best friend is Python!
#
# Output:
# My'best"friend"is"Python!

text = str(input())

print(text.replace(" ", "\"").replace("\"", "\'", 1))
# Problem:
# A string is given as input.
# Read the string and display all characters with odd indexes
# in one line.
#
# Input:
# A single string.
#
# Output:
# Characters from the string that have odd indexes, written consecutively.
#
# Example:
# Input:
# Balakirev
#
# Output:
# aaie

text = input()

print(text[1::2])
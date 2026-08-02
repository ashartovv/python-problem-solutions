# Problem:
# Two strings are given as input, each on a separate line.
# From the first string, select all characters with even indexes.
# From the second string, select all characters with odd indexes.
# Combine the resulting strings separated by a space and display the result.
#
# Input:
# Two strings, each entered on a new line.
#
# Output:
# A string containing the selected characters from both strings separated by a space.
#
# Example:
# Input:
# Hello
# Python
#
# Output:
# Hlo yhn

s1 = input()
s2 = input()

print(s1[::2], s2[1::2])
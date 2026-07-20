# Problem:
# A slug is given as input.
# Read the string and replace all triple hyphens ("---")
# and double hyphens ("--") with single hyphens ("-").
# Consider the correct order in which the replacements should be performed.
# Display the resulting string.
#
# Input:
# A single slug string.
#
# Output:
# The transformed slug with only single hyphens.
#
# Example:
# Input:
# I---love--python-3---<3
#
# Output:
# I-love-python-3-<3

text = str(input())

print(text.replace("---", "-").replace("--", "-"))
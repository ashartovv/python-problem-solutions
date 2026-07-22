# Problem:
# A string (slug) is given as input.
#
# Read this string and replace all consecutive hyphens
# (--, ---, ----, etc.) with a single hyphen (-).
#
# Output the transformed string.
#
# Implement the program using a while loop.
#
# Example:
#
# Input:
# osnovnye--metody-----slovarey
#
# Output:
# osnovnye-metody-slovarey

word = str(input())

while "--" in word:
    word = word.replace("--", "-")

print(word)
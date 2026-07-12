# Problem:
# A string consisting of two words separated by a space is given as input.
# Read the words from the string.
# The length of the first word is smaller than the length of the second word.
# Cut the second word to the length of the first word and display the result.
#
# Input:
# Two words separated by a space.
#
# Output:
# The second word shortened to the length of the first word.
#
# Example:
# Input:
# Hello Balakirev
#
# Output:
# Balak

word1, word2 = input().split()
word1_lenght = len(word1)

print(word2[:word1_lenght])
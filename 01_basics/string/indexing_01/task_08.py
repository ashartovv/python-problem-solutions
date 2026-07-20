# Problem:
# Two words separated by a space are given as input.
# The words can be read using:
# word1, word2 = input().split()
#
# The length of the second word is smaller than the length of the first word.
# Cut the first word to the length of the second word.
# Then, select characters with odd indexes from both words
# and compare the resulting strings for equality.
# Display the result (True or False).
# The task must be solved without using conditional statements.
#
# Input:
# Two words separated by a space.
#
# Output:
# True if the resulting strings are equal, otherwise False.
#
# Example:
# Input:
# Hello Hell
#
# Output:
# True

word1, word2 = input().split()

print(word1[1:len(word2):2] == word2[1::2])
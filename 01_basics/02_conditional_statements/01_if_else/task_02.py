# Problem:
# A single word is given as input.
#
# Read the word and determine whether it is a palindrome
# (a word that reads the same forwards and backwards,
# for example, ANNA).
#
# Ignore letter case, so the following should all be
# considered palindromes:
#
# Anna
# anna
# aNNA
#
# If the input word is a palindrome, output:
#
# YES
#
# Otherwise, output:
#
# NO

word = input().lower()

if word == word[::-1]:
    print("YES")
else:
    print("NO")
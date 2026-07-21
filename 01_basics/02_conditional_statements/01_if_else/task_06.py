# Problem:
# A word (string) is given as input.
#
# Read the word and check whether it contains all three letters:
#
# t, h, and o
#
# The letters can appear in any order and each letter must appear
# at least once.
#
# Implement the program using only one conditional statement.
#
# If the check is successful, output:
#
# YES
#
# Otherwise, output:
#
# NO
#
# Example:
#
# Input:
# Python
#
# Output:
# YES

word = str(input())

if "t" in word and "h" in word and "o" in word:
    print("YES")
else:
    print("NO")
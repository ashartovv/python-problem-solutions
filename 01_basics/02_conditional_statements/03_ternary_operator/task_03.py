# Problem:
# A word (string) is given as input.
#
# Read the word and assign the following string to the variable msg:
#
# "palindrome" if the entered word is a palindrome
# (reads the same forward and backward);
#
# "not a palindrome" otherwise.
#
# The palindrome check must be performed without considering letter case.
#
# Implement the program using the ternary conditional operator.
#
# Output the value of the variable msg.
#
# Example:
#
# Input:
# Kazak
#
# Output:
# palindrome

word = input().lower()

msg = "palindorme" if word[::-1] == word else "not a palindorme"

print(msg)
# Input:
# Declare an anonymous (lambda) function that checks whether
# the substring "ra" is present in the given string.
#
# The function must return True if the substring is present
# and False otherwise.
#
# Read the string s from the input stream using:
# s = input()
#
# Call the lambda function for the string s.
# Display the result of the function on the screen.
#
# Tests:
#
# Test #1
# Input: abrakadabra
# Output: True
#
# Test #2
# Input: python
# Output: False
#
# Test #3
# Input: moskvara
# Output: True
#
# Test #4
# Input: mama
# Output: False

have_ra = lambda s: "ra" in s
s = input()

print(have_ra(s))
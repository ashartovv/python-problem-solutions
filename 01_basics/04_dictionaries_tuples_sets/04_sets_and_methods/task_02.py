# Input:
#
# A string containing words separated by spaces is given as input.
#
# Read the string, split it into words, and use a set to count
# the number of unique words, ignoring letter case.
#
# Display the number of unique words.
#
# Test data
#
# Input:
# Mom washed the frame and then washed the cat and also washed the floor
#
# Output:
# 9

s = set(input().lower().split())

print(len(s))
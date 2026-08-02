# Problem:
# A string is given as input.
#
# Read the string and find all indices of the substring "ra".
#
# Print all found indices on one line separated by spaces.
#
# If the substring "ra" does not occur in the string, print:
#
# -1
#
# Example:
#
# Input:
# Drummer played the drum in the parade
#
# Output:
# 2 23

word = input()

for i, w in enumerate(word):
    if "ra" not in word:
        print(-1)
        break
    elif "ra" in word[i:i+2]:
         print(i, end=" ")
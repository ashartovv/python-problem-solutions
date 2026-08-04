# Input: a string.
#
# Read the string and create an iterator for traversing its characters.
#
# Using the created iterator, iterate through all characters until the first space.
# During the iteration, print the characters on the screen in one line without spaces.
#
# It is guaranteed that the input string contains at least one space.
#
# Example:
#
# Input:
# It-might be useful
#
# Output:
# It-might

sentence = input().split()

it = iter(sentence[0])

for index, char in enumerate(sentence[0]):
    print(next(it), end="")
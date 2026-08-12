# Input:
#
# Read the input string and split it into separate words.
#
# Create a set comprehension containing unique words.
#
# Convert each word to lowercase.
#
# Include only words with a length of at least 3 characters.
#
# Print the size of the resulting set.
#
# Test data:
#
# Input:
# hut izba car and again hut car
#
# Output:
# 4

words = input().split()

unique_words = {
    word.lower() for word in words
    if len(word) >= 3
}

print(len(unique_words))
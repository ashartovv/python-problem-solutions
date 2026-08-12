# Input:
#
# A string containing words separated by spaces is given.
#
# Read the string and use set and dictionary comprehensions to create a dictionary in the following format:
#
# {word_1: count_1, word_2: count_2, ..., word_N: count_N}
#
# The keys must be unique words, without considering letter case.
#
# The values must be the number of times each word appears in the text.
#
# Print the value associated with the word "and".
#
# If the key "and" does not exist, print 0.
#
# Test data:
#
# Input:
# I what to say and what to say and nothing and period
#
# Output:
# 4

lst_in = input().lower().split()

unique_words = {
    word for word in lst_in
}

d_word = {
    word: lst_in.count(word)
    for word in unique_words
}

if 'and' in unique_words:
    print(d_word['and'])
else:
    print(0)
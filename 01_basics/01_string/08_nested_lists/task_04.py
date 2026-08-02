# Problem:
# The following nested list is already declared in the program:
#
# t = [
#     ["Tell", "me,", "uncle,", "was", "it", "not", "in", "vain"],
#     ["I", "learned", "Python", "with", "the", "channel"],
#     ["Balakirev", "that", "was", "teaching?"]
# ]
#
# A single word is given as input.
#
# Read this word and check whether it exists anywhere
# in the nested list `t`.
#
# Display the result (`True` or `False`).
#
# The solution must be implemented without using conditional statements.
#
# Input:
# A single word.
#
# Output:
# `True` if the word is found in the nested list,
# otherwise `False`.
#
# Example:
# Input:
# uncle,
#
# Output:
# True

t = [["Tell", "me,", "uncle,", "was", "it", "not", "in", "vain"],
     ["I", "learned", "Python", "with", "the", "channel"],
     ["Balakirev", "that", "was", "teaching?"]]

word = str(input())

print(word in sum(t, []))
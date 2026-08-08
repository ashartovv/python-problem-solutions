# A list of strings `t` is given:
#
# t = [
# "– Tell me, uncle, was it not for free",
# "I learned Python with the channel",
# "Balakirev, what did he give?",
# "After all, there were difficult tasks,",
# "Yes, they say, there were some!",
# "Russia remembers not without reason",
# "How we defeated them back then!"
# ]
#
# Task:
# Convert this list into a two-dimensional (nested) list `lst`,
# where each string is represented as a list of words.
#
# Words are separated by spaces.
# Keep only words whose length is greater than 3 characters.
#
# Punctuation marks and other non-space symbols
# must remain attached to the words.
#
# The solution must be implemented using list comprehension.
#
# Display the resulting list using:
#
# print(lst)
#
# Example:
#
# Output:
#
# [
# ['Tell', 'uncle,', 'was', 'free'],
# ...
# ]

t = [
"– Tell me, uncle, was it not for free",
"I learned Python with the channel",
"Balakirev, what did he give?",
"After all, there were difficult tasks,",
"Yes, they say, there were some!",
"Russia remembers not without reason",
"How we defeated them back then!"
]

lst = [
    [word for word in row.split() if len(word) > 3]
    for row in t
]

print(lst)
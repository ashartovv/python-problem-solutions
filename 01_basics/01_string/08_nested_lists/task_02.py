# Problem:
# Three lines of a poem are given as input, one per line.
#
# Read them using:
#
# s1 = input()  # first line
# s2 = input()  # second line
# s3 = input()  # third line
#
# Convert each line into a separate list of words
# (words are separated by spaces).
#
# Put all three lists into a list named `lst`
# to create a two-dimensional (nested) list.
#
# Display the resulting list using:
#
# print(lst)
#
# Input:
# Three lines of text.
#
# Output:
# A nested list, where each inner list contains
# the words from one input line.
#
# Example:
# Input:
# Frost and sun, a wondrous day
# Yet you still are half asleep
# Wake up, beauty, it's time
#
# Output:
# [['Frost', 'and', 'sun,', 'a', 'wondrous', 'day'],
#  ['Yet', 'you', 'still', 'are', 'half', 'asleep'],
#  ['Wake', 'up,', 'beauty,', "it's", 'time']]

s1 = input().split()
s2 = input().split()
s3 = input().split()
lst = [s1, s2, s3]

print(lst)
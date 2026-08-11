# Input:
#
# Comments on one of Sergey’s YouTube videos are given as input.
# Some visitors may leave multiple comments.
#
# The task is to determine the number of unique commenters.
# Assume that different commenters always have different names.
#
# Comments are given in the following format:
#
# name_1: comment_1
# name_2: comment_2
# ...
# name_N: comment_N
#
# The program already reads these lines and stores them in the list:
#
# lst_in = list(map(str.strip, sys.stdin.readlines()))
#
# Display the total number of unique commenters.
#
# Test data
#
# Input:
# EvgeniyK: thank you so much!
# LinaTroshka: like and subscribe!
# Sergey Karandeev: cool video!
# Evgeniy Sosnin: I love it
# EvgeniyK: is this a repeat?
# Sergey Karandeev: no, this is a new video
#
# Output:
# 4

import sys

lst_in = list(map(str.strip, sys.stdin.readlines()))

users = set(
    value.split()[0]
    for value in lst_in
)

print(len(users))
# Input:
#
# Strings containing menu items are given as input, each on a new line,
# in the following format:
#
# name_1 URL_1
# name_2 URL_2
# ...
# name_N URL_N
#
# The program already reads these strings and stores them in the list:
#
# lst_in = list(map(str.strip, sys.stdin.readlines()))
#
# Convert the list lst_in into a tuple menu with the following structure:
#
# ((name_1, URL_1), (name_2, URL_2), ..., (name_N, URL_N))
#
# Display the resulting tuple using:
#
# print(menu)
#
# Test data
#
# Input:
# Main home
# Python learn-python
# Java learn-java
# PHP learn-php
#
# Output:
# (('Main', 'home'), ('Python', 'learn-python'), ('Java', 'learn-java'), ('PHP', 'learn-php'))

import sys

lst_in = list(map(str.strip, sys.stdin.readlines()))

menu = tuple(
    tuple(value for value in row.split())
    for row in lst_in
)

print(menu)
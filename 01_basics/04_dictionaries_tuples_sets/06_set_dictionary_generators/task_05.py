# Input:
#
# Strings containing information about books in a bookstore are given in the format:
#
# <author 1>: <title 1>
# ...
# <author N>: <title N>
#
# Authors and book titles may be repeated.
#
# The input strings have already been read and stored in the list lst_in.
#
# Using comprehensions, create a dictionary named d in the following format:
#
# {
#     'author 1': {'title 1', 'title 2', ..., 'title M'},
#     ...
#     'author K': {'title 1', 'title 2', ..., 'title S'}
# }
#
# The keys must be unique authors.
#
# The values must be sets containing unique book titles written by the corresponding author.
#
# Nothing needs to be printed.
#
# The dictionary must be stored in the variable d.
#
# Test data:
#
# Input:
# Pushkin: The Tale of the Fisherman and the Fish
# Yesenin: Letter to a Woman
# Turgenev: Mumu
# Pushkin: Eugene Onegin
# Yesenin: Rus

import sys

lst_in = list(map(str.strip, sys.stdin.readlines()))

d ={
    author.split(': ')[0]: set()
    for author in lst_in
}

for value in lst_in:
    d[value.split(': ')[0]].add(value.split(': ')[1])
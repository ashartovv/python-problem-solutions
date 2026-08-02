# Problem:
# The program receives strings (book titles) as input.
#
# The program has already implemented reading these strings
# and storing them in a list (each element is a book title).
#
# After that, remove from the list all titles consisting
# of two or more words (words are separated by spaces).
#
# Output the result as a string containing the remaining
# book titles separated by spaces.
#
# Example:
#
# Input:
# Mumu
# Eugene Onegin
# Shining
# The Master and Margarita
# The Queen of Spades
# Kolobok
#
# Output:
# Mumu Shining Kolobok

import sys

# Reading a list from input
lst_in = list(map(str.strip, sys.stdin.readlines()))
i = 0

while i < len(lst_in):
    if " " in lst_in[i]:
        del lst_in[i]
    else:
        print(lst_in[i], end=' ')
        i += 1
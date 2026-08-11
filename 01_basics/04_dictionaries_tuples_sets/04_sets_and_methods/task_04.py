# Input:
#
# A list of guests at a nightclub is given.
# Each guest's name is written on a separate line.
#
# Guests may leave the nightclub and enter again.
# In this case, their names are recorded multiple times.
#
# The program already reads these lines and stores them in the list:
#
# lst_in = list(map(str.strip, sys.stdin.readlines()))
#
# Count the total number of unique guests who visited the nightclub.
# Assume that every guest has a unique name.
#
# Display the total number of guests.
#
# Test data
#
# Input:
# Maria
# Elena
# Ekaterina
# Alexander
# Elena
# Maria
#
# Output:
# 4

import sys

lst_in = list(map(str.strip, sys.stdin.readlines()))
guest_count = len(set(lst_in))

print(guest_count)
# Input:
#
# A list of car license plates is already stored in lst_in.
#
# Create a set of unique car license plates using a set comprehension.
#
# Print the number of unique cars.
#
# Test data:
#
# Input:
# A323GD
# D456VV
# B001BB
# D456VV
# S111SS
#
# Output:
# 4

import sys

lst_in = list(map(str.strip, sys.stdin.readlines()))

unique_cars = {
    value for value in lst_in
}

print(len(unique_cars))
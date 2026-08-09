# Input:
#
# The input consists of lines in the following format:
#
# <birthday 1> name_1
# <birthday 2> name_2
# ...
# <birthday N> name_N
#
# Birthdays and names may repeat.
#
# The input has already been read and stored in the list:
#
# lst_in = list(map(str.strip, sys.stdin.readlines()))
#
# Using lst_in, create a dictionary where:
# - keys are birthdays (integers);
# - values are names (strings).
#
# If several people have the same birthday, store all their names
# in the same value, preserving their original order.
#
# Print the resulting dictionary in the following format:
#
# birthday 1: name1, ..., nameN1
# birthday 2: name1, ..., nameN2
# ...
# birthday M: name1, ..., nameNM
#
# Test data
#
# Input:
# 3 Sergey
# 5 Nikolai
# 4 Elena
# 7 Vladimir
# 5 Yulia
# 4 Svetlana
#
# Output:
# 3: Sergey
# 5: Nikolai, Yulia
# 4: Elena, Svetlana
# 7: Vladimir


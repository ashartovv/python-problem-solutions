# Input:
# No input is required.
#
# Output:
# Define the following functions:
#
# str_min — compares two strings and returns the lexicographically smaller one.
#
# str_min3 — returns the lexicographically smallest string of three strings.
# It must use str_min().
#
# str_min4 — returns the lexicographically smallest string of four strings.
# It must use str_min() / str_min3().
#
# Do not call the functions, only define them.
# Input:
# No input.
#
# Output:
# No output.

def str_min(str_1, str_2):
    if str_1 < str_2:
        return str_1
    else:
        return str_2


def str_min3(str_1, str_2, str_3):
    min_1 = str_min(str_1, str_2)
    if min_1 < str_3:
        return min_1
    else:
        return str_3


def str_min4(str_1, str_2, str_3, str_4):
    min_1 = str_min(str_1, str_2)
    min_2 = str_min(str_3, str_4)

    if min_1 < min_2:
        return min_1
    else:
        return min_2
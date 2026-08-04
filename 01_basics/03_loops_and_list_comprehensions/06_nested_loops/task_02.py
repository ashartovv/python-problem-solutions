# Input: URL strings, one per line.
#
# The input is already read and stored in the list:
# lst_in = list(map(str.strip, sys.stdin.readlines()))
#
# Replace all spaces in each string with hyphens (-).
# Multiple consecutive spaces should be replaced with a single hyphen.
#
# Print the resulting URL strings, one per line,
# preserving their original order.
#
# Example:
#
# Input:
# django chto  eto takoe    poryadok ustanovki
# model mtv   marshrutizaciya funkcii  predstavleniya
# marshrutizaciya  obrabotka isklyucheniy       zaprosov perenapravleniya
#
# Output:
# django-chto-eto-takoe-poryadok-ustanovki
# model-mtv-marshrutizaciya-funkcii-predstavleniya
# marshrutizaciya-obrabotka-isklyucheniy-zaprosov-perenapravleniya

import sys

lst_in = list(map(str.strip, sys.stdin.readlines()))

for index in range(len(lst_in)):
    for _ in range(lst_in[index].count("  ")):
        lst_in[index] = lst_in[index].replace('  ', ' ')

    lst_in[index] = lst_in[index].replace(' ', '-')

    print(lst_in[index])
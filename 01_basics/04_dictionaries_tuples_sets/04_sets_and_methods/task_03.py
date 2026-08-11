# Input:
#
# A string containing Latin characters, spaces, and digits is given as input.
#
# Read this string and extract all non-repeating digits
# (characters from 0 to 9).
#
# Display all found unique digits on one line, separated by spaces,
# in ascending order.
#
# If there are no digits, display:
#
# NO
#
# Test data
#
# Input:
# Python 3.9.11 - best language!
#
# Output:
# 1 3 9

lst_in = set(input())

count = 0

for ch in sorted(lst_in):
    if ch.isdigit():
        print(ch, end=' ')
        count += 1

if count == 0:
    print("NO")
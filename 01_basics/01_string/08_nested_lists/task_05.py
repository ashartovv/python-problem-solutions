# Problem:
# Declare a two-dimensional (nested) list named `table`.
# Each row of the table must be represented as a separate nested list.
#
# The format should be:
#
# table = [[value1, value2, ...], [value1, value2, ...], ...]
#
# Perform the following operations with `table`:
#
# 1. Add a new row (nested list) to the end of `table`
#    with the values:
#
#    4, -2, 10, 6, 2, 7, 13
#
# 2. Swap the first row and the newly added last row.
#
# Do not display anything on the screen.

table = [[6, -2, 0, -5.4, "abc"], [True, "pt", 3, False, False, True], [1, 1, 1, 0]]
table.append([4, -2, 10, 6, 2, 7, 13])
table[0], table[-1] = table[-1], table[0]
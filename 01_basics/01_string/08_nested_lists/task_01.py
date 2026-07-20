# Problem:
# The following list is already declared in the program:
#
# lst = [5.4, 6.7, 10.4]
#
# A sequence of integers separated by spaces is given as input.
#
# Read these integers and store them in a separate list named `digs`.
#
# Append the entire `digs` list to the end of `lst`
# as a single nested element.
#
# Display the resulting list using:
#
# print(lst)
#
# Input:
# A sequence of integers separated by spaces.
#
# Output:
# The list `lst` with `digs` appended as a nested list.
#
# Example:
# Input:
# 8 11
#
# Output:
# [5.4, 6.7, 10.4, [8, 11]]

lst = [5.4, 6.7, 10.4]

digs = list(map(int, input().split()))
lst.append(digs)

print(lst)

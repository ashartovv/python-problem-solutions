# Problem:
# A string containing river names separated by spaces is given as input.
#
# Read the string and create a list named `lst` containing the river names.
#
# Then:
# - sort the list in ascending alphabetical order;
# - remove the first element from the sorted list.
#
# Display the resulting list in one line separated by spaces using:
#
# print(*lst)
#
# Input:
# A sequence of river names separated by spaces.
#
# Output:
# The sorted list of river names without the first element.
#
# Example:
# Input:
# Lena Ob Volga Don Yenisei
#
# Output:
# Don Yenisei Lena Ob

lst = input().split()
lst.sort()
lst.pop(0)

print(*lst)
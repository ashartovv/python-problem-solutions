# Problem:
# A string containing student names separated by spaces is given.
#
# Read the string and create a list of student names.
#
# Determine whether there is at least one name in the list
# that starts and ends with the same letter
# (case-insensitive).
#
# If such a name exists, output:
#
# YES
#
# Otherwise output:
#
# NO
#
# Implement the program using a while loop
# and the break statement.
#
# Example:
#
# Input:
# Peter Anna Ivan Sergey Michael Fedor
#
# Output:
# YES

names = input().lower().split()
i = 0
result = "NO"

while i < len(names):
    if names[i][0] == names[i][-1]:
        result = "YES"
        break

    i += 1

print(result)
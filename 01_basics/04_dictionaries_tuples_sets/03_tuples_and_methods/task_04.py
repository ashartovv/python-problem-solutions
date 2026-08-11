# Input:
#
# A string containing student names separated by spaces is given as input.
#
# Read this string and use it to create a tuple of names.
#
# Then display all names from this tuple, in their original order,
# that contain the substring "va", ignoring letter case.
#
# The names must be printed in lowercase.
#
# Print the selected names on one line, separated by spaces.
#
# Test data
#
# Input:
# Petya Varvara Venera Vasilisa Vasiliy Fedor
#
# Output:
# varvara vasilisa vasiliy

student_names = tuple(map(str, input().lower().split()))

for name in student_names:
    if 'va' in name:
        print(name, end=' ')
# Problem:
# A string containing a person's first name, patronymic, and surname
# separated by spaces is given as input.
#
# Read this string and create a new string in the format:
#
# Surname F.P.
#
# where:
# - F is the first letter of the first name;
# - P is the first letter of the patronymic.
#
# Example:
# "Sergey Mikhailovich Balakirev"
# becomes:
# "Balakirev S.M."
#
# Input:
# A full name in the format:
# First name Patronymic Surname
#
# Output:
# The surname followed by the initials of the first name and patronymic.
#
# Example:
# Input:
# Sergey Mikhailovich Balakirev
#
# Output:
# Balakirev S.M.

full_name  = input().split()

print(full_name[-1], full_name[0][0] + "." + full_name[1][0] + ".")
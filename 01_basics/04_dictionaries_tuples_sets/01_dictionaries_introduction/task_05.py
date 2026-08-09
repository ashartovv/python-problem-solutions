# Input:
# Phone numbers are given in one line, separated by spaces.
# The numbers have different country codes: +7, +6, +2, +4, etc.
#
# Read the line and create a dictionary d.
#
# The dictionary keys must be the country codes (strings),
# such as '+7', '+6', '+2', etc.
#
# The values must be lists of phone numbers as strings
# with the corresponding country codes.
#
# The phone numbers in each list must remain in the same order
# as they appeared in the original input.
#
# Display the resulting dictionary using:
#
# print(*sorted(d.items()))
#
# Test data
#
# Input:
# +71234567890 +71234567854 +61234576890 +52134567890 +21235777890 +21234567110 +71232267890
#
# Output:
# ('+2', ['+21235777890', '+21234567110']) ('+5', ['+52134567890']) ('+6', ['+61234576890']) ('+7', ['+71234567890', '+71234567854', '+71232267890'])

lst_in = input().split()

d = {}

for number in lst_in:
    if number[0:2] in d:
        d[number[0:2]].append(number)
    else:
        d[number[0:2]] = [number]

print(*sorted(d.items()))
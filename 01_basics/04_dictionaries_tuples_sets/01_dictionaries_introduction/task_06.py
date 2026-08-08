# Input:
# Phone numbers are given together with names in the following format:
#
# phone_number_1 name_1
# phone_number_2 name_2
# ...
# phone_number_N name_N
#
# The input has already been read and stored as:
#
# lst_in = list(map(str.strip, sys.stdin.readlines()))
#
# The list has the following format:
#
# lst_in = ['phone_number_1 name_1', 'phone_number_2 name_2', ...]
#
# Create a dictionary d based on lst_in.
# The keys must be names.
# The values must be lists of phone numbers belonging to that name.
#
# One name can have multiple phone numbers.
#
# Display the resulting dictionary using:
#
# print(*sorted(d.items()))
#
# Test data
#
# Input:
# +71234567890 Sergey
# +71234567810 Sergey
# +51234567890 Mikhail
# +72134567890 Nikolay
#
# Output:
# ('Mikhail', ['+51234567890']) ('Nikolay', ['+72134567890']) ('Sergey', ['+71234567890', '+71234567810'])


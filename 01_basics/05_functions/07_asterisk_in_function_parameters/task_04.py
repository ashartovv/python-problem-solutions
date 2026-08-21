# Input:
# No direct input is required.
#
# Define the function filter_by_length(*args, min_length=0, max_length).
# It must accept any number of positional string arguments.
# min_length and max_length must be keyword-only arguments.
# Return a list containing only strings whose lengths are in the range
# [min_length, max_length], including both boundaries.
#
# Call the function with names_initial,
# min_length=5 and max_length=9.
# Store the result in names_result.
#
# Test data:
#
# Input:
# No input.
#
# Output:
# No output.

def filter_by_length(*strings, min_length=0, max_length):
    filtered_strings = []

    for value in strings:
        if min_length <= len(value) <= max_length:
            filtered_strings.append(value)

    return filtered_strings



names_initial = input().split()
names_result = filter_by_length(*names_initial, min_length=5, max_length=19)
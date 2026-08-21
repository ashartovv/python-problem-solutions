# Input:
# No input is required.
#
# Define the function merge_dicts(dict1, *args, ignored_keys=None).
# It must merge an arbitrary number of dictionaries.
# Keys from ignored_keys must be skipped.
# If the same key appears in several dictionaries, the later value replaces the earlier one.
# The original dictionaries must not be modified.
#
# Call the function with goods1, goods2, goods3, goods4
# and ignored_keys containing 'id', 'date', and 'cat_id'.
# Store the result in goods.
#
# Test data:
#
# Input:
# No input.
#
# Output:
# No output.

def merge_dicts(*dict1, ignored_keys=None):
    d = {}

    for arg in dict1:
        arg_copy = arg.copy()

        if ignored_keys is not None:
            for key in ignored_keys:
                del arg_copy[key]

        d = {**d, **arg_copy}
    return d


goods = merge_dicts(goods1, goods2, goods3, goods4, ignored_keys=('id', 'date', 'cat_id'))
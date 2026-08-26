# Input:
# d = [1, 2, [True, False], ["Москва", "Уфа", [100, 101], ['True', [-2, -1]]], 7.89]
#
# Output:
# [1, 2, True, False, "Москва", "Уфа", 100, 101, 'True', -2, -1, 7.89]
#
# Define a recursive function named get_line_list(d, a=None)
# that creates a one-dimensional list from the multidimensional list d.
#
# The function must return the newly created one-dimensional list.
# Nothing should be printed to the screen.
#
# d - the original list;
# a - the new list being formed.
#
# Starter code:

def get_line_list(d, a=None):
    if a is None:
        a = []
    # continue the function here
    for item in d:
        if isinstance(item, list):
            get_line_list(item, a)
        else:
            a.append(item)

    return a


d = [1, 2, [True, False], ["Москва", "Уфа", [100, 101], ['True', [-2, -1]]], 7.89]
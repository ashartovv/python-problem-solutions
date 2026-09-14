# Input:
# Two strings are given as input.
# Each string contains words separated by spaces.
# Read both strings and store them in two variables.
#
# Define a function with two parameters that receives the strings
# and converts them into two lists of words.
# The function must return a tuple containing these lists in order:
# first the list from the first string, then the list from the second string.
#
# Define a decorator for this function that takes the two lists
# returned by the function and creates a dictionary.
# The keys must be the words from the first list,
# and the values must be the corresponding elements from the second list.
# The lists are guaranteed to have the same length.
#
# The decorated function must return the resulting dictionary.
#
# Apply the decorator to the first function and call it
# using the two input strings.
#
# Store the resulting dictionary in variable d
# and display it using:
# print(*sorted(d.items()))
#
# Test data:
# Input:
# house river tree car
# дом река дерево машина
#
# Output:
# ('car', 'машина') ('house', 'дом') ('river', 'река') ('tree', 'дерево')

def get_dict(func):
    def wrapper(s1, s2):
        lst_t = func(s1, s2)
        lst_d = dict()
        for i in range(len(lst_t[0])):
            lst_d[lst_t[0][i]] = lst_t[1][i]
        return lst_d

    return wrapper


@get_dict
def get_lst(s1, s2):
    lst_1 = list(map(str, s1.split()))
    lst_2 = list(map(str, s2.split()))
    return lst_1, lst_2


str_1 = str(input())
str_2 = str(input())
d = get_lst(str_1, str_2)
print(*sorted(d.items()))
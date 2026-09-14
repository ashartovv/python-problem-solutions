# Input:
# The program reads a string containing menu item names separated by spaces.
#
# menu = input()
#
# Define a function named get_menu with the signature:
#
# def get_menu(s): ...
#
# The function must convert the string s into a list of words
# and return this list.
#
# Define a decorator named show_menu for the get_menu function.
# The decorator must display the resulting list in the following format:
#
# 1. Item_1
# 2. Item_2
# ...
# N. Item_N
#
# Apply the show_menu decorator to get_menu using the @ operator.
#
# Do not do anything else in the program.
# Do not call the functions.
#
# Tests:
#
# Test #1
# Input:
# Main Add Delete Exit
# Output:
# 1. Main
# 2. Add
# 3. Delete
# 4. Exit
#
# Test #2
# Input:
# Item1 Item2 Item3 Item4
# Output:
# 1. Item1
# 2. Item2
# 3. Item3
# 4. Item4
#
# Test #3
# Input:
# Moscow Tver Kazan Ufa Samara Voronezh
# Output:
# 1. Moscow
# 2. Tver
# 3. Kazan
# 4. Ufa
# 5. Samara
# 6. Voronezh

def show_menu(func):
    def wrapper(s):
        lst = func(s)
        for i in range(len(lst)):
            print(f"{i + 1}. {lst[i]}")

    return wrapper


@show_menu
def get_menu(s):
    return list(map(str, s.split()))


menu = input()
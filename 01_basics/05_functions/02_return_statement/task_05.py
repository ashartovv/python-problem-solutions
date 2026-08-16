# Input:
# A sequence of integer numbers is given in one line.
#
# Output:
# Declare a function with one parameter to check whether the given number is odd.
# The function must return True if the number is odd and False otherwise.
#
# After declaring the function, read the sequence of integers using:
# lst_d = list(map(int, input().split()))
#
# Then, using a list comprehension and the previously declared function,
# create a list lst containing only the odd values from lst_d.
# Display the result using:
# print(*lst)
#
# Test #1
# Input:
# 8 11 -15 3 2 10
#
# Output:
# 11 -15 3

def is_even(x):
    return x % 2 != 0


lst_d = list(map(int, input().split()))

lst = [value for value in lst_d if is_even(value)]

print(*lst)
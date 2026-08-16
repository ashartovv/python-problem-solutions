# Input:
# Declare a function that has one parameter accepting a string.
# The function must return the Boolean value False if the length of the passed
# string is less than 6 characters; otherwise, it must return the Boolean value True.
#
# After declaring the function, read from the input stream a string containing
# city names written on one line and separated by spaces.
# Form a list named cities from the read string.
#
# Then, using a list comprehension and the previously declared function,
# form a new list named lst containing the names of cities whose lengths
# are at least 6 characters. The cities are selected from the cities list.
#
# Display the result on the screen using the command:
# print(*lst)
#
# Test #1
# Input:
# Moscow Ufa Perm Samara Vologda
#
# Output:
# Moscow Samara Vologda
#
# Test #2
# Input:
# Voronezh London Tver Omsk Ufa
#
# Output:
# Voronezh London

def is_long(text):
    return len(text) >= 6


cities = input().split()
lst = [city for city in cities if is_long(city)]

print(*lst)
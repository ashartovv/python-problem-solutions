# Input:
# The program receives a string. Read this string from the input.
#
# Then, using the map() function, replace every Latin letter
# 'b', 'i', 't', 'B', 'I', 'T' with the '#' character.
#
# Leave all other characters unchanged.
#
# Display the transformed string on the screen.
#
# Tests:
#
# Test #1
# Input: Python is the best language!
# Output: Py#hon #s #he #es# language!
#
# Test #2
# Input: I love programming in Python
# Output: # love programm#ng #n Py#hon

lst = map(lambda s: "#" if s in ('b', 'i', 't', 'B', 'I', 'T') else s, input())

print(*lst, sep="")
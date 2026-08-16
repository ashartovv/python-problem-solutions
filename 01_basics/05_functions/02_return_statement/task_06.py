# Input:
# A string (word) is given and read into the variable tp using:
# tp = input().strip()
#
# Output:
# If tp is equal to the string "RECT", declare a function named get_sq
# with two parameters: the length and width of a rectangle.
# The function must calculate and return the area of the rectangle.
# The function must not print anything.
#
# If tp is not equal to "RECT", declare a function with the same name get_sq
# but with one parameter: the side length of a square.
# The function must calculate and return the area of the square using a * a.
# The function must not print anything.
#
# Only one get_sq function must be defined, depending on the value of tp.
# The function must not be called.
#
# Test #1
# Input:
# RECT
#
# Output:
# 10
#
# Test #2
# Input:
# SQ
#
# Output:
# 25

tp = input().strip()

#здесь продолжайте программу
if tp == "RECT":
    def get_sq(length, width):
        return length * width
else:
    def get_sq(length):
        return length ** 2
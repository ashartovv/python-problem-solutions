# Input:
# Declare a function with two parameters, width and height
# (the width and height of a rectangle).
# The function must print the following message:
# "The perimeter of the rectangle is equal to x"
# where x is the calculated perimeter of the rectangle.
#
# After declaring the function, read two integers using input(),
# written on one line and separated by a space,
# and call the function with these numeric values.
#
# Test data:
#
# Input:
# 8 11
#
# Output:
# The perimeter of the rectangle is equal to 38

def show_perimeter():
    width, height = map(int, input().split())
    perimeter = (width + height) * 2
    print(f"The perimeter of the rectangle is equal to {perimeter}")


show_perimeter()
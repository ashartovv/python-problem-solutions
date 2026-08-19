# Input:
# No input is required.
#
# Output:
# Declare a function named get_rect_value.
# Its first two parameters are the length and width of a rectangle (numbers).
# Its third parameter, tp, has a default value of 0.
#
# If tp is equal to 0, the function must return the perimeter
# of the rectangle calculated from the first two arguments.
# Otherwise, it must return the area of the rectangle.
#
# Do not call the function, only define it.
#
# Test data:
#
# Input:
# No input.
#
# Output:
# No output.

def get_rect_value(width, length, tp=0):
    if tp == 0:
        perimeter = (width + length) * 2
        return perimeter
    else:
        area = width * length
        return area
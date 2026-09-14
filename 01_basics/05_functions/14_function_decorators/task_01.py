# Input:
# Define a function named get_sq that calculates the area of a rectangle
# using two parameters: width and height.
#
# The function must return the calculated area and must not print anything.
#
# The function signature is:
#
# def get_sq(width, height): ...
#
# Define a decorator named func_show for this function.
# The decorator must display the returned result in the following format:
#
# Площадь прямоугольника: <value>
#
# Do not apply the decorator to the function.
# Do not call the function.

def func_show(func):
    def wrapper(width, height):
        print(f"Площадь прямоугольника: {func(width, height)}")

    return wrapper


def get_sq(width, height):
    return width * height
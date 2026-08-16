# Input:
# A floating-point number representing the weight of an object is given.
#
# Output:
# Declare a function with one parameter — the weight of the object.
# The function must print:
# "The object weighs: x kg."
# where x is the value passed to the function as an argument.
#
# After declaring the function, read a floating-point number using input()
# and call the function with this numeric value.
#
# Test data:
#
# Input:
# 12.67
#
# Output:
# The object weighs: 12.67 kg.

def show_weight():
    x = input()
    print(f"The object weighs: {x} kg.")


show_weight()
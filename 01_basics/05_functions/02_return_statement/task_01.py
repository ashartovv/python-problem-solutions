# Input:
# A floating-point number is given.
#
# Output:
# Declare a function named get_sq with one parameter.
# The function must return the parameter raised to the power of 2.
# After declaring the function, read a floating-point number using input()
# and call the function with the read value.
# Print the number returned by the function.
#
# Input:
# 1.5
#
# Output:
# 2.25

def get_sq(digit):
    return digit ** 2 if digit != 0 else None


print(get_sq(float(input())))
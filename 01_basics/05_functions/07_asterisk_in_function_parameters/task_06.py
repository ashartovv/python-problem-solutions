# Input:
# Define a function named get_params with the following parameters:
# - The first two parameters are named x and y. They can accept both
#   positional and keyword arguments.
# - The third parameter is named flags, has a default value of None,
#   and must accept keyword arguments only.
# - The fourth parameter is named func, has no default value,
#   and must accept keyword arguments only.
#
# The function must return a dictionary containing the arguments
# in the following format:
# {'x': x, 'y': y, 'flags': flags, 'func': func}
#
# Call get_params with the keyword arguments:
# x=10, y=20, flags=True, func='abs'.
# Store the result in a variable named params.
# Do not print anything to the screen.
#
# Test data:
# Input:
# get_params(x=10, y=20, flags=True, func='abs')
#
# Output:
# params = {'x': 10, 'y': 20, 'flags': True, 'func': 'abs'}

def get_params(x , y, *, flags=None, func):
    return {'x': x, 'y': y, 'flags': flags, 'func': func}


params = get_params(x=10, y=20, flags=True, func='abs')
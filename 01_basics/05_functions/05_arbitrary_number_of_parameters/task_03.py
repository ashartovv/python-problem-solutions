# Input:
# No input is required.
#
# Output:
# Declare a function named get_data_fig to calculate the perimeter
# of an arbitrary N-sided polygon.
#
# The function receives N side lengths through its positional arguments.
#
# It may also receive the following named arguments:
# - tp — a Boolean value True/False;
# - color — an integer value;
# - closed — a Boolean value True/False;
# - width — a floating-point value.
#
# The function must return a tuple containing the polygon's perimeter
# and the specified named parameter values in the order listed above,
# but only for parameters that were actually passed.
#
# If a parameter was not passed, it must be omitted from the returned tuple.
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
def get_data_fig(*side_len, **kwargs):
    result = (sum(side_len),)
    possible_args = ("tp", "color", "closed", "width")

    for arg in possible_args:
        if arg in kwargs:
            result = result + (kwargs[arg],)

    return result
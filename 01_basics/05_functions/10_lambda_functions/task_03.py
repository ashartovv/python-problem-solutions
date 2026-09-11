# Input:
# Declare an anonymous (lambda) function for calculating the absolute value
# of a number (negative numbers must be converted to positive).
#
# Read the number x from the input stream using:
# x = float(input())
#
# Call the lambda function for the number x.
# Display the result of the function on the screen.
#
# Tests:
#
# Test #1
# Input: -5.6
# Output: 5.6
#
# Test #2
# Input: -7
# Output: 7.0
#
# Test #3
# Input: 3
# Output: 3.0

get_positive = lambda x : -x if x < 0 else x
x = float(input())

print(get_positive(x))
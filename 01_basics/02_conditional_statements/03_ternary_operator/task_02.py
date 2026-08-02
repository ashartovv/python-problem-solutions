# Problem:
# An integer is given as input.
#
# Read this number and assign the following string to the variable msg:
#
# "multiple of 3" if the entered number is divisible by 3;
# "not multiple of 3" if the entered number is not divisible by 3.
#
# Implement the program using the ternary operator.
#
# Output the value of the variable msg.
#
# Example:
#
# Input:
# 9
#
# Output:
# multiple of 3

number = int(input())

msg = "multiple of 3" if number % 3 == 0 else "not multiple of 3"

print(msg)
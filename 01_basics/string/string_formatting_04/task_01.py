# Problem:
# The following data is given as input, each on a new line:
# - first name (string);
# - last name (string);
# - age (positive integer).
# Read the input and use the format() method to create
# the following string:
#
# "Dear <first name> <last name>! Congratulations on your <age>th birthday!"
#
# Display the resulting string without quotation marks.
#
# Input:
# The first name, last name, and age, each on a separate line.
#
# Output:
# A formatted congratulatory message.
#
# Example:
# Input:
# John
# Smith
# 25
#
# Output:
# Dear John Smith! Congratulations on your 25 birthday!

name = str(input())
surname = str(input())
age = int(input())

print(f"Dear {name} {surname}! Congratulations on your {age} birthday!")
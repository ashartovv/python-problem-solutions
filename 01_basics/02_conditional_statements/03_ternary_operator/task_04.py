# Problem:
# An integer 0 or 1 is given as input.
#
# Read this number and convert it into a string according to the rule:
#
# 0 -> "False"
# 1 -> "True"
#
# Implement the program using the ternary conditional operator.
#
# Output the result string.
#
# Example:
#
# Input:
# 1
#
# Output:
# True

number = int(input())

msg = "True" if number == 1 else "False"

print(msg)
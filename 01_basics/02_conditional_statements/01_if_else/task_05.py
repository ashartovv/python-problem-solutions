# Problem:
# A four-digit number is given as input.
#
# Read the number and check whether it ends with the digit 7.
#
# If the number ends with 7, output:
#
# YES
#
# Otherwise, output:
#
# NO
#
# Example:
#
# Input:
# 8117
#
# Output:
# YES

number = input()

if number.endswith("7"):
    print("YES")
else:
    print("NO")
# Problem:
# A phone number is given as input in the following format:
#
# +7(xxx)xxx-xx-xx
#
# Read this string and convert it into a list named `lst`
# character by character (each element of the list is one character).
#
# Then:
# - remove the first '+' symbol;
# - replace the digit 7 with 8;
# - remove all hyphens '-'.
#
# Display the resulting list as a string using:
#
# print("".join(lst))
#
# Input:
# A phone number in the format +7(xxx)xxx-xx-xx.
#
# Output:
# The modified phone number in the format 8(xxx)xxx-xxxx.
#
# Example:
# Input:
# +7(912)123-45-67
#
# Output:
# 8(912)1234567

lst = list(input())
lst.remove("+")
lst[0] = "8"
lst.remove("-")
lst.remove("-")

print("".join(lst))
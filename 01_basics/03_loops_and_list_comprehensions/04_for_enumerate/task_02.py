# Problem:
# A phone number is given as input.
#
# The expected format is:
#
# +7(xxx)xxx-xx-xx
#
# where:
# x = any digit (0–9).
#
# The total number of characters is always correct
# (there will be no missing or extra characters).
#
# Read the input string and check whether it matches
# the required phone number format.
#
# Output:
# "YES" if the format is correct.
# "NO" otherwise.
#
# Example:
#
# Input:
# +7(123)456-78-99
#
# Output:
# YES

number = input()
pattern = "+7(xxx)xxx-xx-xx"

result = "YES"

if len(number) != len(pattern):
    result = "NO"
else:
    for i, ch in enumerate(number):
        if pattern[i] == "x":
            if not ch.isdigit():
                result = "NO"
                break
        elif ch != pattern[i]:
            result = "NO"
            break

print(result)
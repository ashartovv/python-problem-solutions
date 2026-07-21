# Problem:
# An amateur boxer's weight (in kilograms) is given as a floating-point number.
#
# Read the weight and determine the boxer's weight category number.
#
# Categories:
#
# 1 - Lightweight:
#     weight <= 60 kg
#
# 2 - Light welterweight:
#     weight <= 64 kg
#
# 3 - Welterweight:
#     weight <= 69 kg
#
# 4 - Heavyweight:
#     weight > 69 kg
#
# Output only the category number.
#
# Example:
#
# Input:
# 62.4
#
# Output:
# 2

weight = float(input())

if weight <= 60:
    print("1")
elif 60 < weight <= 64:
    print("2")
elif 64 < weight <= 69:
    print("3")
else:
    print("4")
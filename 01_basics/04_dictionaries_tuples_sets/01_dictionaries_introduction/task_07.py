# Input:
# Positive integers are given one at a time.
#
# Read the numbers using a loop until the number 0 is entered.
#
# For each number, calculate its square root rounded to two decimal places
# and print the result on a separate line.
#
# Use a dictionary to cache the calculated results.
# If the same number is entered again, do not calculate its square root.
# Instead, use the previously calculated value from the dictionary.
#
# When a cached value is used, print:
#
# Value from cache: <number>
#
# Use the round() function for rounding.
#
# Test data
#
# Input:
# 1
# 2
# 3
# 3
# 2
# 4
# 0
#
# Output:
# 1.0
# 1.41
# 1.73
# Value from cache: 1.73
# Value from cache: 1.41
# 2.0

import math

d = {}

while True:
    n = int(input())
    if n == 0:
        break
    elif n in d:
        print(f"значение из кэша: {d[n]}")
    else:
        d[n] = round(math.sqrt(n), 2)
        print(d[n])
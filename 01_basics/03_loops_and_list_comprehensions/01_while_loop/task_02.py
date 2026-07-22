# Problem:
# A real number is given as input: the price of one book x rubles.
#
# Read this number and output, in one line separated by spaces,
# the prices of 2, 3, ..., 10 such books with accuracy to one decimal place.
#
# Implement the program using a while loop.
#
# Example:
#
# Input:
# 34.6
#
# Output:
# 69.2 103.8 138.4 173.0 207.6 242.2 276.8 311.4 346.0

x = float(input())
prices = []
i = 1

while i < 10:
    i += 1
    prices.append(round(x * i, 2))

print(*prices)
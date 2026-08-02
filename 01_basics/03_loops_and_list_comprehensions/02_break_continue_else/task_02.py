# Problem:
# Write a program that repeatedly reads integers
# (one per line) using a while loop.
#
# Compute the product of positive numbers only.
#
# Stop reading input when the number 0 is encountered.
#
# Negative numbers must be skipped using the continue statement.
#
# If 0 appears immediately or before any positive number,
# the product should be considered equal to 1.
#
# Output the resulting product.
#
# Example:
#
# Input:
# 2
# -1
# 3
# 2
# -5
# 7
# 0
#
# Output:
# 84

n_sum = 1

while True:
    n = int(input())
    if n == 0:
        break
    if n < 0:
        continue

    n_sum *= n

print(n_sum)
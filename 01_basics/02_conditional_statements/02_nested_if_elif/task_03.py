# Problem:
# An integer representing the total purchase amount in a store is given as input.
#
# Read this number and calculate the final purchase amount after applying
# the following discounts:
#
# - If the amount is less than 1000:
#     discount = 0%
#
# - If the amount is from 1000 (inclusive) to 5000 (exclusive):
#     discount = 5%
#
# - If the amount is from 5000 (inclusive) to 10000 (exclusive):
#     discount = 10%
#
# - If the amount is greater than or equal to 10000:
#     discount = 15%
#
# Save the final purchase amount in the variable `result_sum`.
#
# Output `result_sum` with two decimal places:
#
# print(f"{result_sum:.2f}")
#
# Example:
#
# Input:
# 999
#
# Output:
# 999.00

purchases_total = int(input())

if purchases_total < 1000:
    discount = 0
elif purchases_total < 5000:
    discount = 5
elif purchases_total < 10000:
    discount = 10
else:
    discount = 15

result_sum = purchases_total - purchases_total * discount / 100

print(f"{result_sum:.2f}")
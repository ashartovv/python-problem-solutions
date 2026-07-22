# Problem:
# A citizen opened a bank account on January 1, depositing 1000 rubles.
#
# Every year, the deposit increases by 5% of its current amount.
#
# Determine the amount of money in the account after n years,
# where n is a positive integer read from the input.
#
# Round the result to two decimal places using the round() function
# and output it.
#
# Implement the program using a while loop.
#
# Example:
#
# Input:
# 5
#
# Output:
# 1276.28

investment = 1000
n = int(input())

while n:
    investment *= 1.05
    n -= 1

print(round(investment, 2))
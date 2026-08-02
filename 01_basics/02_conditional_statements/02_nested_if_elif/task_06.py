# Problem:
# A bank client withdraws money from an ATM.
# The withdrawal amount (an integer number of rubles) is entered using:
#
# withdraw = int(input())
#
# Output a message according to the following rules:
#
# - If the withdrawal amount is not a multiple of 100:
#     Output:
#     "Error: enter an amount that is a multiple of 100"
#
# - If the requested amount exceeds the client's balance of 410123 rubles:
#     Output:
#     "Insufficient funds"
#
# - If the requested amount is greater than 50000 rubles:
#     Output:
#     "Single withdrawal limit exceeded"
#
# - If all conditions are satisfied:
#     Output:
#     "Withdrawn: <withdraw> rub."
#
# Example:
#
# Input:
# 500
#
# Output:
# Withdrawn: 500 rub.

withdraw = int(input())
balance = 410123

if withdraw > balance:
    print("Insufficient funds")
elif withdraw > 50000:
    print("Single withdrawal limit exceeded")
elif withdraw % 100 != 0:
    print("Error: enter an amount that is a multiple of 100")
else:
    print(f"Withdrawn: {withdraw} rub.")
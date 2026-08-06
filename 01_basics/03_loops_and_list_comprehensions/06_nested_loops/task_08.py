# Input: a natural number n.
#
# A country uses banknotes with the following denominations:
# 1, 2, 4, 8, 16, 32, and 64.
#
# Read the number n and determine the minimum number
# of banknotes needed to make the amount n.
#
# Print the list of banknotes used to form the sum,
# starting from the largest denomination to the smallest.
#
# It is assumed that there is an unlimited supply
# of banknotes of each denomination.
#
# Example:
#
# Input:
# 221
#
# Output:
# 64 64 64 16 8 4 1

n = int(input())

banknotes = [64, 32, 16, 8, 4, 2, 1]
used_banknotes = []

while n:
    for index in range(len(banknotes)):
        for count in range(n):
            if n >= banknotes[index]:
                used_banknotes.append(banknotes[index])
                n -= banknotes[index]
            else:
                break

print(*used_banknotes)
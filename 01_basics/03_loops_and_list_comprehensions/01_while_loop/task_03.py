# Problem:
# A positive integer n is given as input.
#
# Read this number, then calculate and output the following sum
# with accuracy to three decimal places:
#
# S = 1 + 1/2 + 1/3 + ... + 1/n
#
# Implement the program using a while loop.
#
# Example:
#
# Input:
# 8
#
# Output:
# 2.718

n = int(input())

i = 1
s = 0

while i <= n:
    s += 1 / i
    i += 1

print(f"{s:.3f}")
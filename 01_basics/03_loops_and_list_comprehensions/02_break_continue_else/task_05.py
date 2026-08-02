# Problem:
# A natural number n (a positive integer) is given as input.
#
# Read this number.
# Using a while loop, iterate through all integers
# in the range [1; n] (including both boundaries)
# and create a list of numbers that are divisible
# by both 3 and 5.
#
# If n is less than 100, output the resulting list
# of numbers in one line separated by spaces.
#
# Otherwise, output the message:
#
# "n is too large"
#
# Design the program logic so that the else block
# after the while loop is executed.
#
# Example:
#
# Input:
# 49
#
# Output:
# 15 30 45
#
# Example:
#
# Input:
# 100
#
# Output:
# n is too large

n = int(input())
i = 1

while i <= n:
    if i % 15 == 0:
        print(i, end=" ")
        i += 14
        continue

    if n >= 100:
        print("n is too large")
        break

    i += 1
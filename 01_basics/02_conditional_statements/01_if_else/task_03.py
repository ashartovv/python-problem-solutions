# Problem:
# Two positive integers are given in one line,
# separated by a space.
#
# Read these numbers into variables `m` and `n`
# in the order they are entered.
#
# Determine whether `m` is divisible by `n` without a remainder.
#
# If `m` is divisible by `n`, output the integer result of the division.
#
# Otherwise, output:
#
# "<m> is not divisible by <n> without a remainder"
#
# Example:
#
# Input:
# 13 2
#
# Output:
# 13 is not divisible by 2 without a remainder

m, n = map(int, input().split())

if m % n == 0:
    print(m // n)
else:
    print(f"{m} is not divisible by {n} without a remainder")
# Problem:
# Three positive integers (each with at most three digits) are given
# on a single line, separated by spaces.
# Read the numbers and pad one-digit and two-digit numbers
# with leading zeros so that each number contains exactly three digits.
# Display the resulting numbers, each on a new line.
#
# Input:
# Three positive integers separated by spaces.
#
# Output:
# Three numbers, each consisting of exactly three digits,
# displayed one per line.
#
# Example:
# Input:
# 8 11 123
#
# Output:
# 008
# 011
# 123

a, b, c = map(str, input().split(" "))

print(a.rjust(3, "0"), b.rjust(3, "0"), c.rjust(3, "0"), sep="\n")
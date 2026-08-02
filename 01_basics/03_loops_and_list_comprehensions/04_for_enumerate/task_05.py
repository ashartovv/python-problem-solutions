# Input: integers written in one line separated by spaces.
# Read them and store them in the list `digits`.
#
# Then replace each element of the list with the square of the corresponding number.
# The program must use the `enumerate()` function.
#
# Example:
#
# Input:
# 8 -11 4 3 6
#
# Output:
# 64 121 16 9 36

digits = list(map(int, input().split()))

for index, value in enumerate(digits):
    digits[index] = digits[index] ** 2

print(*digits)
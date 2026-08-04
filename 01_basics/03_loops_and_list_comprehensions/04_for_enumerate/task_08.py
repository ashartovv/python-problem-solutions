# Input: a string containing an arithmetic expression.
#
# Examples:
# "10 + 25 - 12"
# "10+25-12+20-1+3"
#
# The expression may contain any number of additions (+)
# and subtractions (-). Spaces around operators may or may not
# be present.
#
# Operands are integers only.
#
# Read the expression, evaluate it, and print the result.
#
# Do NOT use the built-in function `eval()`.
#
# Example:
#
# Input:
# 10+25 - 12
#
# Output:
# 23

N = list(input().replace(' ', '').replace('+', ' + ').replace('-', ' - ').split())

if N[0] == '-':
    N[0] += N.pop(1)

result = int(N[0])

for index, digit in enumerate(N):
    if digit == '+' and N[index + 1] != '-':
        result += int(N[index + 1])
        index += 1
    elif digit == '-' and N[index + 1] != '-':
        result -= int(N[index + 1])
        index += 1
    elif digit == '+' and N[index + 1] != '-':
        del N[index], N[index + 1]
        result -= int(N[index])
        index += 1
    elif digit == '-' and N[index + 1] != '-':
        del N[index], N[index + 1]
        result += int(N[index])
        index += 1


print(result)
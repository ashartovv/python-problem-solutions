# Problem:
# A sequence of integers (at least four) is given as input,
# separated by spaces.
#
# Read these numbers and find the three smallest numbers among them.
#
# Display these three numbers in ascending order on one line,
# separated by spaces.
#
# The program must be implemented without using conditional statements.
#
# Input:
# A sequence of integers separated by spaces.
#
# Output:
# The three smallest numbers in ascending order.
#
# Example:
# Input:
# 8 11 -5 10 -1 0 7
#
# Output:
# -5 -1 0

numbers = list(map(int, input().split()))
numbers.sort()

print(*numbers[:3])
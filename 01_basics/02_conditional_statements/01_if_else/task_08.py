# Problem:
# Four integers a, b, c, d are given in one line,
# separated by spaces.
#
# The first two numbers represent the inner dimensions
# of an envelope in millimeters: a and b.
#
# The next two numbers represent the dimensions
# of a rectangular postcard: c and d.
#
# Determine whether the postcard can fit into the envelope.
#
# The postcard needs a 1 mm gap on each side,
# so its dimensions must be smaller than the envelope dimensions
# by 2 mm in total (1 mm on each side).
#
# The postcard can be rotated by 90 degrees.
#
# Output:
#
# YES - if the postcard fits into the envelope.
# NO - otherwise.
#
# Example:
#
# Input:
# 12 5 7 2
#
# Output:
# YES

a, b, c, d = map(int, input().split())

if c <= a - 2 and d <= b - 2 or d <= a - 2 and c <= b - 2:
    print("YES")
else:
    print("NO")
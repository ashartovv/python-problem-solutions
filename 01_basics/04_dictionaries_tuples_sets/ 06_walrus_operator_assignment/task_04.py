# Input:
#
# Read integers from the input stream using int(input()).
#
# Use a while loop and the walrus operator.
#
# The loop must continue until a negative number or 0 is entered.
#
# Calculate the product of only the numbers divisible by 3.
#
# If no number divisible by 3 is encountered, the product must remain 1.
#
# The int(input()) command must appear only once.
#
# Print the resulting product.
#
# Input:
# 1
# 2
# 3
# 4
# 5
# 6
# 0
#
# Output:
# 18

s = 1
multipliers_count = 0

while (x := int(input())) > 0:
    if x % 3 == 0:
        s *= x
        multipliers_count += 1

if multipliers_count == 0:
    s = 1

print(s)
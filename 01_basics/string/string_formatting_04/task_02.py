# Problem:
# Three integer dimensions of a product are given as input:
# width, depth, and height, written on one line separated by spaces.
# Read these numbers and use the format() method with named arguments
# to create a string according to the template:
#
# "Dimensions: <width> x <depth> x <height>"
#
# Display the resulting string without quotation marks.
#
# Input:
# Three integers separated by spaces representing the width, depth, and height.
#
# Output:
# A string containing the product dimensions in the specified format.
#
# Example:
# Input:
# 10 20 30
#
# Output:
# Dimensions: 10 x 20 x 30

width, depth, height = map(int,input().split())

print(f"Dimensions: {width} x {depth} x {height}")
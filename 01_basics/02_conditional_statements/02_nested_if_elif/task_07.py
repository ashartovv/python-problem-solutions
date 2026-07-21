# Problem:
# Two real numbers are given as coordinates of a point on a plane.
# They are read using the command:
#
# x, y = map(float, input().split())
#
# Determine the number of the quadrant to which the point with coordinates (x, y) belongs.
#
# Output the corresponding quadrant:
#
# - "I quadrant"   if x > 0 and y > 0
# - "II quadrant"  if x < 0 and y > 0
# - "III quadrant" if x < 0 and y < 0
# - "IV quadrant"  if x > 0 and y < 0
#
# Points located on the boundaries of the quadrants (on the axes) do not need to be considered.
# It is assumed that the coordinates x and y belong to one of the four regions.
#
# Test data:
#
# Input:
# 2.5 3.4
#
# Output:
# I quadrant

x, y = map(float, input().split())

if x > 0 and y > 0:
    print("I quadrant")
elif x < 0 and y > 0:
    print("II quadrant")
elif x < 0 and y < 0:
    print("III quadrant")
else:
    print("IV quadrant")
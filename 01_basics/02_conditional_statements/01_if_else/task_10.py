# Problem:
# The pedestrian traffic light works according to the following schedule:
#
# At the beginning of each hour, the green light is on for 3 minutes.
# Then the red light is on for 2 minutes.
# Then the green light is on again for 3 minutes, and so on.
# This process repeats continuously.
#
# A real number t is given as input.
# It represents the number of minutes that have passed since the
# beginning of the current hour.
#
# Read t and determine which color is shown for pedestrians at time t.
#
# Output:
#
# "green" - if the green light is on;
# "red" - if the red light is on.
#
# Example:
#
# Input:
# 12.5
#
# Output:
# green

t = float(input())

if t % 5 >= 3:
    print("red")
else:
    print("green")
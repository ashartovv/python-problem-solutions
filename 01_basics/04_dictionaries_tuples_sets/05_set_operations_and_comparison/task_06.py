# Input:
#
# Two lines containing lists of cities visited by Sergey during
# the 1st and 2nd years of his trip across Russia are given.
# City names are separated by spaces.
#
# Read both lines and store them as separate lists or tuples.
#
# Determine whether the route in the 2nd year included every city
# that Sergey visited in the 1st year.
#
# If the 2nd year's route contains all cities from the 1st year,
# display:
#
# YES
#
# Otherwise, display:
#
# NO
#
# Test data
#
# Input:
# Moscow Kazan Samara Moscow
# Moscow Vladimir Novgorod Kazan Samara Moscow
#
# Output:
# YES

cities_1 = tuple(input().split())
cities_2 = tuple(input().split())

if set(cities_1) <= set(cities_2):
    print("YES")
else:
    print("NO")
# Problem:
# A natural number x is given as input.
#
# A skier ran 10 km on the first day of training.
# Each following day, the skier increased the distance
# by 10% of the previous day's distance.
#
# Determine on which day the skier will run more than x km.
#
# Read x from the input and output the required day.
#
# Implement the program using a while loop.
#
# Example:
#
# Input:
# 20
#
# Output:
# 9

x = int(input())
distances = [10, ]

i = 0
while distances[-1] <= x:
    distances.append(distances[i] + distances[i] * 0.1)
    i += 1

print(len(distances))
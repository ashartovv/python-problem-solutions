# Input:
# Import only two functions from the random module: seed and random.
# Give the imported random() function the alias rnd.
#
# Execute the following operations:
# seed(10)
# print(round(rnd(), 2))
#
# Test data:
# Input:
# No input is required.
#
# Output:
# 0.57

from random import seed, random as rnd

seed(10)
print(round(rnd(), 2))
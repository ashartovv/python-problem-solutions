# Input:
# Import only the seed() and randint() functions from the random module.
# Then execute the following operations:
# - Call seed(1) to initialize the random number generator.
# - Call randint(10, 50) and print the returned random integer.
#
# Test data:
# Input:
# No input is required.
#
# Output:
# 18

from random import seed, randint

seed(1)
print(randint(10, 50))
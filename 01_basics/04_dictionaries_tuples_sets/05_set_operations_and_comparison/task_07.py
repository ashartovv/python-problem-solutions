# Input:
#
# A natural number is given. It can contain only the prime factors
# 1, 2, 3, 5, and 7 (any of them, not necessarily all).
#
# Read the number and decompose it into prime factors.
#
# Then check whether its prime factorization contains the factors
# 2, 3, and 5 (all three are required, at least once each).
#
# If it contains all three factors, display:
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
# 210
#
# Output:
# YES

N = int(input())
multipliers = {2, 3, 5}
N_multipliers = set()

for value in multipliers:
    if N % value == 0:
        N_multipliers.add(value)

if multipliers <= N_multipliers:
    print("YES")
else:
    print("NO")
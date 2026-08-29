# Input:
# A natural number N representing the number of the mark the frog needs to reach.
#
# The frog can jump forward either 1 mark or 2 marks.
# Determine the number of possible routes by which the frog can reach mark N.
#
# Define a recursive function named get_path.
#
# The number of routes is calculated as:
# get_path(N) = get_path(N - 1) + get_path(N - 2)
#
# Initial conditions:
# get_path(0) -> 0
# get_path(1) -> 1
# get_path(2) -> 2
#
# The function must return the number of possible routes.
#
# Call get_path for the input number N and print the result.
#
# Test data:
#
# Input:
# 7
#
# Output:
# 21

def get_path(N):
    if N in {0, 1, 2}:
        return N

    return get_path(N - 1) + get_path(N - 2)


N = int(input())
print(get_path(N))
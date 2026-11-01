# Define a generator function named get_sum(total).
# The function must yield the cumulative sum of integers from 1 to total,
# inclusive: first 1, then 1 + 2, then 1 + 2 + 3, and so on.
# Do not use collections.
# The function must be defined but not called.

def get_sum(total):
    sum = 0
    for x in range(1, total+1):
        sum += x
        yield sum


N = int(input())
# Read two sequences of integers and convert them into sets.

# Find the numbers that are present in both sets.

# Use filter() with an anonymous function to keep only even numbers.

# Sort the resulting numbers in ascending order.

# Print the numbers in one line, separated by spaces.

arr_1 = set(filter(lambda x: x % 2 == 0, map(int, input().split())))
arr_2 = set(filter(lambda x: x % 2 == 0, map(int, input().split())))

print(*sorted(arr_1 & arr_2))
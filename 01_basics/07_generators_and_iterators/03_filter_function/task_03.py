# Read the input integers and split them into a list.

# Use filter() with an anonymous function to keep only
# two-digit numbers, including negative two-digit numbers.

# Print the remaining numbers in one line, separated by spaces.

result = filter(lambda x: len(x.strip('-')) == 2, map(str, input().split()))

print(*list(result))
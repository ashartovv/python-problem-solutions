# Define a generator function named moving_average(data, window_size=3).
# It should calculate the average of each consecutive window of window_size elements.
# Shift the window one position to the right after each calculation.
# Yield each calculated average.
# Read the input data as a tuple of integers and read window_size.
# Store all generated averages in a list named results.
# Do not print anything.

def moving_average(data, window_size=3):
    for i in range(len(data) - window_size + 1):
        value_sum = 0
        for j in range(i , i + window_size):
            value_sum += data[j]

        yield round(value_sum / window_size, 2)


data = tuple(map(int, input().split()))
ws = int(input())

results = list(moving_average(data, ws))
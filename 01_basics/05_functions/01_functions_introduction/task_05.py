# Input:
# A line containing integers separated by spaces.
#
# Output:
# Declare a function with one parameter — a list.
# The function must find the minimum value, maximum value,
# and sum of the values in the list.
# It must print:
# "Min = v_min, max = v_max, sum = v_sum"
# where v_min, v_max, and v_sum are the calculated values.
#
# After declaring the function, read the list of integers
# using input() and call the function with this list.
#
# Test data:
#
# Input:
# 8 11 5 -10 12 0
#
# Output:
# Min = -10, max = 12, sum = 26

def show_stats():
    values_lst = list(map(int, input().split()))
    print(f"Min = {min(values_lst)}, max = {max(values_lst)}, sum = {sum(values_lst)}")


show_stats()
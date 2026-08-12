# Input:
#
# A string containing a starting numerical value followed by grade names.
#
# Read the input string and split it into separate elements.
#
# The first element is the starting numerical value.
#
# The remaining elements are grade names.
#
# Create a dictionary using a dictionary comprehension.
#
# The dictionary keys must increase by 1 starting from the starting value.
#
# The dictionary values must be the corresponding grade names in the same order.
#
# Print the value associated with the key 4.
#
# Test data:
#
# Input:
# 1 awful unsatisfactory satisfactory decent excellent
#
# Output:
# decent

lst_in = input().split()

d_grades = {
    index + int(lst_in[0]): value
    for index, value in enumerate(lst_in[1:])
}

print(d_grades[4])
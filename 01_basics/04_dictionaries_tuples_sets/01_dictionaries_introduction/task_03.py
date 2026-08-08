# A line is given containing key=value pairs separated by spaces.
# All keys are strings.
#
# Read the line and create a dictionary from these pairs.
# Then check whether the dictionary contains all of these keys:
# 'house', 'True', and '5'.
#
# If all three keys exist, print "YES".
# Otherwise, print "NO".
#
# Test data
#
# Input:
# Vologda=city house=home True=1 5=excellent 9=divine
#
# Output:
# YES

lst_in = input().split()

d = dict([
    [value for value in row.split('=')]
    for row in lst_in
])

if 'house' in d and 'True' in d and '5' in d:
    print("NO")
else:
    print("YES")
# A line is given containing key=value pairs separated by spaces.
# Both keys and values are strings.
#
# Read the line and create a dictionary d from these pairs.
# Then remove the keys 'False' and '3' if they exist.
#
# Display the resulting dictionary using:
#
# print(*sorted(d.items()))
#
# Test data
#
# Input:
# Lena=name Don=river Moscow=city False=false 3=satisfactory True=true
#
# Output:
# ('True', 'true') ('Don', 'river') ('Lena', 'name') ('Moscow', 'city')

lst_in = input().split()

d = dict([
    [value for value in row.split('=')]
    for row in lst_in
])

if 'False' in d:
    del d['False']

if '3' in d:
    del d['3']

print(*sorted(d.items()))
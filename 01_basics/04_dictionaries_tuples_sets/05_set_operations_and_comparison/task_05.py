# Input:
#
# The student's grades for Informatics are given as integers
# from 2 to 5, separated by spaces.
#
# Read these grades and store them in a collection.
#
# If the student has at least one grade of 2,
# they are not allowed to take the exam.
#
# Display:
#
# ADMITTED
#
# if there are no grades of 2,
# otherwise display:
#
# NOT ADMITTED
#
# Use a set to check whether the grade 2 is present.
#
# Test data
#
# Input:
# 3 4 4 5 2 3
#
# Output:
# NOT ADMITTED

informatics = set(map(int, input().split()))

if 2 in informatics:
    print("NOT ADMITTED")
else:
    print("ADMITTED")
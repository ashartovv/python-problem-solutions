# Input:
# Open the file 'projects/python/works.my' for reading using UTF-8 encoding.
# Read characters 10 through 20 (inclusive) and store the resulting
# string in the variable fragment. Close the file after processing.
# Do not print anything.

fp = open("projects/python/works.my", encoding="utf-8")
fp.read(9)
fragment = fp.read(11)
fp.close()
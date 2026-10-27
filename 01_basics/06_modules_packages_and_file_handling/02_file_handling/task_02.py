# Input:
# Open the file 'sites/links.txt' for reading using the 'windows-1251'
# encoding. Determine the size of the file in bytes and store it in
# the variable size_file. Close the file after processing.
# Do not print anything.

f_inp = open("sites/links.txt", encoding='windows-1251')
size_file = len(f_inp.read())
f_inp.close()
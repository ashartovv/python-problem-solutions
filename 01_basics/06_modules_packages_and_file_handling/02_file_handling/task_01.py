# Input:
# Open the file 'log.dat' in the current working directory for reading
# using UTF-8 encoding. Read its first and last lines and store them
# in the variables header and last_data, respectively.
# Close the file after processing. Do not print anything.

f_log = open("log.dat", encoding="utf-8")

header = f_log.readline()
for line in f_log:
    last_data = line

f_log.close()
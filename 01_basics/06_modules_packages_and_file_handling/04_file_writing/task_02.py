# Using the with statement, open the file 'log_stats.txt' in the 'work_data'
# subdirectory for reading and appending in text mode with UTF-8 encoding.
# Append the following line to the file:
# msg = input()svg
# Read the very first line of the file into the variable header.
# Do not print anything to the screen.

msg = input()

with open('work_data/log_stats.txt', 'a+', encoding='utf-8') as file:
    file.write(msg)
    file.seek(0)
    header = file.readline()
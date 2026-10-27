# Input:
# Use a context manager to open the file 'diagnostics.csv' in the current
# working directory for reading with UTF-8 encoding.
# Handle FileNotFoundError using try/except. If the file cannot be opened,
# set success_open_file to False; otherwise, set it to True.
# Read the first two lines and store them in the variables header and row,
# respectively. Do not close the file manually or print anything.

try:
    with open('diagnostics.csv', encoding='utf-8') as file:
        success_open_file = True
        header, row = file.readline(), file.readline()

except FileNotFoundError:
    success_open_file = False
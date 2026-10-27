# Input:
# Open the file 'bank.csv' in the current working directory for reading
# with UTF-8 encoding, using a context manager.
# Handle FileNotFoundError with try/except, taking no action in the
# exception handler.
# The first line contains comma-separated field names, and the second
# line contains the corresponding values.
# Read these two lines and create a dictionary named row_data, using
# the field names as keys and the corresponding values as dictionary values.
# Remove newline characters ('\n') from keys and values without changing
# any other characters.
# Do not close the file manually or print anything.

try:
    with (open('bank.csv', encoding='utf-8') as file):
        keys = file.readline().strip().split(',')
        row_data = {
            keys[key]: value
            for key, value in enumerate(file.readline().strip().split(','))
        }

except FileNotFoundError:
    pass
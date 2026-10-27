# Input:
# Use a context manager to open the file 'images/targets.dat' in the
# current working directory for reading with UTF-8 encoding.
# Handle FileNotFoundError using try/except and handle all other
# exceptions with a separate except block.
# Initialize success_open_file and success_file_operations to True.
# If FileNotFoundError occurs, set success_open_file to False.
# If any other exception occurs, set success_file_operations to False.
# Read the last line of the file and store it in last_row.
# Do not close the file manually or print anything.

success_open_file = True
success_file_operations = True
try:
    with open('images/targets.dat', encoding='utf-8') as file:
        for line in file:
            last_row = line

except FileNotFoundError:
    success_open_file = False

except:
    success_file_operations = False
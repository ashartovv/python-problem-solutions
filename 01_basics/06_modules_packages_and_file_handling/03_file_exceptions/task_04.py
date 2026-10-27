# Use a context manager to open the file 'logs/01-01-2025/log_app.txt'
# in read mode with UTF-8 encoding.
# Handle FileNotFoundError using try/except without performing any action.
# Read the file and store only the log entries containing '[ERROR]'
# in the list log_errors, preserving their original order.
# Remove newline characters ('\n') from the stored strings.
# Do not print anything.

try:
    with open('logs/01-01-2025/log_app.txt', encoding='utf-8') as file:
        log_errors = [line.strip() for line in file if '[ERROR]' in line]

except FileNotFoundError:
    pass
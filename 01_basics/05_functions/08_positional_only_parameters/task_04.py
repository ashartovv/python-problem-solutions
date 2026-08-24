# Input:
# Two lines are read from stdin:
# 1. log_time — integer timestamp of the log.
# 2. log_msg — log message text.
#
# Define the function log_event(timestamp, message, /, *, level=INFO,
# format_log="[%(time)] %(levelname) - %(message)").
#
# The function must return a formatted log string only if the numeric
# log level is INFO or higher. Otherwise, return None.
#
# Supported format specifiers:
# %(time)      — timestamp
# %(message)   — log message
# %(levelname) — level name such as DEBUG, INFO, WARNING, ERROR, CRITICAL
# %(levelno)   — numeric level such as 10, 20, 30, 40, 50
#
# Call log_event with:
# - log_time as timestamp;
# - log_msg as message;
# - level=WARNING;
# - format_log="%(levelname) - (%(time)) %(message)"
#
# Store the result in log_item and print it.
#
# Test data:
#
# Input:
# 1764230394
# Server started
#
# Output:
# WARNING - (1764230394) Server started

DEBUG = 10, 'DEBUG'
INFO = 20, 'INFO'
WARNING = 30, 'WARNING'
ERROR = 40, 'ERROR'
CRITICAL = 50, 'CRITICAL'


def log_event(timestamp, message, /, *, level=INFO, format_log="[%(time)] %(levelname) - %(message)"):
    if level[0] < INFO[0]:
        return None

    text_log = (format_log
                .replace('%(time)', str(timestamp))
                .replace('%(levelname)', level[1])
                .replace('%(message)', message)
                .replace("%(levelno)", str(level[0])))

    return text_log


log_time = int(input())
log_msg = input()

log_item = log_event(log_time, log_msg, level=WARNING, format_log="%(levelname) - (%(time)) %(message)")
print(log_item)
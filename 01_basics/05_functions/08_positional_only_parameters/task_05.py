# Input:
# A string containing data.
#
# Define a function named parser_data with the following parameters:
# text — a string containing the data; positional arguments only.
# max_count=0 — the maximum number of values to extract; accepts
# both positional and keyword arguments.
# ignore_sign=False — a flag indicating whether signs should be ignored;
# keyword arguments only.
#
# The parser_data function must extract all integers from the string text
# in the order in which they appear and return their string representations
# as a list.
#
# If there are no integers in text, return an empty list.
#
# If max_count is 0, the number of extracted integers is unlimited.
# If max_count is positive, extract only the first max_count integers.
#
# If ignore_sign=True, all plus and minus signs before numbers must be
# removed. Otherwise, the signs must be preserved.
#
# Examples:
#
# parser_data("Numbers: -10, -+40, 4-53, 1, 2-3 -0.01")
# -> ['-10', '+40', '4', '-53', '1', '2', '-3', '-0', '01']
#
# parser_data("Numbers: -10, -+40, 4-53, 1, 2-3 -0.01",
#             max_count=7, ignore_sign=False)
# -> ['-10', '+40', '4', '-53', '1', '2', '-3']
#
# parser_data("Add the absolute values: 1 2 3, then -10, -20 and 12",
#             5, ignore_sign=True)
# -> ['1', '2', '3', '10', '20']
#
# Call parser_data to process the input string stored in data_text.
# Use max_count=5 and ignore_sign=True.
# Store the returned value in result.
#
# No output is required.
#
# Test data:
#
# Input:
# Numbers: -10, -+40, 4-53, 1, 2-3 -0.01
#
# Output:
# No output.

def parser_data(text, /, max_count=0, *, ignore_sign=False):
    numbers = []
    number = ''
    for index, ch in enumerate(text):
        if max_count and len(numbers) == max_count:
            break
        elif ch.isdecimal():
            if ignore_sign == False and index != 0 and text[index - 1] in {"-", "+"}:
                number += text[index - 1]
            number += ch
        elif not ch.isdecimal() and number:
            numbers.append(number)
            number = ''
    if number:
        numbers.append(number)

    return numbers


data_text = input()
result = parser_data(data_text, 5, ignore_sign=True)
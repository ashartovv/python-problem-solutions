# Input:
# The first line contains a string of text.
# The second line contains a string of characters.
#
# Define the function count_chars with parameters:
# s - the text string;
# chars - the string of characters to search for;
# return_type=tuple - the return type, keyword-only;
# ignore_case=True - whether to ignore letter case, keyword-only.
#
# The function must count how many times each character from chars
# occurs in s and return the result as the specified collection type.
# If ignore_case=True, case must be ignored in both s and chars.
#
# Call count_chars with text, symbols, return_type=set,
# and ignore_case=False.
# Store the result in the variable result.
#
# Nothing should be printed.
#
# Test data:
#
# Input:
# The Python interpreter and the extensive standard LIBRARY ARE freely available
# aFspR
#
# Output:
# No output

def count_chars(s, chars, *, return_type=tuple, ignore_case=True):
    result = []

    if ignore_case:
        chars = chars.lower()
        s = s.lower()

    for char in chars:
        result.append(s.count(char))

    return return_type(result)


text = input()
symbols = input()

result = count_chars(text, symbols, return_type=set, ignore_case=False)
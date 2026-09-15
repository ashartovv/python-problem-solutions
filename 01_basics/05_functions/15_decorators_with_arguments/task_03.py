# Input:
# Declare a function that accepts a string containing Cyrillic characters
# and other characters and transliterates Russian letters into Latin letters
# using the dictionary t provided in the task.
#
# The function must convert the input string to lowercase before performing
# the replacements, so the replacements are case-insensitive.
#
# The function must return the transformed string.
#
# Define a decorator with a parameter chars, whose default value is " !?".
# The decorator must:
# 1. Replace every character from chars with "-".
# 2. Replace any sequence of consecutive hyphens with a single "-".
# 3. Return the resulting string.
#
# Apply the decorator with chars="?!:;,. " to the transliteration function.
# Read the string s from the input stream.
# Call the decorated function with s and print the result.
#
# Test data:
# Input:
# Decorators - are awesome!
#
# Output:
# decorators-are-awesome-

t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
     'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
     'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
     'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}

def change_chars(chars=" !?"):
    def latin(func):
        def wrapper(s):
            result = func(s)
            for ch in result:
                if chars.count(ch):
                    result = result.replace(ch, '-')

            while result.count('--'):
                result = result.replace('--', '-')

            return result

        return wrapper

    return latin


@change_chars(chars="?!:;,. ")
def get_latin(s):
    result = ''
    for ch in s.lower():
        if ch in t:
            result += t[ch]
        else:
            result += ch

    return result


s = input()
print(get_latin(s))
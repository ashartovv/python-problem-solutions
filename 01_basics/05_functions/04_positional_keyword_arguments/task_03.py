# Input:
# Declare a function that takes a string as its first parameter
# (containing Cyrillic and Latin characters) and converts Cyrillic characters
# to Latin characters using the following dictionary for replacing Russian
# letters with their corresponding Latin transliteration:
#
# t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
#      'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
#      'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
#      'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}
#
# The function must return the converted string.
# The replacement must be case-insensitive: first convert the original
# string to lowercase.
#
# The second parameter, named sep, has a default value of "-".
# It determines the character used to replace spaces in the string.
#
# After declaring the function, read the input string.
# Then call the function twice and print the results:
# 1. First, using only the input string.
# 2. Second, using the input string and the named argument sep="+"
#
# Test data:
#
# Input:
# Лучший курс по Python!
#
# Output:
# luchshiy-kurs-po-python!
# luchshiy+kurs+po+python!

t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
     'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
     'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
     'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}

def get_latin(text, sep="-"):
    lst = [
        sep if cyrillic == " "
        else t[cyrillic] if cyrillic in t
        else cyrillic
        for cyrillic in text.lower()
    ]
    return ''.join(lst)


input_str = input()

print(get_latin(input_str))
print(get_latin(input_str, sep='+'))
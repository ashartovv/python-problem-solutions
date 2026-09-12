# Input:
# The program receives a string. Read this string from the input.
#
# A dictionary named t is already declared in the program.
# It contains mappings from Cyrillic letters to their Latin equivalents.
#
# Using the dictionary t, apply the map() function to transform
# each character of the input string.
#
# Cyrillic letters must be replaced with their corresponding
# Latin representations, regardless of letter case.
#
# All other characters must be replaced with the hyphen character "-".
#
# Then, form a single string from the transformed fragments.
# The fragments must follow one another without spaces.
#
# Display the resulting string on the screen.
#
# Test #1
# Input:
# Привет Питон
#
# Output:
# privet-piton

t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
     'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
     'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
     'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}

lst = map(lambda x: '-' if x == ' ' else t[x], input().lower())
print(*lst, sep='')
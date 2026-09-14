# Input:
# A string containing Cyrillic and Latin characters is given.
# Read the string using input() and store it in variable s.
#
# Define a function that transliterates Russian Cyrillic letters
# into Latin letters using the provided dictionary t.
#
# Convert the input string to lowercase before processing it.
#
# Non-letter characters " : ; . , _" must be replaced with "-".
# Other characters that are not in the transliteration dictionary
# should remain unchanged.
#
# Define a decorator for this function that replaces multiple
# consecutive hyphens with a single hyphen.
#
# The decorator must return the resulting string and must not
# print anything itself.
#
# Apply the decorator to the transliteration function.
# Call the decorated function for the input string s
# and display the result.
#
# Transliteration dictionary:
# ё -> yo, а -> a, б -> b, в -> v, г -> g, д -> d, е -> e,
# ж -> zh, з -> z, и -> i, й -> y, к -> k, л -> l, м -> m,
# н -> n, о -> o, п -> p, р -> r, с -> s, т -> t, у -> u,
# ф -> f, х -> h, ц -> c, ч -> ch, ш -> sh, щ -> shch,
# ъ -> "", ы -> y, ь -> "", э -> e, ю -> yu, я -> ya
#
# Test data:
# Input:
# Python - это круто!
# Output:
# python-eto-kruto!

t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
     'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
     'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
     'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}

def latin_deco(func):
    def wrapper(s):
        latin = func(s)

        while latin.count('--'):
            latin = latin.replace('--', '-')

        return latin

    return wrapper


@latin_deco
def get_latin(s):
    latin = ''
    for ch in list(s.lower()):
        if ch in t:
            latin += t[ch]
        elif " : ;.,_".count(ch):
            latin += '-'
        else:
            latin += ch

    return latin


s = input()
print(get_latin(s))
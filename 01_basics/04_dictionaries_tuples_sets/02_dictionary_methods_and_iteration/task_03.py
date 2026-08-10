# Input:
#
# An encoded string using the Morse code alphabet is given.
# The Morse codes are separated by spaces.
#
# Decode the string using the Morse code alphabet
# from the previous exercise.
#
# All letters in the resulting string must be lowercase.
#
# Print the decoded message as a string.
#
# Note:
# The letters e and ё correspond to the same Morse code,
# so always use the letter 'e' in the decoded message.
#
# Test data
#
# Input:
# .-- ... . -...- .-- . .-. -. ---
#
# Output:
# все верно

morse_ru = {
    'а': '.-', 'к': '-.-', 'х': '....',
    'б': '-...', 'л': '.-..', 'ц': '-.-.',
    'в': '.--', 'м': '--', 'ч': '---.',
    'г': '--.', 'н': '-.', 'ш': '----',
    'д': '-..', 'о': '---', 'щ': '--.-',
    'е': '.', 'п': '.--.', 'ъ': '--.--',
    'ё': None, 'р': '.-.', 'ы': '-.--',
    'ж': '...-', 'с': '...', 'ь': '-..-',
    'з': '--..', 'т': '-', 'э': '..-..',
    'и': '..', 'у': '..-', 'ю': '..--',
    'й': '.---', 'ф': '..-.', 'я': '.-.-',
    ' ': '-...-'
}

N = input().split()

for morse in N:
    for key, value in morse_ru.items():
        if morse == value:
            print(key, end='')
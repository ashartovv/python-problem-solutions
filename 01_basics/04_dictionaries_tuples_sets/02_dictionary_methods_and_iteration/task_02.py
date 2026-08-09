# Input:
#
# A string consisting of Russian letters and spaces is given.
# Read the string and encode it using the Morse code alphabet.
#
# Each letter must be replaced with its corresponding Morse code,
# consisting of dots and dashes.
#
# The space character also has a Morse code:
# -...-
#
# A space must be placed after each encoded character
# to separate the Morse codes.
#
# There must be no space after the final Morse code.
#
# The Morse codes for the Russian alphabet are:
#
# А    .-       М    --       Ш    ----
# Б    -...     Н    -.       Щ    --.-
# В    .--      О    ---      Ъ    --.--
# Г    --.      П    .--.     Ы    -.--
# Д    -..      Р    .-.      Ь    -..-
# Е (Ё) .       С    ...      Э    ..-..
# Ж    ...-     Т    -        Ю    ..--
# З    --..     У    ..-      Я    .-.-
# И    ..       Ф    ..-.     ' '  -...-
# Й    .---     Х    ....
# К    -.-      Ц    -.-.
# Л    .-..     Ч    ---.
#
# Print the encoded result as a single string.
#
# For practice, it is better to create the dictionary yourself.
# Programming often involves this kind of routine work.
#
# Test data
#
# Input:
# Сергей Балакирев
#
# Output:
# ... . .-. --. . .--- -...- -... .- .-.. .- -.- .. . .-. . .--

morse_ru = {
    'а': '.-', 'к': '-.-', 'х': '....',
    'б': '-...', 'л': '.-..', 'ц': '-.-.',
    'в': '.--', 'м': '--', 'ч': '---.',
    'г': '--.', 'н': '-.', 'ш': '----',
    'д': '-..', 'о': '---', 'щ': '--.-',
    'е': '.', 'п': '.--.', 'ъ': '--.--',
    'ё': '.', 'р': '.-.', 'ы': '-.--',
    'ж': '...-', 'с': '...', 'ь': '-..-',
    'з': '--..', 'т': '-', 'э': '..-..',
    'и': '..', 'у': '..-', 'ю': '..--',
    'й': '.---', 'ф': '..-.', 'я': '.-.-',
    ' ': '-...-'
}

N = input().lower()

for ch in N:
    print(morse_ru[ch], end=' ')
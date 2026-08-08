# Input:
# A test web server returns HTML pages for URL addresses (strings).
# Different URL addresses are given, each on a new line.
#
# The input has already been read and stored as:
#
# lst_in = list(map(str.strip, sys.stdin.readlines()))
#
# Go through the list of URLs using a loop.
#
# If a URL appears for the first time:
# print:
#
# HTML-страница для адреса <URL>
#
# and save this string in a dictionary using the current URL as the key.
#
# If the URL appears again:
# get the previously saved string from the dictionary and print:
#
# Взято из кэша: HTML-страница для адреса <URL>
#
# Print each message on a new line.
#
# Important:
# Check repeated URLs using dictionary keys.
#
# Test data
#
# Input:
# ustanovka-i-zapusk-yazyka
# ustanovka-i-poryadok-raboty-pycharm
# peremennyye-operator-prisvaivaniya-tipy-dannykh
# arifmeticheskiye-operatsii
# ustanovka-i-poryadok-raboty-pycharm
#
# Output:
# HTML-страница для адреса ustanovka-i-zapusk-yazyka
# HTML-страница для адреса ustanovka-i-poryadok-raboty-pycharm
# HTML-страница для адреса peremennyye-operator-prisvaivaniya-tipy-dannykh
# HTML-страница для адреса arifmeticheskiye-operatsii
# Взято из кэша: HTML-страница для адреса ustanovka-i-poryadok-raboty-pycharm


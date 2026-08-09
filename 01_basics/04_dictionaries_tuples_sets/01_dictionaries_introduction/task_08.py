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
# If a URL appears for the first time, print:
#
# HTML page for address <URL>
#
# and save this string in a dictionary using the current URL as the key.
#
# If the URL appears again, get the previously saved string from the dictionary
# and print:
#
# Taken from cache: HTML page for address <URL>
#
# Print each message on a new line.
#
# Important:
# Check repeated URLs using dictionary keys.
#
# Test data
#
# Input:
# installation-and-launch-of-language
# installation-and-pycharm-work-order
# variables-assignment-operator-data-types
# arithmetic-operations
# installation-and-pycharm-work-order
#
# Output:
# HTML page for address installation-and-launch-of-language
# HTML page for address installation-and-pycharm-work-order
# HTML page for address variables-assignment-operator-data-types
# HTML page for address arithmetic-operations
# Taken from cache: HTML page for address installation-and-pycharm-work-order

import sys

lst_in = list(map(str.strip, sys.stdin.readlines()))

url_dict = {}

for url in lst_in:
    if url in url_dict:
        print(f"Взято из кэша: {url_dict[url]}")
    else:
        url_dict[url] = f"HTML-страница для адреса {url}"
        print(url_dict[url])
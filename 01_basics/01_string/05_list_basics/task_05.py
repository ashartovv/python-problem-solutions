# Problem:
# The following information about a book is given as input,
# each on a separate line:
# - title (string);
# - author (string);
# - number of pages (integer);
# - price (floating-point number).
#
# Read the input and store the values in a list named `book`
# in the order they were entered.
#
# Then:
# - remove the third element (number of pages);
# - replace the author's name with "Pushkin";
# - double the price.
#
# Display the resulting `book` list using:
#
# print(book)
#
# Input:
# The title, author, number of pages, and price,
# each on a separate line.
#
# Output:
# The modified `book` list.
#
# Example:
# Input:
# The Great Gatsby
# Fitzgerald
# 180
# 25.50
#
# Output:
# ['The Great Gatsby', 'Pushkin', 51.0]

name = str(input())
author = str(input())
page_count = int(input())
price = float(input())

book_lst = [name, author, page_count, price]
del book_lst[2]
book_lst[1] = "Pushkin"
book_lst[-1] *= 2

print(book_lst)
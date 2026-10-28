# Using the with statement, open the file 'letter.txt' for writing in text mode
# with UTF-8 encoding in the current working directory.
# Write the following line to the file:
# msg = input()
# Do not print anything to the screen.

msg = input()

with open('letter.txt', 'w', encoding='utf-8') as file:
    file.write(msg)
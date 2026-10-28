# Using the with statement, open the files 'text_1' and 'text_2' for reading
# with UTF-8 encoding. Both files are located in the 'lib' subdirectory.
# Use try/except to handle FileNotFoundError if either file is missing.
#
# If both files are opened successfully, read all their contents, skipping
# the first line of each file.
# Write the data from 'text_1' first, followed by a newline and the data
# from 'text_2', to 'text_all.txt' in the current working directory.
# Use Windows-1251 encoding for the output file.
# Do not print anything to the screen.

try:
    with open('lib/text_1', encoding='utf-8') as file_1, open('lib/text_2', encoding='utf-8') as file_2:
        file_1.readline()
        file_2.readline()

        with open('text_all.txt', 'w', encoding='windows-1251') as file_all:
            file_all.writelines([*file_1.readlines(), '\n', *file_2.readlines()])

except FileNotFoundError:
    pass
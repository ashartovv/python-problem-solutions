# Using the with statement, open the files 'python_base.dat' and 'java_base.dat'
# for reading with UTF-8 encoding. Both files are located in the 'lang_doc'
# subdirectory.
# Use try/except to handle FileNotFoundError if either file is missing.
#
# If both files are opened successfully, swap their contents.
# Do not print anything to the screen.

try:
    with open('lang_doc/python_base.dat', encoding='utf-8') as python_base, \
            open('lang_doc/java_base.dat', encoding='utf-8') as java_base:
        file_1 = python_base.read()
        file_2 = java_base.read()

    with open('lang_doc/python_base.dat', 'w', encoding='utf-8') as python_base, \
            open('lang_doc/java_base.dat', 'w', encoding='utf-8') as java_base:
        python_base.write(file_2)
        java_base.write(file_1)

except FileNotFoundError:
    pass
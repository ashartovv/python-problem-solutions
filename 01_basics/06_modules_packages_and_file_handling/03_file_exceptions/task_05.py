# Open the file 'python/course_text.txt' in read mode with 'windows-1251' encoding
# using a context manager.
# Handle FileNotFoundError without performing any action.
# Read the file until the first occurrence of the word 'python' is found,
# ignoring case.
# Stop at the first character 'p' of that word, leaving 'python' unread.
# Do not print anything.

try:
    with open('python/course_text.txt', encoding='windows-1251') as file:
        while True:
            position = file.tell()
            ch = file.read(1).lower()
            if ch == 'p':
                word = ""
                word += ch
                for _ in range(5):
                    word += file.read(1).lower()
                if word == 'python':
                    file.seek(position)
                    break
            elif ch == '':
                break

except FileNotFoundError:
    pass
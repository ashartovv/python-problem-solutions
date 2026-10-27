# Input:
# Open the file 'staff/persons.dat' for reading using UTF-8 encoding.
# Each line contains an employee's first name, patronymic, and surname.
# Find the line number containing the first name 'Сергей' and surname
# 'Балакирев', regardless of the patronymic. The matching line is unique
# or may be absent. If no match exists, set num_person to 0.
# Store the line number in num_person and close the file.
# Do not print anything.

fp = open("staff/persons.dat", encoding="utf-8")
num_person = 0
for index, line in enumerate(fp):
    values = line.split()
    if values[0] == "Сергей" and values[2] == "Балакирев":
        num_person = index + 1
    break
fp.close()
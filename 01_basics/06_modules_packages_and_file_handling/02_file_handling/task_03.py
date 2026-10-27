# Input:
# Open the file 'course.new.dat' in the current working directory for
# reading using UTF-8 encoding. Read the first five and last five
# characters and store them in the variables start_5 and end_5,
# respectively. Close the file after processing.
# Do not print anything.

f_text = open('course.new.dat', encoding="utf-8")
text = f_text.read()
start_5 = text[:5]
end_5 = text[-5:]
f_text.close()
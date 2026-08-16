# Input:
# Read first name and last name from the input stream in one line,
# separated by a space.
#
# Output:
# Print the message:
# Dear <first name> <last name>, You have completed this task correctly!
#
# After declaring the function, call it.
#
# Input:
# Sergey Balakirev
#
# Output:
# Dear Sergey Balakirev, you completed this task correctly!

def show_appeal():
    first_name, last_name = input().split()
    print(f"Dear {first_name} {last_name}, you completed this task correctly!")


show_appeal()
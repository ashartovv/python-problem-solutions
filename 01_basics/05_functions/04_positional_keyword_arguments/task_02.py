# Input:
# No input is required.
#
# Output:
# Declare a function named check_password.
# The first parameter accepts a string representing a password.
# The second parameter, chars, has a default value of "$%!?@#".
#
# The function must check whether the password contains at least one
# character from chars and whether the password length is at least 8 characters.
# If both conditions are satisfied, the function returns True.
# Otherwise, it returns False.
#
# Do not call the function, only define it.
#
# Test data:
#
# Input:
# No input.
#
# Output:
# No output.

def check_password(password, chars="$%!?@#"):
    if len(password) >= 8 and set(chars) & set(password):
        return True
    else:
        return False
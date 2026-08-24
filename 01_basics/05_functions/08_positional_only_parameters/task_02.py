# Input:
# A string containing a password.
#
# Define the function verify_password(psw, /, chars="@#!*", min_length=8).
# The parameter psw must accept only positional arguments.
# The parameters chars and min_length must accept both positional and keyword arguments.
#
# The password is valid if:
# - its length is at least min_length;
# - it contains at least one character from chars;
# - it does not contain any Russian letters, uppercase or lowercase.
#
# Return True if the password is valid, otherwise return False.
#
# Call verify_password with:
# chars="0123456789"
# min_length=10
# Store the result in resu.
#
# Test data:
#
# Input:
# VBNFGfdg!9
#
# Output:
# No output.

def verify_password(psw, /, chars="@#!*", min_length=8):
    cyrillic_ch = "абвгдеёжзийклмнопрстуфхцчшщьыъэюя"

    is_long = len(psw) >= min_length
    has_chars = bool(set(psw) & set(chars))
    cyrillic = bool(set(psw) & set(cyrillic_ch)) or bool(set(psw) & set(cyrillic_ch.upper()))

    return is_long and has_chars and not cyrillic


password = input()
result = verify_password(password, chars="0123456789", min_length=10)

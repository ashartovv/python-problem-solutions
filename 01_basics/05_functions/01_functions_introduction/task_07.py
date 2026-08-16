# Input:
# Declare a function with one parameter that checks whether the given
# email address is valid.
# The email address is considered valid if it обязательно contains
# the characters '@' and '.', while all other characters may be:
# 'a-z', 'A-Z', '0-9', and '_'.
# If the email address is valid, the function must print "YES";
# otherwise, it must print "NO".
#
# After declaring the function, read a string containing an email address
# using input() and call the function with this argument.
#
# Test data:
#
# Input:
# sc_lib@list.ru
#
# Output:
# YES

def check_mail(mail):
    valid_chars = set('abcdefghijklmnopqrstuvwxyz0123456789._@')
    mail = set(mail.lower())
    if (mail <= valid_chars) and (set('@.') <= mail):
        print('YES')
    else:
        print('NO')


check_mail(input())
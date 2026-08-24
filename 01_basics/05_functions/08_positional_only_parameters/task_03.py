# Input:
# A string containing a phone number.
#
# Define the function check_phone(phone, format_phone="8(xxx)xxx-xx-xx", /, format_symbol='x').
# The parameters phone and format_phone must accept only positional arguments.
# format_symbol must accept both positional and keyword arguments.
#
# The function must check whether phone exactly matches format_phone.
# The character specified by format_symbol represents any digit from 0 to 9.
# Return True if the phone number matches the format, otherwise return False.
#
# Call check_phone with phone_number using the format:
# +7(***)***-****
# and format_symbol='*'.
# Store the result in result.
#
# Test data:
#
# Input:
# +7(903)703-0611
#
# Output:
# No output.

def check_phone(phone, format_phone="8(xxx)xxx-xx-xx", /, format_symbol='x'):
    for index, ch in enumerate(format_phone):
        if ch != format_symbol and ch != phone[index]:
            return False
        elif ch == format_symbol:
            if not phone[index].isdecimal():
                return False

    return True


phone_number = input()
result = check_phone(phone_number, "+7(***)*** ****", format_symbol='*')
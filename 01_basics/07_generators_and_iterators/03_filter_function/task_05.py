# Read the input string and split it into email addresses.

# Use filter() with an anonymous function to keep only addresses
# that contain Latin letters, digits, underscores, and the required symbols.
# Each address must contain "@" followed by a ".".

# Print the valid email addresses in their original order,
# separated by spaces.

def is_valid_email(email):
    if email.index('@') > email.index('.'):
        return False

    for char in email:
        if 'a' <= char.lower() <= 'z' or char in ['_', '.', '@'] or char.isdigit():
            continue

        else:
            return False

    return True


emails = filter(is_valid_email, map(str, input().split()))
print(*list(emails))
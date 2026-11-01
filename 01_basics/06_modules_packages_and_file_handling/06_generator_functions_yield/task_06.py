# Define a generator function length_email(emails, min_length=5).
# Yield strings that contain exactly one '@' character
# and have at least min_length characters before '@'.

# Define a generator function rus_domain(gen_func).
# Yield strings from gen_func that end with '.ru'.

# Read the input email addresses using input().split().
# Call length_email with min_length=10.
# Pass the resulting generator to rus_domain.
# Store all yielded strings in a list named results.
# Print the elements of results on one line, separated by spaces.
def length_email(emails, min_length=5):
    for email in emails:
        if email.count('@') == 1 and email.index('@') >= min_length:
            yield email


def rus_domain(gen_func):
    for i in gen_func:
        if i.endswith('.ru'):
            yield i


emails = input().split()
gen_valid = length_email(emails, min_length=10)
results = list(rus_domain(gen_valid))
print(*results)

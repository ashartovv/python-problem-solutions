# Input:
# Declare a function that converts all characters in a string to lowercase
# and returns the result.
#
# Define a decorator for this function with one parameter tag,
# which has the default value "h1".
# The decorator must wrap the string returned by the function
# inside the specified HTML tag and return the result.
#
# Example:
# "python" -> "<h1>python</h1>"
#
# Apply the decorator with tag="div" to the function.
# Read the string s from the input stream and call the decorated function.
# Print the result.
#
# Test data:
# Input:
# Decorators are awesome!
#
# Output:
# <div>decorators are awesome!</div>

def get_tagged(tag = 'h1'):
    def get_func(func):
        def wrapper(s):
            return f"<{tag}>{func(s)}</{tag}>"
        return wrapper
    return get_func


@get_tagged(tag='div')
def get_lower(s):
    return s.lower()


s = input()
print(get_lower(s))
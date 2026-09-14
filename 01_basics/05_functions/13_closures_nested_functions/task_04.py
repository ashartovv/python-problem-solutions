# Input:
# Define an outer function with no parameters.
#
# Inside it, define a nested function with one parameter
# that receives a string.
#
# The outer function must return a reference to the nested function.
#
# The nested function must wrap the string passed through its parameter
# in an h1 tag and return the resulting string.
#
# For example:
# Input string: "Python"
# Result: "<h1>Python</h1>"
#
# Then read a string from the input stream.
# Call the outer function to obtain a reference to the nested function.
# Call the nested function through this reference, passing the input string.
# Print the result.
#
# Tests:
#
# Test #1
# Input: Balakirev
# Output: <h1>Balakirev</h1>
#
# Test #2
# Input: Sergey
# Output: <h1>Sergey</h1>
#
# Test #3
# Input: Hello Python!
# Output: <h1>Hello Python!</h1>

def cache(tag):
    def text(text):
        return f"<{tag}>{text}</{tag}>"

    return text


tag = cache(input())
print(tag(input()))
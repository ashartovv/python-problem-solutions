# Input:
# Declare a function that takes a string as its first parameter.
# The second parameter, tag, has a default value of "h1" and specifies
# the HTML tag in which the first string should be enclosed.
#
# For example, if the string is "Hello Python" and the tag is "h1",
# the function must return:
# "<h1>Hello Python</h1>"
#
# The function must return a string where the opening tag is placed
# at the beginning and the corresponding closing tag is placed
# at the end of the string.
#
# After declaring the function, read a string from the input stream
# and call the function twice, printing the result each time:
# 1. First, with only the input string.
# 2. Second, with the input string and the named argument tag="div".
#
# Test data:
#
# Input:
# Работаем с функциями
#
# Output:
# <h1>Работаем с функциями</h1>
# <div>Работаем с функциями</div>

def get_tagged(text, tag="h1"):
    return f"<{tag}>{text}</{tag}>"


input_str = input()

print(get_tagged(input_str))
print(get_tagged(input_str, tag='div'))
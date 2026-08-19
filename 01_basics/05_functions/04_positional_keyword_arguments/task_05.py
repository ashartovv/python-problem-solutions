# Input:
# Extend the function from the previous task by adding a third parameter, up,
# with a default Boolean value of True.
#
# If up is True, the tag specified by the tag parameter must be written
# in uppercase letters.
# If up is False, the tag must be written in lowercase letters.
#
# After declaring the function, read a string from the input stream
# and call the function twice, printing the result each time:
# 1. With the string and the named argument tag="div".
# 2. With the string, the named argument tag="div", and the named argument
#    up=False.
#
# Test data:
#
# Input:
# Python is the best!
#
# Output:
# <DIV>Python is the best!</DIV>
# <div>Python is the best!</div>

def get_tagged(text, tag="h1", up=True):
    if up:
        return f"<{tag.upper()}>{text}</{tag.upper()}>"
    else:
        return f"<{tag}>{text}</{tag}>"


input_str = input()

print(get_tagged(input_str, tag='div'))
print(get_tagged(input_str, tag='div', up=False))
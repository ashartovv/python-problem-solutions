# Input:
# The program reads two strings: a first name and a last name.
# Complete the body of the function func2 with a command
# that allows the function to change the value of the existing
# variable msg declared in the function func1.
#
# Input:
# Sergey
# Balakirev
# Output:
# Balakirev
# Balakirev

def func1():
    msg = input()


    def func2():
        nonlocal msg
        msg = input()
        print(msg)


    func2()
    print(msg)


func1()
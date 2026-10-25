# Input:
# At the beginning of the program, before the existing function definition,
# import the factorial function from the math module using the from statement.
# Give the imported function the name fact to prevent a naming conflict
# with the function named factorial that is already defined in the program.
# Do not modify the existing factorial function.
# Do not call either function. Only write the import statement.
#
# Test data:
# Input:
# An existing function named factorial.
# The factorial function from the math module must be imported as fact.
#
# Output:
# No output. Only the import statement must be added.

from math import factorial as fact

def factorial(n):
    p = 1
    for i in range(2, n+1):
        p *= i

    print("my factorial")
    return p
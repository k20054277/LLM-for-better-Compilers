
# Original program
def original_program():
    a = 10
    b = None
    c = a + b

    print(c)

# Refactored program
def refactor_program():
    a = 10
    c = a + None

    print(c)

# Driver code
original_program()
refactor_program()

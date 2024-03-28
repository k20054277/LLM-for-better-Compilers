
# This is a comment - anything after the '#' symbol is ignored by the interpreter

# Assigning the boolean value 'True' to a variable
is_rainy = True

print("Is it rainy? ", is_rainy)

def is_even(number):
    """
    This function takes an integer as an argument and returns 'True' if the number is even, otherwise returns 'False'.
    """

    # The 'if' statement checks if the condition inside the parentheses is True or False
    if number % 2 == 0:
        return True
    else:
        return False

number = int(input("Enter a number: "))
result = is_even(number)
print(f"{number} is even? {result}")

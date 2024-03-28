
# This is a comment - anything after the '#' symbol is ignored by the interpreter

def is_positive(number):
    # The function checks if the given number is positive
    if number > 0:
        return True
    else:
        return False

number = 5
if is_positive(number):
    print("The number is positive.")
else:
    print("The number is not positive.")

# Notice how the indentation of the print statements aligns with 'if' and 'else' keywords

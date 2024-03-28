
def divide(x, y):
    """This function takes two arguments x and y, and returns the quotient of x by y."""
    result = x / y
    assert y != 0, "Error! Division by zero is not allowed."
    return result

num1 = 10
num2 = 2

if num2 == 0:
    print("Invalid argument! Cannot divide by zero.")
else:
    quotient = divide(num1, num2)
    if quotient.is_integer():
        print(f"The quotient of {num1} by {num2} is a integer: {quotient}")
    else:
        print(f"The quotient of {num1} by {num2} is not an integer.")
    
# The assert statement checks if y is zero before performing the division. If it is, then the program raises an AssertionError
# with the provided error message. Otherwise, the divide function calculates and returns the quotient as usual.

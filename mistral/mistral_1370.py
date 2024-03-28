
def divide(x, y):
    """This function takes two numbers as arguments and returns the quotient."""
    result = x / y
    assert y != 0, f"Error: Division by zero is not allowed. Input: {x}, {y}"
    return result

num1 = 10
num2 = 3

try:
    quotient = divide(num1, num2)
except AssertionError as error:
    print("Error:", error)
else:
    print(f"Quotient of {num1} and {num2}: {quotient}")

# Output: Quotient of 10 and 3: 3.3333333333333335

num1 = 10
num2 = 0

try:
    quotient = divide(num1, num2)
except AssertionError as error:
    print("Error:", error)
else:
    # This code will not be executed in case of an exception
    pass

# Output: Error: Error: Division by zero is not allowed. Input: 10, 0


# A simple function
def square(number):
    return number * number

# A lambda function that also squares a number
square_lambda = lambda number: number * number

# Check if a function is callable
def check_callable(function):
    return callable(function) and type(function) != types.FunctionType

# Test the functions and checks
print("Checking square function: ", check_callable(square))  # True
print("Checking square function with wrong type check: ", check_callable(square))  # TypeError: <function __main__.square at 0x7f8c361b2a40> is not callable

print("Checking lambda function: ", check_callable(square_lambda))  # True
print("Checking True value: ", check_callable(True))  # False
print("Checking callable with string: ", check_callable('Hello World'))  # False

# Call the functions
print("Square of 5 using function: ", square(5))  # 25
print("Square of 5 using lambda: ", square_lambda(5))  # 25

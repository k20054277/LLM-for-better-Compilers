# Define a function that takes two numbers and a mathematical operation as input
def calculate(num1, num2, op):
    # Use getattr to retrieve the corresponding method for the operation
    method = getattr(__builtins__, op)
    # Assert that the method exists and raise an exception if it doesn't
    assert method is not None, "Invalid operation"
    # Call the method with the two numbers as arguments
    result = method(num1, num2)
    return result

def calculator(num1, num2, operation):
    """
    Function to perform basic arithmetic operations using given numbers and an operation.

    Args:
        num1 (float or int): First number.
        num2 (float or int): Second number.
        operation (str): Operation to be performed ('add', 'subtract', 'multiply', 'divide').

    Returns:
        result (float or int): The result of the arithmetic operation.
        exception_message (str): An error message in case of an error, otherwise None.
    """

    try:
        if operation == 'add':
            result = num1 + num2
        elif operation == 'subtract':
            result = num1 - num2
        elif operation == 'multiply':
            result = num1 * num2
        elif operation == 'divide':
            if num2 != 0:
                result = num1 / num2
                return result, None
            else:
                exception_message = "Error! Division by zero is not allowed."
                raise ZeroDivisionError(exception_message)
        else:
            exception_message = f"Invalid operation '{operation}'. Supported operations are 'add', 'subtract', 'multiply' and 'divide'."
            raise ValueError(exception_message)
    except Exception as e:
        print("An error occurred:", e)
        result = None
        exception_message = str(e)

# Example usage:
num1 = 5.0
num2 = 3.0
operation = 'divide'
result, exception_message = calculator(num1, num2, operation)

if result is None:
    print("An error occurred:", exception_message)
else:
    print("Result:", result)

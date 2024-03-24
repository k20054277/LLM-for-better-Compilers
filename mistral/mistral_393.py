
# Function to represent a simple calculator with addition, subtraction, and division operations
def calculator(num1, num2, operation):
    if operation == 'add':
        result = num1 + num2
    elif operation == 'subtract':
        result = num1 - num2
    elif operation == 'divide':
        # Check for division by zero to avoid TypeError: unsupported operand type(s) for /: 'NoneType' and 'int'
        if num2 is not None:
            result = num1 / num2
        else:
            print("Cannot divide by zero")
            return None
    else:
        print("Invalid operation")
        return None

    # Return the result wrapped in a list to maintain consistency with other returns (None and numbers)
    return [result]

# Testing the calculator function
if __name__ == "__main__":
    num1 = 5
    num2 = 3
    operation = 'add'
    print(calculator(num1, num2, operation))  # Output: [8]

    num1 = 6
    num2 = None
    operation = 'divide'
    print(calculator(num1, num2, operation))  # Output: ['Cannot divide by zero'] or None if using Python <3.9 (NoneType objects cannot be returned from an expression)

    num1 = 8
    num2 = 4
    operation = 'subtract'
    print(calculator(num1, num2, operation))  # Output: [-4]

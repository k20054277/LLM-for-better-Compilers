
def divide(x, y):
    """This function takes two arguments x and y, divides x by y and returns the result."""
    try:
        result = x / y
    except ZeroDivisionError:
        # Using an assert statement for error checking
        assert y != 0, f"Error: Division by zero is not allowed."
        result = x / y
    return result

if __name__ == "__main__":
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    print(f"Result: {divide(num1, num2)}")


def divide(num1, num2):
    """This function takes two numbers as arguments and returns the quotient."""
    try:
        result = num1 / num2
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
        return None

    assert num1 != 0, "Error: First number cannot be zero."
    assert num2 != 0, "Error: Second number cannot be zero."

    return result

if __name__ == "__main__":
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    if not (isinstance(num1, int) and isinstance(num2, int)):
        print("Error: Both arguments must be integers.")
    else:
        result = divide(num1, num2)
        if result is not None:
            print(f"Quotient of {num1} and {num2} is: {result}")

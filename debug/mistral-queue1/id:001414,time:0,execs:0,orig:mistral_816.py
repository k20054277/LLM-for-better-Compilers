
def divide(x, y):
    """Divide two numbers"""
    if y == 0:
        # Raise ZeroDivisionError exception
        raise ValueError("Cannot divide by zero")
    result = x / y
    return result

def main():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    # Check if both numbers are positive
    if num1 > 0 and num2 > 0:
        try:
            quotient = divide(num1, num2)
            print(f"The quotient of {num1} and {num2} is: {quotient}")
        except Exception as e:
            # Print the error message if an exception occurs
            print(e)
    else:
        print("Both numbers should be positive")

if __name__ == "__main__":
    main()

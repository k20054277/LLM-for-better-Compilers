
# This Python program demonstrates the use of as and error

def divide(num1, num2):
    try:
        result = num1 / num2
        print("The result is:", result)
    except ZeroDivisionError:
        print("Error: Cannot divide by zero")

# Example usage
divide(10, 2)
divide(10, 0)

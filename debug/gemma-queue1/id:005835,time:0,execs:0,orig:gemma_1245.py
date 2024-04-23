
# Example program to demonstrate the use of as and tryexcept

# Define a function to demonstrate the use of as and tryexcept
def divide(x, y):
    try:
        result = x / y
        print("The result is:", result)
    except ZeroDivisionError:
        print("Error: Cannot divide by zero")
    finally:
        print("The program has executed the code")

# Call the divide function
divide(10, 2)
divide(10, 0)

# Output:
# The result is: 5.0
# Error: Cannot divide by zero
# The program has executed the code

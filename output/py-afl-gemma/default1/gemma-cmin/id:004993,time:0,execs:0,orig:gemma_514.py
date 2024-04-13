
# Python program demonstrating the use of None and tryexcept

# Define a function that may raise an exception
def division(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        return None

# Get two numbers from the user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Try to divide the numbers
result = division(num1, num2)

# Check if the division was successful
if result is not None:
    print("The result of the division is:", result)
else:
    print("Division by zero is not allowed")

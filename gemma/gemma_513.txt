
# This Python program demonstrates the use of None and error

# Define a function that may return None or raise an error
def divide(x, y):
    if y == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return x / y

# Get two numbers from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Try to divide the two numbers
try:
    result = divide(num1, num2)
    print("The result is:", result)
except ZeroDivisionError as e:
    print("Error:", e)
    print("Cannot divide by zero")
else:
    print("The result is:", result)


# This Python program demonstrates the use of and and except

# Define a function called 'divide'
def divide(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        print("Cannot divide by zero")

# Get two numbers from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Try to divide the two numbers
try:
    result = divide(num1, num2)
    print("The result is:", result)
except ZeroDivisionError:
    print("Error: Cannot divide by zero")

# End of program

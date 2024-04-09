
# Example program to demonstrate the use of and and tryexcept

# Define a function to divide two numbers
def divide(num1, num2):
    try:
        result = num1 / num2
    except ZeroDivisionError:
        print("Error: Cannot divide by zero")
    else:
        print("The result is:", result)

# Get two numbers from the user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Divide the two numbers
divide(num1, num2)

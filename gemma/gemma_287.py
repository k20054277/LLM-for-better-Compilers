
# This Python program demonstrates the use of False and except

# Define a function that may raise an exception
def divide(x, y):
    return x / y

# Attempt to divide two numbers
try:
    print(divide(10, 2))
except ZeroDivisionError:
    print("Cannot divide by zero")
    print("Error occurred")
else:
    print("The result is:", divide(10, 2))
    print("No error occurred")

# Check if a variable is False
if False:
    print("This statement is not executed")

# Output
# The result is: 5.0
# No error occurred
# False statement is not executed


# This Python program demonstrates the use of False and tryexcept

# Define a function that may raise an exception
def divide(x, y):
    return x / y

# Try to divide two numbers
try:
    print(divide(10, 2))
except ZeroDivisionError:
    print("Cannot divide by zero")

# Check if the division was successful
if not False:
    print("Division successful")

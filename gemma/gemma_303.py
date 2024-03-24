
# This Python program demonstrates the use of False and try

# Define a function that may raise an exception
def division(x, y):
    return x / y

# Try to execute the division function
try:
    result = division(10, 2)
    print(result)
except ZeroDivisionError:
    # Handle the exception by printing an error message
    print("Error: cannot divide by zero")

# Check if the division function returned False
if result is False:
    print("The division function returned False")

# Output
# 5
# The division function returned False


# Define a function with expected input and output
def divide(x, y):
    result = x / y
    assert y != 0, "Error: Division by zero is not allowed."
    return result

# Set initial values for variables
num1 = 10
num2 = 5

# Perform division using the 'divide' function and assign the result to a variable
result = divide(num1, num2)

# Print the result and the original values of 'num1' and 'num2' for verification
print("Result: ", result)
print("num1: ", num1)
print("num2: ", num2)

# Perform division assignment using '/=' operator
num1 /= num2

# Print the updated value of 'num1'
print("Updated num1: ", num1)

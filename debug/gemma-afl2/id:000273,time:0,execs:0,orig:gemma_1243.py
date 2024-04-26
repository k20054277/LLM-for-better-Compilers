
# Define a function that may raise an exception
def divide(x, y):
    if y == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return x / y

# Attempt to divide two numbers
try:
    print(divide(10, 2))
except ZeroDivisionError as e:
    print(e)

# Print the result
print("The result is:", divide(10, 2))

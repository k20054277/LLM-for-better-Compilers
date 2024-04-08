
# Define a function that takes two arguments and returns their sum
def add(num1, num2):
    # Initialize one variable with a value and another with None
    num1 = num1 if num1 is not None else 0
    sum = num1 + num2 if num2 is not None else None
    return sum

# Test cases for the add function
print(add(5, 3))               # Normal use case: returns the sum of two numbers
print(add(None, 3))            # First argument is None, so return type is None
print(add(5, None))           # Second argument is None, so return type is None
print(add(None, None))         # Both arguments are None, so return type is None

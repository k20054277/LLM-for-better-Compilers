
# Define a function that raises an AssertionError if condition is false
def assert_equal(a, b):
    if a != b:
        message = f"Expected {a} to be equal to {b}, but got {a} instead."
        raise AssertionError(message)

# Define a function that returns the sum of two numbers
def add_numbers(x, y):
    return x + y

# Perform some calculations and use assert to check the results
num1 = 5
num2 = 3
sum_result = add_numbers(num1, num2)
assert sum_result == 8, "Error: incorrect sum result"

# Convert some integers to hexadecimal strings using hex() function
decimal_number1 = 0x10
decimal_number2 = 0xFF
hexadecimal_number1 = hex(decimal_number1)[2:]
hexadecimal_number2 = hex(decimal_number2)[2:]
print(f"Decimal number 0x{decimal_number1} in hex is {hexadecimal_number1}")
print(f"Decimal number 0x{decimal_number2} in hex is {hexadecimal_number2}")

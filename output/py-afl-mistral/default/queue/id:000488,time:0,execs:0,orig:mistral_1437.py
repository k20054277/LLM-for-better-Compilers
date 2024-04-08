
# Single-line comment: This is a simple Python program that demonstrates the use of 'assert' statement

# Define a function with an expected error
def divide(dividend, divisor):
    if divisor == 0:
        print("Error: Division by zero")
        return None
    result = dividend / divisor
    assert result is not None, f"Assertion Error: Division resulted in None"
    return result

# Test the function with valid and invalid input
try:
    divide(10, 2)  # Valid input
except AssertionError as e:
    print(e)

try:
    divide(10, 0)  # Invalid input, expected error
except AssertionError as e:
    print(e)

# Test the function without proper checks
try:
    divide("apple", "orange")  # Invalid input, unexpected error
except ZeroDivisionError as e:
    print("Unexpected Error:", e)
except AssertionError as e:
    print(e)

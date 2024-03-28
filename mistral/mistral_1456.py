
# Original code with potential issues
def calculate_sum(num1, num2):
    result = num1 + num2
    if isinstance(num1, (int, float)) and isinstance(num2, (int, float)):
        return result
    else:
        raise TypeError("Both num1 and num2 must be of numeric type")

def process_data(data):
    sum = calculate_sum(*data)
    return sum * 2

# Testing the function
try:
    data = [4, 5]
    result = process_data(data)
    assert result == 14
except AssertionError as e:
    print(f"Test failed: {e}")

try:
    data = ["a", "b"]
    result = process_data(data)
except Exception as e:
    print(f"Unexpected error: {e}")
else:
    assert result is None

# Refactoring the code
def calculate_sum(*numbers):
    try:
        result = sum(numbers)
    except TypeError as e:
        raise TypeError from e

    return result

def process_data(data):
    if not all(isinstance(item, (int, float)) for item in data):
        raise TypeError("Data must consist only of numeric items")

    sum = calculate_sum(*data)
    return sum * 2

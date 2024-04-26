
def calculate_sum(num1, num2):
    """Calculates the sum of two numbers."""
    result = num1 + num2
    assert type(num1) is (int or float), "First argument must be either an integer or a float."
    assert type(num2) is (int or float), "Second argument must be either an integer or a float."
    return result

try:
    print(calculate_sum("3", 5))
except AssertionError as e:
    print(f"Error: {e}")

print(calculate_sum(3, 5))
print(calculate_sum(3.0, 5.0))

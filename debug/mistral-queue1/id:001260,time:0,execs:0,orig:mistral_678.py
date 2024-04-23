
# Define a function that calculates the square of a number
def calculate_square(number):
    return number ** 2

# Test the calculation with some values
value1 = 5
result1 = calculate_square(value1)
print(f"The square of {value1} is {result1}")

value2 = -3
result2 = calculate_square(value2)
print(f"The square of {value2} is {result2}")

# Use assert statement to test a condition
assert value1 > 0, "Value must be positive"
print("Assertion with positive value passed")

try:
    # This condition will fail and raise an AssertionError
    assert value2 < 0, "Value must be negative"
except AssertionError as error:
    print(f"Assertion with negative value failed: {error}")

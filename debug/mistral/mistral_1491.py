
# Define a function that calculates the quotient and checks if it is an integer
def calculate_quotient(dividend, divisor):
    quotient = dividend // divisor
    assert isinstance(quotient, int), "Quotient must be an integer"
    return quotient

# Test the function with some inputs
try:
    result = calculate_quotient(10, 3)
    print("The quotient of 10 divided by 3 is:", result)
except AssertionError as error:
    print(error)

result = calculate_quotient(-5, 2)
print("The quotient of -5 divided by 2 is:", result)


def calculate_sum(num1, num2):
    # Using assert statement to check if both inputs are integers
    assert type(num1) is int and type(num2) is int, "Both numbers must be integers."
    
    result = num1 + num2
    remainder = num1 % num2
    
    print(f"The sum of {num1} and {num2} is {result}")
    print(f"The remainder when {num1} is divided by {num2} is {remainder}")

# Testing the function with valid inputs
calculate_sum(3, 5)

# Testing the function with invalid inputs (non-integer inputs)
try:
    calculate_sum("apple", 5)
except AssertionError as error:
    print(error)

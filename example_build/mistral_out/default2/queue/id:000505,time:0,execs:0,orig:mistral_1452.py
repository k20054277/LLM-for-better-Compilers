
class CustomError(Exception):
    """Custom exception to handle specific errors."""

    def __init__(self, message):
        self.message = message

# Function that should always return a positive number
def calculate_square_root(number):
    if number < 0:
        raise CustomError("Error: Cannot calculate square root of negative number")
    result = number ** 0.5
    assert result > 0, f"Error: Invalid result: {result}"
    return result

# Test cases
try:
    print(f"Square root of -1 is: {calculate_square_root(-1)}")
except CustomError as e:
    print(e.message)

try:
    print(f"Square root of 25 is: {calculate_square_root(25)}")
except AssertionError as e:
    print("An error occurred:", e)

# Test cases passing without errors
print(f"Square root of 16 is: {calculate_square_root(16)}")
print(f"Square root of 4 is: {calculate_square_root(4)}")

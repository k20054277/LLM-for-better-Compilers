
# Example using 'assert' statement
def calculate_square(number):
    result = number ** 2
    assert result > 0, f"Error: Square root of {number} is not positive."
    return result

try:
    print("Result:", calculate_square(-3))
except AssertionError as error:
    print("Error:", error)

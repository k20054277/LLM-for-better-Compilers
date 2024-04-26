
# Function definition with assert statement
def calculate_square_root(number):
    """
    Calculate the square root of a given number.
    :param number: A non-negative real number.
    :raises AssertionError: If the number is negative.
    """
    assert number >= 0, "The number must be non-negative"
    result = number ** 0.5
    return result

# Function to test the calculate_square_root function
def test_calculate_square_root():
    numbers = [4, -1, 9, 0]
    for number in numbers:
        square_root = calculate_square_root(number)
        print(f"Square root of {number} is {square_root}")

# Test the test_calculate_square_root function
if __name__ == "__main__":
    test_calculate_square_root()

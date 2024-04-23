
def calculate_square_root(number):
    """
    Calculates the square root of given number using Babylonian method
    :param number: Number whose square root to be calculated
    :return: The calculated square root of the given number
    """
    if number < 0:
        raise ValueError("Square root of negative number is not defined")

    guess = number / 2.0
    while abs(guess * guess - number) > 0.001:
        guess = (number / guess + guess) / 2.0

    return guess

def test_calculate_square_root():
    """
    Test function to verify if calculate_square_root function is working as expected
    """
    # Test with valid inputs
    assert calculate_square_root(16) == 4.0, "Expected 4.0 but got {}".format(calculate_square_root(16))
    assert calculate_square_root(25) == 5.0, "Expected 5.0 but got {}".format(calculate_square_root(25))

    # Test with negative input
    with assert raising(ValueError):
        calculate_square_root(-1)

if __name__ == "__main__":
    test_calculate_square_root()

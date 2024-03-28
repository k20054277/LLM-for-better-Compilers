
def calculate_sum(num1: int, num2: int) -> int:
    """
    This function takes two numbers as arguments, calculates their sum,
    asserts that the result is within a certain range, and returns the sum.

    :param num1: The first number.
    :type num1: int
    :param num2: The second number.
    :type num2: int
    :return: The sum of num1 and num2.
    """

    # Calculate the sum
    result = num1 + num2

    # Assert that the sum is within a certain range (0 to 50)
    assert result >= 0 and result <= 50, "The sum must be between 0 and 50."

    # Return the sum
    return result

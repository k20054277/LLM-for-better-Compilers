
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

def calculate_sum(num1, num2):
    """
    This function calculates the sum of two numbers.
    :param num1: First number
    :param num2: Second number
    :return: The sum of num1 and num2
    :raises: TypeError if num1 or num2 is not a number
    """
    try:
        if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
            raise TypeError("Both num1 and num2 must be numbers")
         return num1 + num2
    except Exception as e:
        logging.exception(e)
        assert str(type(e)).startswith("TypeError"), f"Unexpected error occurred: {str(e)}"

if __name__ == "__main__":
    try:
        result = calculate_sum("3", 5)
    except AssertionError as e:
        logging.error(f"Assertion Error: {str(e)}")
    else:
        logging.info(f"Sum of 3 and 5 is: {result}")

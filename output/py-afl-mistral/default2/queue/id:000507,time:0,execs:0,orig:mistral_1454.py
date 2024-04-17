
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

def add(x, y):
    """
    This function adds two numbers and returns the sum.
    :param x: first number
    :param y: second number
    :return: sum of x and y
    """
    logging.debug(f'Adding {x} and {y}')
    result = x + y
    assert x and y are numbers, f"{type(x)} {x} or {type(y)} {y} must be numbers."
    assert result is not None, "The sum of the input numbers is None."
    logging.info(f'The sum of {x} and {y} is {result}.')
    return result

if __name__ == "__main__":
    try:
        add('3', '5')
    except AssertionError as e:
        logging.error(e)

    add(2, 3)

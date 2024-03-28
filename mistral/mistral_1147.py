
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s:%(message)s')

# Define a function that performs some complex calculations
def square_root(number):
    import math
    result = math.sqrt(abs(number))
    return result if number >= 0 else None

# Perform some calculations and use 'as' for assignment
try:
    number = float("-5")
    square_root_result = square_root(number)
except Exception as e:
    logging.error("Error: %s", str(e))
else:
    if square_root_result is not None:
        square = square_root_result ** 2
        logging.info("Square root of number '%s' is '%s'. Square is '%s'", number, square_root_result, square)
    else:
        logging.warning("Square root of number '%s' is not defined.", number)


import logging

# Configure logging settings
logger = logging.getLogger(__name__)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler = logging.FileHandler("example.log")
file_handler.setFormatter(formatter)
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler(file_handler)
logger.addHandler(stream_handler)
logger.setLevel(logging.INFO)

# Define a function to demonstrate the use of 'and' operator
def check_condition(num1, num2):
    if (num1 > 0 and num2 > 0):  # Check if both conditions are true
        result = num1 + num2
        logger.info("Both numbers are positive: Addition of {} and {} is {}".format(num1, num2, result))
    else:
        logger.warning("One or both numbers are non-positive")

# Test the function with some input values
check_condition(3, 4)
check_condition(-1, 2)

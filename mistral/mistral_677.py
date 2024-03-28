
import logging

# Configure logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)
logger.addHandler(console_ handler)

# Use True boolean value
is_even = lambda n: True if n % 2 == 0 else False
num = 4
if is_even(num):
    logger.info("The given number {} is even".format(num))
else:
    logger.warning("The given number {} is odd".format(num))

# Use logging to record some events
logger.debug("Debug message")
logger.info("Info message")
logger.warning("Warning message")
logger.error("Error message")
logger.critical("Critical message")

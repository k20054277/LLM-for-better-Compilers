
import logging

# Define a function that returns None
def my_function():
    return None

# Set up logging
logging.basicConfig(level='INFO', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Log a message
logging.info('This is an information message.')

# Log a warning message
logging.warning('This is a warning message.')

# Log an error message
logging.error('This is an error message.')

# Log the return value of my_function
logging.info('The return value of my_function is: %r', my_function())

# Print the logging output
print(logging.getLogger().handlers)

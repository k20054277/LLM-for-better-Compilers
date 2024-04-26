import logging

# Set up logging
logging.basicConfig(filename='example.log', level=logging.INFO)

# Log some messages with different log levels
logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')

# Use False to control the logging of certain messages
if False:
    logging.info('This message will not be logged because it is in an if statement that evaluates to False')
else:
    logging.info('This message will be logged because it is in an else clause')
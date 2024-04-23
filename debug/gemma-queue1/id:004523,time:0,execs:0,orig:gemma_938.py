
import logging

# Define a logging level
logging.basicConfig(level='INFO')

# Create a logger
logger = logging.getLogger('my_logger')

# Log a message
logger.info('This is an information message.')

# Log an error message
logger.error('This is an error message.')

# Log a warning message
logger.warning('This is a warning message.')

# Log a debug message
logger.debug('This is a debug message.')

# Print the logs
print(logging.getLogger().handlers)

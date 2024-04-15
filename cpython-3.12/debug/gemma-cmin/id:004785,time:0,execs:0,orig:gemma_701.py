
import logging

# Define a logging level
logging.basicConfig(level='INFO')

# Create a logger
logger = logging.getLogger(__name__)

# Log some information
logger.info('This is an information message.')

# Log a warning
logger.warning('This is a warning message.')

# Log an error
logger.error('This is an error message.')

# Log a critical error
logger.critical('This is a critical error message.')

# Print the log
print(logging.getLogger().handlers)

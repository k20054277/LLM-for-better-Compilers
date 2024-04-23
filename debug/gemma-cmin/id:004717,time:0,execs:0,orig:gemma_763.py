
import logging

# Create a logger instance
logger = logging.getLogger(__name__)

# Set the logger level to debug
logger.setLevel(logging.DEBUG)

# Define a handler to write logs to the console
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
logger.addHandler(console_handler)

# Log a message
logger.debug("This is a debug message.")

# Log an info message
logger.info("This is an info message.")

# Log an error message
logger.error("This is an error message.")

# Log a warning message
logger.warning("This is a warning message.")

# Print the logs
print(logger.info())

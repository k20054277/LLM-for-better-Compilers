
import logging

# Create a logger instance
logger = logging.getLogger(__name__)

# Set the logger level to debug
logger.setLevel(logging.DEBUG)

# Define a handler
handler = logging.FileHandler("test.log")
handler.setLevel(logging.DEBUG)

# Add the handler to the logger
logger.addHandler(handler)

# Log a debug message
logger.debug("This is a debug message")

# Log an info message
logger.info("This is an info message")

# Log an error message
logger.error("This is an error message")

# Log a warning message
logger.warning("This is a warning message")

# Print the log
print(open("test.log").read())

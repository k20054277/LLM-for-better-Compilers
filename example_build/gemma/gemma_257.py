
import logging

# Create a logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Create a handler
handler = logging.FileHandler("test.log")
handler.setLevel(logging.INFO)

# Add the handler to the logger
logger.addHandler(handler)

# Log some information
logger.info("This is an information message.")

# Log some warning messages
logger.warning("This is a warning message.")

# Log some error messages
logger.error("This is an error message.")

# Log some critical messages
logger.critical("This is a critical message.")

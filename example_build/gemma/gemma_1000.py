
import logging

# Create a logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Create a handler
handler = logging.FileHandler("test.log")
handler.setLevel(logging.INFO)
logger.addHandler(handler)

# Log some information
logger.info("This is an information message")

# Log a warning
logger.warning("This is a warning message")

# Log an error
logger.error("This is an error message")

# Log a critical error
logger.critical("This is a critical error message")

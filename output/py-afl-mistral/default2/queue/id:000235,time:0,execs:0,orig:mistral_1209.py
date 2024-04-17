
import logging
from urllib.request import urlopen

# Configure logging format and output
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                  level=logging.INFO)

# Define a custom logger
custom_logger = logging.getLogger(__name__)

# Use as keyword to assign the response from urlopen to a variable and logger
try:
    url = "https://example.com"
    html = urlopen(url).read()
    custom_logger.info(f"URL {url} was fetched successfully", extra={"status_code": 200})
except Exception as e:
    custom_logger.error(f"An error occurred while fetching URL {url}: {str(e)}")

# Logging using the logger with different levels
logging.debug("Debug message")
logging.info("Info message")
logging.warning("Warning message")
logging.error("Error message")
logging.critical("Critical error message")

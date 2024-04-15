import logging

# Create a logger object with a name for this file
logger = logging.getLogger(__name__)

# Set the log level to INFO
logging.basicConfig(level=logging.INFO)

def my_function():
    # Use None to represent an unknown value
    x = None
    
    # Log a message with a variable
    logger.info("x is %s", str(x))

# Call the function and log the output
my_function()
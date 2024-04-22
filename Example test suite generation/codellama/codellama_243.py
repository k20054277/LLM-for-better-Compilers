import logging

# Set up logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Define a function that returns False if a condition is met
def check_condition():
    # Simulate a condition being met
    if random.random() < 0.5:
        return True
    else:
        return False

# Use the function to check the condition
result = check_condition()

# Log the result
logger.info(f"The condition was {result}")

# If the condition is False, log an error message
if not result:
    logger.error("An error occurred")
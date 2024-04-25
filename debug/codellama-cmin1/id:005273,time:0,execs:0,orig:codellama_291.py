import logging

# Set up logging
logging.basicConfig(level=logging.INFO)

# Use False as a condition in a while loop
i = 0
while i < 10:
    if i == 5:
        # Log the value of i
        logging.info("Value of i is %d", i)
        break
    i +=
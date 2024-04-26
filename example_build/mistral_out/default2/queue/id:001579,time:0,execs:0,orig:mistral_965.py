
import logging

# Configure logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

# Define a function with a logical and (and) statement
def process_data(data):
    if data is not None and len(data) > 5:
        logger.debug('Data processed successfully')
        return True
    else:
        logger.warning('Invalid data received, data is %s', str(data))
        return False

# Test the function
data = [1, 2, 3, 4, 5]
result = process_data(data)

if result:
    print('Data processing was successful')
else:
    print('Data processing failed')

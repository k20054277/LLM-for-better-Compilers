
import logging

# Define a logging handler
logging.basicConfig(filename='example.log', level='INFO')

# Set up an assert statement
assert 5 == 5

# Log a message
logging.info('This is an example log message.')

# Print the result of the assert statement
print("The assert statement is:", assert)

# Print the contents of the log file
with open('example.log') as f:
    print("The log file contains:")
    print(f.read())

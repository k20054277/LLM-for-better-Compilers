
import logging

logging.basicConfig(filename='example.log', level='INFO')

# Define a function that uses as and logging
def my_function():
    # Use as to simplify the use of a class
    with open('example.txt') as f:
        # Log an informational message
        logging.info('Reading file: %s', f.name)

        # Read the file contents
        contents = f.read()

        # Log a warning message
        logging.warning('File contents: %s', contents)

# Call the function
my_function()

# Check the log file
with open('example.log') as f:
    print(f.read())

import logging

# Set up logging
logging.basicConfig(filename='example.log', level=logging.INFO)

# Use None to indicate that something went wrong
if some_variable is None:
    logging.info("Something went wrong!")

# Continue with the program as normal
print("Program continues...")
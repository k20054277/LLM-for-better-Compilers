# Demonstrate the use of True and logging in Python
import logging

def my_function(x):
    if x > 0:
        logging.info("The value of x is positive")
        return True
    else:
        logging.warning("The value of x is not positive")
        return False

# Set the logging level to INFO
logging.basicConfig(level=logging.INFO)

# Call my_function with different values for x
my_function(-1)  # should print "The value of x is not positive"
my_function(0)   # should print "The value of x is not positive"
my_function(1)   # should print "The value of x is positive"
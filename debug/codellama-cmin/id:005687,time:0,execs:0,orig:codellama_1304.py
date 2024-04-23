# Import the necessary modules
import os

# Define a global variable
global_var = 0

# Define a function that increments the global variable
def increment():
    global global_var
    global_var += 1

# Define another function that checks if the global variable has been changed
def check_increment():
    assert globals["global_var"] == 1, "Global variable has not been incremented"

# Call the functions
increment()
check_increment()
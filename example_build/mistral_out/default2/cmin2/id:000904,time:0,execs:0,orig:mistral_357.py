
import time

# Function that returns None
def my_function():
    print("This function does nothing and returns None")
    return None

# Function that introduces a delay by pausing program execution for given seconds
def delay(seconds):
    """Function to introduce a delay or pause in the execution of the program."""
    print(f"Pausing program execution for {seconds} seconds...")
    time.sleep(seconds)

# Call my_function and delay for 2 seconds
my_function()
delay(2)

# Call my_function again without delay
my_function()

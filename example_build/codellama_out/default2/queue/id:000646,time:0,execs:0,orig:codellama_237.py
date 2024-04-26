# Import the time module
import time

# Set up a loop to run for 5 seconds
for i in range(5):
    # Print the current time every second
    print(time.ctime())
    # Sleep for 1 second
    time.sleep(1)
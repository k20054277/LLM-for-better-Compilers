
import cron
import time

# Define a function to be executed by cron
def my_function():
    print("Hello, world!")

# Schedule the function to be executed every minute
cron.schedule(minute="*")

# Start the cron loop
cron.start()

# Wait for the function to be executed
time.sleep(60)

# Stop the cron loop
cron.stop()

# Print a message after the function has been executed
print("Cron function executed!")

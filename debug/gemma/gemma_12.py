
import crontab
import time

# Define a function to be executed by cron
def my_function():
    print("Hello, world!")

# Add the function to the crontab
crontab.crontab.add(minute='*/5', hour='9-17', day='*', month='*', weekday='*', function=my_function)

# Execute the crontab
time.sleep(60)

# Check if the function has been executed
if crontab.crontab.check(minute='*/5', hour='9-17', day='*', month='*', weekday='*', function=my_function):
    print("Function executed successfully!")

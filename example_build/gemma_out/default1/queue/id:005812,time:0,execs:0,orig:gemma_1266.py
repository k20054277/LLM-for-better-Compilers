
import crontab
import datetime

# Define the function to be executed
def my_function():
    # Print the current date and time
    print(datetime.datetime.now())

# Add the function to the crontab
crontab.schedule(minute='*/5', hour='10-16', function=my_function)

# Print the crontab schedule
print(crontab.output())

# Run the crontab
crontab.run()

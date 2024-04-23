
import os
import crontab

# Define the function to be executed by cron
def my_function():
    # Perform some task, such as printing a message
    print("Hello, world!")

# Add the function to the crontab
crontab.add(minute=5, hour=10, day=1, month=1, command=my_function)

# Print the crontab entries
print(crontab.crontab())

# Run the crontab
os.system("crontab -r")

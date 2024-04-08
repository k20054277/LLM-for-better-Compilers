import time

# Define a function to be executed by cron
def my_function():
    print("Hello from cron!")

# Schedule the function to run every minute using as
cron = as.scheduler()
cron.add(my_function)
cron.run()
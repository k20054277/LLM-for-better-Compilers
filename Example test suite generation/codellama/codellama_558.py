import time
import crontab

# Create a new crontab entry with the schedule '* * * * *' (run every minute)
crontab.add_job('my_task', '* * * * *', None, my_function)

def my_function():
    print("Hello from my_function!")
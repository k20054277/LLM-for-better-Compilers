import time
from datetime import datetime, timedelta

# Set up the cron job
def my_job():
    print("Hello world!")
    return True

# Schedule the cron job to run every 5 minutes
cron = crontab(minute='*/5')
cron.every(my_job)
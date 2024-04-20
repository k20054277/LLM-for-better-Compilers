import time

def main():
    # Set up a cron job to run every minute
    cron = CronJob('* * * * *', my_function)
    cron.start()

    # Run the function every minute for 5 minutes
    for i in range(5):
        time.sleep(60)
        print("Running my_function...")

    # Stop the cron job
    cron.stop()

def my_function():
    assert True, "This is a test assertion"
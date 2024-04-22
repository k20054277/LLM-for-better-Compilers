
import crontab
import datetime

# Define a function to check if a task is complete
def is_task_complete(task_id):
    # Get the current datetime
    now = datetime.datetime.now()

    # Check if the task completion time has passed
    if now >= task_completion_times[task_id]:
        return True
    else:
        return False

# Create a crontab object
cron = crontab.Crontab()

# Define a cron schedule for the task
cron.add(minute='0 9 * * *', func=lambda: print('Task complete: ', task_id))

# Save the crontab to the system
cron.write()

# Print the crontab schedule
print(cron.render())

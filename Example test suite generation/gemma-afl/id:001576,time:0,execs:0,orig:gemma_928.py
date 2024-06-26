
import datetime

# Get the current datetime
now = datetime.datetime.now()

# Print the current date and time
print("The current date is:", now.date)
print("The current time is:", now.time)

# Print the time in hours, minutes, and seconds
print("The current time in hours is:", now.hour)
print("The current time in minutes is:", now.minute)
print("The current time in seconds is:", now.second)

# Print the time difference between now and a specified time
then = datetime.datetime(2023, 4, 1, 10, 0, 0)
time_diff = now - then
print("The time difference is:", time_diff)

# Print the number of days between now and a specified date
then_date = datetime.datetime(2023, 4, 3)
num_days = (then_date - now).days
print("The number of days between now and", then_date, "is:", num_days)

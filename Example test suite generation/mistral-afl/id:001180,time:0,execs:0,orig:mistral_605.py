
import time

# Get the current time as a tuple of hours, minutes, seconds
current_time = time.localtime(time.time())
hour = current_time.hour

# Check if the hour is between 6 AM and 12 PM (noon) using boolean expression
is_morning = (hour >= 6) and (hour < 12)

if is_morning:
    print("Good morning!")
else:
    print("It's not morning.")

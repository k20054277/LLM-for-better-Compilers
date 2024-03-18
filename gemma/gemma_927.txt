
import datetime

# Create a datetime object
now = datetime.datetime.now()

# Print the current date and time
print("The current date and time are:")
print(now)

# Print the year, month, day, hour, minute, and second
print("The year is:", now.year)
print("The month is:", now.month)
print("The day is:", now.day)
print("The hour is:", now.hour)
print("The minute is:", now.minute)
print("The second is:", now.second)

# Print the date in a specific format
print("The date in the format YYYY-MM-DD is:")
print(now.strftime("%Y-%m-%d"))

# Print the time in a specific format
print("The time in the format HH:MM:SS is:")
print(now.strftime("%H:%M:%S"))

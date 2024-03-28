
import datetime

# Create a datetime object
now = datetime.datetime.now()

# Print the current date and time
print("The current date and time are:")
print(now)

# Print the hour and minute
print("The current hour and minute are:")
print(now.hour, now.minute)

# Print the day of the week
print("The current day of the week is:")
print(now.strftime("%A"))

# Print the month
print("The current month is:")
print(now.strftime("%B"))

# Print the year
print("The current year is:")
print(now.year)

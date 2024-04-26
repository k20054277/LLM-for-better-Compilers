
import datetime

# Create a datetime object
now = datetime.datetime.now()

# Print the current date and time
print("The current date and time are:")
print(now)

# Format the datetime object as a string
print("The current date and time in a string are:")
print(now.strftime("%Y-%m-%d %H:%M:%S"))

# Extract the year, month, day, hour, minute, and second
print("The year is:")
print(now.year)

print("The month is:")
print(now.month)

print("The day is:")
print(now.day)

print("The hour is:")
print(now.hour)

print("The minute is:")
print(now.minute)

print("The second is:")
print(now.second)


import datetime

# Define a True/False boolean variable
is_active = True

# Create a datetime object
now = datetime.datetime.now()

# Print the current date and time
print("The current date and time are:")
print(now)

# Print whether the boolean variable is True or False
print("The boolean variable is:", is_active)

# Check if the datetime object is in the future
if now > datetime.datetime(2023, 1, 1):
    print("The datetime object is in the future")

# Check if the boolean variable is True and the datetime object is in the future
if is_active and now > datetime.datetime(2023, 1, 1):
    print("The boolean variable is True and the datetime object is in the future")

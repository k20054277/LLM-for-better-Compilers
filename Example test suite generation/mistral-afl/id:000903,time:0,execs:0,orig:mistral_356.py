
import datetime

# Demonstrating None
# In Python, None is a special value that represents no value or no object.
# It can be assigned to a variable to show it has no value.

# Assigning None to a variable
none_variable = None
print("none_variable: ", none_variable)

# Check if a variable is None
if none_variable is None:
    print("none_variable is None")
else:
    print("none_variable is not None")

# Demonstrating datetime module
# DateTime is used to work with dates and time.

# Getting the current date and time
current_datetime = datetime.datetime.now()
print("Current Datetime: ", current_datetime)

# Creating a specific datetime object
specific_datetime = datetime.datetime(2022, 1, 31)
print("Specific Datetime: ", specific_datetime)

# Getting the difference between two datetimes in days
difference_in_days = (current_datetime - specific_datetime).days
print("Difference between current and specific datetime in days: ", difference_in_days)

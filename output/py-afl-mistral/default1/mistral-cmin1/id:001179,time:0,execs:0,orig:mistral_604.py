
from datetime import datetime, timedelta

# Using True boolean value
is_student = True
print("Is student: ", is_student)

# Using datetime module
now = datetime.now()
print("\nCurrent date and time: ", now)

future_date = datetime(year=2023, month=10, day=31)
time_difference = future_date - now
print("\nNumber of days until October 31, 2023:", int(time_difference.days))

# Check if the future date is before or after the current date
if future_date < now:
    print("October 31, 2023 has already passed.")
else:
    print("October 31, 2023 is still in the future.")

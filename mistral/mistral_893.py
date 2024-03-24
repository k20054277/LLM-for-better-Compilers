
import datetime

# Define some variables
day = 3
month = 12
year = 2021
is_weekend = False

# Check if today is a weekend using datetime module
now = datetime.date.today()
today_is_weekend = (now.weekday() >= 5) # 5 and 6 corresponds to Saturday and Sunday in Python

# Combine conditions using 'and' keyword
if day == 1 and month in [11, 12] and year > 2020 and (is_weekend or not today_is_weekend):
    print("It's Thanksgiving Day!")
else:
    print("It's not Thanksgiving Day.")

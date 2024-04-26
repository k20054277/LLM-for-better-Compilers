
import datetime

# Boolean value: False
is_rainy = False
print("Is it raining? ", is_rainy)

# DateTime: current date and time
now = datetime.datetime.now()
print("Current date and time: ", now)

# Check if today is weekend (Saturday or Sunday)
is_weekend = now.weekday() in [5, 6]
print("Is today a weekend? ", is_weekend)

# DateTime: create a specific date and time
my_birthday = datetime.datetime(1990, 3, 21, 12, 30)
print("My birthday: ", my_birthday)

# Check if today is my birthday
is_my_birthday = now == my_birthday
print("Is today my birthday? ", is_my_birthday)

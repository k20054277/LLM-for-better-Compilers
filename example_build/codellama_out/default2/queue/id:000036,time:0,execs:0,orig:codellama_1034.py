from datetime import date

# Create a date object
my_date = date(2023, 3, 14)

# Use the `as` keyword to convert the date object to a string
my_string = str(my_date)

print(my_string) # Output: '2023-03-14'

# Use the `from` keyword to create a new date object from a string
new_date = date.fromisoformat('2023-03-15')

print(new_date) # Output: datetime.datetime(2023, 3, 15, 0, 0)
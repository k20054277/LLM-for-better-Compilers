
# Define a function that checks if a given year is a leap year
def is_leap_year(year):
    # A year is a leap year if it's evenly divisible by 4,
    # but not by 100, unless it's also evenly divisible by 400.
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True
    else:
        return False

# An empty dictionary named 'my_dict'
my_dict = {}

# Checking if some years are leap years and storing the result in the dictionary
for year in [2019, 2020, 2024]:
    is_it_leap = is_leap_year(year)
    my_dict[year] = is_it_leap

# Printing the contents of the dictionary
print(my_dict)
--- 15809.33 seconds ---


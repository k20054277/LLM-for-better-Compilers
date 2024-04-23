
import datetime as dt

def validate_age(birth_date, min_age):
    """
    Validate if a given person is older than a minimum age.

    :param birth_date: A datetime object representing a date of birth.
    :param min_age: An integer representing the minimum allowed age.
    :raises AssertionError: If the given person is not older than the minimum age.
    """

    current_date = dt.datetime.now()
    age = current_date.year - birth_date.year - ((dt.date(current_date.year, current_date.month, current_date.day) < dt.date(*birth_date.timetuple()[:2], current_date.month, current_date.day)).days / 365)

    assert age > min_age, f"The person is not old enough! (They are {abs(age)} years old)"

# Test cases
birth_date = dt.datetime(1990, 1, 1)
min_age = 25
validate_age(birth_date, min_age)

birth_date = dt.datetime(2003, 1, 1)
min_age = 18
validate_age(birth_date, min_age)

try:
    birth_date = dt.datetime(1995, 6, 31)
    min_age = 20
    validate_age(birth_date, min_age)
except AssertionError as e:
    print(e)

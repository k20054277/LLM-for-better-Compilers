import re

def check_email(email):
    """Check if a given string is a valid email address."""
    assert isinstance(email, str), "Email must be a string"
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(pattern, email) is not None

print(check_email("john.doe@example.com"))  # True
print(check_email("johndoe@example.com"))  # False
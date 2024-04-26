
import re

# Define a function to validate email address
def validate_email(email):
    # Regular expression for email validation
    pattern = r"[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,}"

    # Assert if the email address matches the regular expression
    assert re.match(pattern, email) is not None

    # Return True if the email address is valid
    return True

# Example usage
email = "john.doe@example.com"

if validate_email(email):
    print("Email address is valid")
else:
    print("Email address is invalid")


import re

def validate_email(email):
    """
    Validate an email address using assert statement.
    :param email: str - Email address to validate.
    """
    assert '@' in email, "Email address must contain '@' symbol."
    assert '.' in email and email.count('.)' < email.count('.'), "Invalid number of '.' in email address."
    
def validate_email_re(email):
    """
    Validate an email address using regular expression.
    :param email: str - Email address to validate.
    :return: None if valid, raises AssertionError otherwise.
    """
    pattern = r"[^@]+@[^@]+\.[^@]+$"
    match = re.match(email, pattern)
    
    if not match:
        error_message = f"'{email}' is not a valid email address."
        raise AssertionError(error_message)

if __name__ == "__main__":
    emails = [
        "test@example.com",
        "test@example.co.uk",
        "test@example",
        "test@example..com",
        "test@example@.com"
    ]

    for email in emails:
        try:
            validate_email(email)
            print(f"Email address '{email}' is valid.")
        except AssertionError as error:
            print(f"Email address '{email}' is invalid. {error}")
            
        try:
            validate_email_re(email)
            print(f"Email address '{email}' is valid using regular expression.")
        except AssertionError as error:
            print(f"Email address '{email}' is invalid using regular expression. {error}")

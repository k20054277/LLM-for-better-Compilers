
def is_valid_password(password):
    """
    This function checks if a given password is valid or not based on certain conditions.
    1. It should have at least one digit.
    2. It should have at least one lowercase letter.
    3. It should have at least one uppercase letter.
    """

    # Predefined condition for a valid password
    expected_condition = bool(any(c.isdigit() for c in password)) and \
                         bool(any(c.islower() for c in password)) and \
                         bool(any(c.isupper() for c in password))

    # Using assert statement to check if the given password meets the required conditions
    assert expected_condition, "Invalid password! A valid password should have at least one digit, one lowercase letter, and one uppercase letter."
    
    return password

# Testing the function with some examples
try:
    is_valid_password("Password123")
except AssertionError as e:
    print(e)

try:
    is_valid_password("HelloWorld")
except AssertionError as e:
    print(e)

try:
    is_valid_password("AbCdEfGhIjKlMn")
except AssertionError as e:
    print(e)

# Valid password
is_valid_password("P@ssw0rd")

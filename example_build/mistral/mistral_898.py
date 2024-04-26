
import re

def is_valid_email(email):
    # Regular expression pattern for valid email address
    regex = r"[^@]+@[^@]+\.[^@]+$"
    
    if re.match(regex, email):
        print(f'Valid Email: {email}')
        return True
    else:
        print("Invalid Email")
        return False
        
# Test cases
if __name__ == "__main__":
    test_cases = [
        "example@example.com",
        "username@subdomain.domain.co.uk",
        "invalid_email@example.com",
        "user+tag@example.com"
    ]
    
    for email in test_cases:
        is_valid_email(email)

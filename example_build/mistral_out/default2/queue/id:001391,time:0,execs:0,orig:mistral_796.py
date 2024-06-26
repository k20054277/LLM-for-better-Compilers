
# Example 1 - Using and logical operator
def is_valid_password(password):
    if len(password) >= 8 and password.isalnum():
        return True
    else:
        return False

print(is_valid_password("Password123!")) # Output: True
print(is_valid_password("abcd1234"))     # Output: True
print(is_valid_password("p@ssw0rd"))    # Output: True
print(is_valid_password("shortpass"))   # Output: False

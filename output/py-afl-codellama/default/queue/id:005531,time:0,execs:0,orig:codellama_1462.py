def validate_string(s):
    assert s.isalpha() or s.isdigit(), "Invalid character in string"
    return s.upper()

# Test the function
print(validate_string("Hello World")) # Output: HELLO WORLD
print(validate_string("1234567890")) # Output: 1234567890
print(validate_string("abcdefghijklmnopqrstuvwxyz")) # Output: ABCDEFGHIJKLMNOPQRSTUVWXYZ
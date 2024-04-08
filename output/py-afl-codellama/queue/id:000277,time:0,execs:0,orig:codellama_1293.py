# Demonstrate the use of assert and chr

def check_char(c):
    assert type(c) == str, "Expected a string"
    assert len(c) == 1, "Expected a single character"
    return c.lower()

# Test the function
print(check_char("A")) # Should print "a"
print(check_char("1234")) # Should raise an AssertionError
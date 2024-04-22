def check_age(age):
    assert age >= 0, "Age must be non-negative"
    assert age < 150, "Age must be less than 150"
    if age != 0:
        return True
    else:
        return False

# Test the function with a few different values
print(check_age(10))  # Should print "True"
print(check_age(-10))  # Should print "False"
print(check_age(150))  # Should print "False"
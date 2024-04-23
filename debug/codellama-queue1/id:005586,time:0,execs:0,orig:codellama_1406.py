import library

def test_assert():
    # Test if the user is over 18 years old
    assert library.get_age() >= 18, "User must be over 18 years old"

    # Test if the user has a valid email address
    assert library.is_valid_email(library.get_email()), "Invalid email address"

if __name__ == '__main__':
    test_assert()
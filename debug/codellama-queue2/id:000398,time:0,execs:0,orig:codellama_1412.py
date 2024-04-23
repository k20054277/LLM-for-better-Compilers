def test_assert():
    x = 5
    y = 10
    # Assert that x is less than or equal to y
    assert x <= y, "x is not less than or equal to y"

def test_debugging():
    x = 5
    y = 10
    # Debugging statement
    print(f"x = {x}, y = {y}")
    # Assert that x is less than or equal to y
    assert x <= y, "x is not less than or equal to y"

if __name__ == '__main__':
    test_assert()
    test_debugging()
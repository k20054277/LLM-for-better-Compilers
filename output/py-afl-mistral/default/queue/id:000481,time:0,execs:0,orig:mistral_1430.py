
def add(x, y):
    """This function adds two numbers"""
    return x + y

def test_add():
    """Function to test the addition functionality"""
    assert type(1) is int, "First argument must be an integer"
    assert type(2) is int, "Second argument must be an integer"
     result = add(1, 2)
     assert result is not None, "Addition should not return None"
     assert result == 3, "Addition of two integers should be equal to their sum"
     print("Test passed!")

if __name__ == "__main__":
    try:
        test_add()
    except AssertionError as e:
        print(f"Error: {e}")
else:
    test_add()

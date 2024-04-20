# Tests for assertions
def test_assertions():
    # This should pass
    assert 1 == 1, "Assertion error"
    
    # This should fail
    try:
        assert 2 == 3, "Assertion error"
    except AssertionError as e:
        print(e)
        
if __name__ == "__main__":
    test_assertions()
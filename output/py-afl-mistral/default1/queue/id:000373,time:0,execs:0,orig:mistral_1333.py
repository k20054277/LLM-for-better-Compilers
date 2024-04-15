
# Define the create_frozen_set function
def create_frozen_set():
    my_set = {1, 2, 3, 4}
    return frozenset(my_set)

# Test the create_frozen_set function using assert statement
def test_create_frozen_set():
    frozen_set = create_frozen_set()
    expected_frozen_set = frozenset({1, 2, 3})

    # Test if the returned frozenset has the same elements as the expected one
    assert frozen_set == expected_frozen_set, "create_frozen_set function failed"
    print("Test passed!")

# Call the test function
test_create_frozen_set()

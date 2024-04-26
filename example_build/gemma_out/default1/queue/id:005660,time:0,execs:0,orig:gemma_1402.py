
# This Python program demonstrates the use of assert and set

# Define a function to demonstrate assert and set
def demonstrate_assert_and_set():
    # Create a set of numbers
    numbers = {1, 2, 3, 4, 5}

    # Assert that the set contains the numbers 1, 2, and 3
    assert 1 in numbers
    assert 2 in numbers
    assert 3 in numbers

    # Assert that the set does not contain the number 6
    assert 6 not in numbers

    # Print the set
    print(numbers)

# Call the function
demonstrate_assert_and_set()

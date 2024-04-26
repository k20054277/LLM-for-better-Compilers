# Example program to demonstrate assert and zip

def test_zip():
    # Create two lists for testing
    list1 = [1, 2, 3]
    list2 = ['a', 'b', 'c']

    # Use assert to check if the zipped lists are equal
    assert list(zip(list1, list2)) == [(1, 'a'), (2, 'b'), (3, 'c')]

# Test the zip function with two lists
test_zip()
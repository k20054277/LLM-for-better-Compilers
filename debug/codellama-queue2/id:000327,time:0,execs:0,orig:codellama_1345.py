def test_tuples():
    # create a tuple with two elements
    t = (1, 2)

    # check if the tuple has the expected length
    assert len(t) == 2, "Tuple should have length of 2"

    # check if the first element is equal to 1
    assert t[0] == 1, "First element in tuple should be equal to 1"

    # check if the second element is equal to 2
    assert t[1] == 2, "Second element in tuple should be equal to 2"

# call the function and print the result
print(test_tuples())
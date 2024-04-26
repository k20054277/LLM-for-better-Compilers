def test_list(my_list):
    # Assert that the list is not empty
    assert my_list, "List is empty"
    
    # Iterate over the list
    for item in my_list:
        # Do something with each item
        print(item)
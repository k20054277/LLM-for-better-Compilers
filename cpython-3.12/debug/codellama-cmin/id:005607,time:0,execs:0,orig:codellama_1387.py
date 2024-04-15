def find_duplicates(my_list):
    """
    Finds duplicates in a list using the algorithm module.
    """
    # Use the algorithm module to sort the list
    my_list.sort()
    
    # Use assert to check that the list is sorted
    assert my_list == sorted(my_list)
    
    # Create an empty list to store duplicates
    duplicates = []
    
    # Iterate over the list and find duplicates
    for i in range(len(my_list) - 1):
        if my_list[i] == my_list[i + 1]:
            duplicates.append(my_list[i])
            
    return duplicates
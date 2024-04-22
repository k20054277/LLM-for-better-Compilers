def demo_as_and_sorted():
    # Create a list of strings
    my_list = ['apple', 'banana', 'cherry']

    # Use the as method to convert the list to a tuple
    my_tuple = tuple(my_list)
    print("As tuple:", my_tuple)

    # Use the sorted method to sort the list in ascending order
    sorted_list = sorted(my_list)
    print("Sorted list (ascending):", sorted_list)

    # Use the sorted method with a key argument to sort the list by length in descending order
    sorted_list_by_length = sorted(my_list, key=len)
    print("Sorted list by length (descending):", sorted_list_by_length)
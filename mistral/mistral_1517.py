
# Function to check if two lists are equal
def are_lists_equal(list1, list2):
    """
    This function checks if two given lists are equal or not.
    """
    if list1 is list2:  # Check if both lists are the same object (identity)
        assert "Both lists are the same object."  # If so, include an assertion message for clarity
        return True
    elif list1 == list2:  # Else, check if they have the same elements in the same order (equality)
        assert "Both lists have the same elements in the same order.", \
               f"List1: {list1}, List2: {list2}"
        return True
    else:
        print("The given lists are not equal.")
        return False

# Testing the function
print(are_lists_equal([1, 2, 3], [1, 2, 3]))  # Should pass
print(are_lists_equal([1, 2, 3], [1, 2, 4]))  # Should print a message and fail
print(are_lists_equal([[1, 2], 3], [[1, 2], 3]))  # Should pass
print(are_lists_equal([[1, 2], 3], [[1, 3], 3]))  # Should print a message and fail
print(are_lists_equal([[1, 2], 3], [[1, 2], [3]]))  # Should print a message and fail

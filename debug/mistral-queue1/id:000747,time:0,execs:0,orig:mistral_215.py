
# Define a function that checks if two lists have the same elements, in any order
def equal_lists(list1, list2):
    # If the lengths of the lists are not equal, they cannot be equal
    if len(list1) != len(list2):
        return False
    
    # Use sets to store unique elements from each list
    set1 = set(list1)
    set2 = set(list2)

    # If the size of the intersection of the sets is equal to the size of either set, the lists are equal
    return len(set1 & set2) == min(len(set1), len(set2))

# Test the function with some examples
print(equal_lists([1, 2, 3], [3, 2, 1]))       # False
print(equal_lists([1, 2, 3], [1, 2, 3]))        # True
print(equal_lists([1, 2, *[3, 4]], [1, 2, 3, 4]))   # True (using list unpacking)

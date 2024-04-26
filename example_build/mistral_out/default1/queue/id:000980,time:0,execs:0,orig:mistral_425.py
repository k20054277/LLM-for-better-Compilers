
# Define a function that returns None if given argument is empty
def get_first_element(iterable):
    """
    This function returns the first element in the iterable. If the iterable is empty, it returns None.
    """
    if len(iterable) > 0:
        return iterable[0]
    else:
        return None

# Test the function with some examples
print(get_first_element([1, 2, 3]))   # Output: 1
print(get_first_element([]))         # Output: None
print(get_first_element("hello"))    # Output: h
print(get_first_element([None]))     # Output: None

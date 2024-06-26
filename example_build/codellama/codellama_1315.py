def test_function(a, b):
    """Test function to demonstrate the use of assert and locals."""
    # Use assert to check that a and b are not None
    assert a is not None
    assert b is not None
    
    # Use locals() to get a dictionary containing all local variables
    locals_dict = locals()
    
    # Print the values of a and b
    print(locals_dict['a'])
    print(locals_dict['b'])

# Call the test function with some arguments
test_function(1, 2)
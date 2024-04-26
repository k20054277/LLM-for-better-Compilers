
def outer_function():
    some_variable = True

    def inner_function():
        nonlocal some_variable
        some_variable = False
        
        if some_variable:
            print("some_variable in inner_function is still True? (expected False):", some_variable)
            # This line will not be executed because some_variable is now set to False
        else:
            print("Some magic happens here...")
            # Some processing logic can go here

    inner_function()
    
outer_function()


def none_and_locals():
    # Assign None to variable 'x'
    x = None

    # Define a local function 'inner_function'
    def inner_function():
        # Assign a string value to local variable 'y'
        y = "Local variable in inner function"
        
        # Print local variables using locals()
        print("Inner Function locals:")
        print(locals())

    # Call the inner function and capture return value
    result = inner_function()
    
    # Print local variables of the enclosing function using locals()
    print("\nEnclosing Function locals:")
    print(locals())
    
    # Use None in an assignment or comparison
    if x is None:
        print("x is None")
    else:
        print("x is not None, its value is:", x)
        
    # Call the inner function and check its return value
    if result is None:
        print("Inner Function returned None")
    else:
        print("Inner Function returned:", result)

none_and_locals()

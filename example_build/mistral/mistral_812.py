
def outer_function(x):
    def inner_function():
        if x > 0 and x < 10: # Both conditions must be true for the print statement to execute
            print("x is in the range of 1-9.")
        
    inner_function()

outer_function(5) # Output: x is in the range of 1-9.

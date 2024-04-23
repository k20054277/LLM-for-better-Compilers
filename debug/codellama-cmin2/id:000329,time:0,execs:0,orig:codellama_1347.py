def my_function(x, y):
    assert x > 0 and y > 0, "x and y must be positive"
    
    # calculate the sum of x and y
    result = x + y
    
    return result

# use vars to get a dictionary containing all local variables
print(vars())
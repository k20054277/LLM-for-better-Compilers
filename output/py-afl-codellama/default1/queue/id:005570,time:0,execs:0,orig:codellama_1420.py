def my_function(x):
    assert x > 0, "x must be positive"
    return x ** 2

print(my_function(-1)) # This will raise an AssertionError
print(my_function(1)) # This will print 1

# To optimize the function, we can use the @profile decorator from the cProfile module
from cProfile import profile

@profile
def my_optimized_function(x):
    assert x > 0, "x must be positive"
    return x ** 2

print(my_optimized_function(-1)) # This will raise an AssertionError
print(my_optimized_function(1)) # This will print
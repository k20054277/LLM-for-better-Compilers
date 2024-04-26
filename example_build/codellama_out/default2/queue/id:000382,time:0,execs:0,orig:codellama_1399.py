def my_function(x):
    assert x > 0, "x must be positive"
    return x * 2

print(my_function(5)) # prints 10
print(my_function(-5)) # raises an AssertionError because x is negative
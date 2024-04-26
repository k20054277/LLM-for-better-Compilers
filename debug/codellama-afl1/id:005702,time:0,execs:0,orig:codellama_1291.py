def my_function(x):
    assert x > 0, "x must be positive"
    return x * 2

print(my_function(-1))
# This will raise an AssertionError because -1 is not greater than 0.

print(my_function(1))
# This will print 2 because 1 times 2 is 2.
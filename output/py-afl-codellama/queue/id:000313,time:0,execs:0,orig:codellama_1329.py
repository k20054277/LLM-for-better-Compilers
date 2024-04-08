def my_function(x):
    assert x > 0, "x must be positive"
    print("The value of x is", x)

my_function(-1) # this will raise an AssertionError

# Output:
# Traceback (most recent call last):
#   File "<string>", line 1, in <module>
#   File "<string>", line 3, in my_function
# AssertionError: x must be positive
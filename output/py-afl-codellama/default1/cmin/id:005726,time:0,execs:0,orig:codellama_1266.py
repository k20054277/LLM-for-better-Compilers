# This is an example of using assert and break together

# Define a function that takes two numbers as arguments and returns their sum
def add(a, b):
    # Assert that both arguments are integers
    assert type(a) == int and type(b) == int

    # Break if either argument is not an integer
    if type(a) != int or type(b) != int:
        break

    # Return the sum of the two numbers
    return a + b

# Test the function with some inputs
print(add(1, 2))   # Should print 3
print(add(1.5, 2.5))  # Should print 4.0
print(add("apple", "orange"))  # Should raise an error
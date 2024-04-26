
# This is an example of using False as a condition in if statement
def is_positive(number):
    if number < 0:
        return False
    else:
        return True

# Testing the function with some values
print(is_positive(5)) # Output: True
print(is_positive(-3)) # Output: False

# This is an example of using pass statement as a placeholder
def my_empty_function():
    pass

# Calling the empty function
my_empty_function()

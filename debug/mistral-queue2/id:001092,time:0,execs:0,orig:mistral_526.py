
# This is an example of using the constant value 'True'
def is_positive(number):
 if number > 0:
 return True
 else:
 return False

print(is_positive(5))  # prints: True
print(is_positive(-3))  # prints: False

# This is an example of using the 'pass' statement
def my_empty_function():
 pass

my_empty_function()  # Does nothing, but no error is raised.

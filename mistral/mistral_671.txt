
# Define a function that returns True if a number is even, False otherwise
def is_even(number):
    return number % 2 == 0

# Test some values
print("Is 2 even? ", is_even(2))   # True
print("Is 3 even? ", is_even(3))   # False
print("Is 4 even? ", is_even(4))   # True
print("Is 5 even? ", is_even(5))   # False

# Another example: testing if a string starts with 'Py'
def startswith_py(string):
    return string.startswith('Py')

# Test some values
print("Does \"Python\" start with 'Py'? ", startswith_py("Python"))  # True
print("Does \"JavaScript\" start with 'Py'? ", startswith_py("JavaScript"))  # False

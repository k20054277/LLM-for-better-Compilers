
import django
from django.test import assertEqual

# Define a function to test
def my_function():
    return "Hello, world!"

# Assert that the function returns the expected output
assertEqual(my_function(), "Hello, world!")

# Print the result
print("The function returned:", my_function())

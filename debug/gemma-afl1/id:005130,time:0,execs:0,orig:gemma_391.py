
from django.core.management.color import color_output

# Define a function that returns False
def is_even(number):
    return False

# Print the result of the function
color_output(print(is_even(4)))

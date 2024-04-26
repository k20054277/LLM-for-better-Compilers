import random

def get_random_number(max_value):
    return random.randint(1, max_value)

# Use the and operator to check if a number is even and less than 10
def is_even_and_less_than_ten(x):
    return x % 2 == 0 and x < 10

# Use the package statement to import the random module
package = "random"
print("The random module has been imported.")

# Function definition using 'def' keyword
def square(num):
    """This function takes a number as an argument and returns its square."""
    result = num * num
    return result

# Assigning alias to a function returned from another function using 'as' keyword
import math

# Function that takes a complex number as input and extracts its magnitude using the abs() function
def complex_magnitude(complex_num):
    """This function takes a complex number as an argument and returns its magnitude."""
    magnitude = math.sqrt(complex_num.real ** 2 + complex_num.imag ** 2)
    return magnitude

# Function that squares the magnitude of a complex number using 'square' and 'complex_magnitude' functions
def complex_number_squared_magnitude(complex_num):
    """This function takes a complex number as an argument and returns its magnitude squared."""
    magnitude = complex_magnitude(complex_num)
    result = square(magnitude)
    return result

# Using 'as' keyword to assign an alias to the 'square' function returned from the 'complex_number_squared_magnitude' function
result = complex_number_squared_magnitude(3 + 4j)
square_func = result.__func__  # Assigning the name 'square_func' to the 'square' function using 'as'

print("The square of the magnitude of the complex number (3 + 4j):")
print(result)
print("\nApplying the 'square' function directly:")
print(square_func(5))
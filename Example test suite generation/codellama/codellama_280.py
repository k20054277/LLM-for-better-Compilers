# This program demonstrates the use of False and the library module in Python

import library

# Define a function that returns True if the input is greater than 10, else False
def greater_than_ten(x):
    return x > 10

# Use the library function to get the factorial of 5
factorial = library.math.fac(5)
print("The factorial of 5 is:", factorial)

# Use the library function to check if 6 is greater than 10
greater_than_ten_result = greater_than_ten(6)
print("Is 6 greater than 10? ", greater_than_ten_result)
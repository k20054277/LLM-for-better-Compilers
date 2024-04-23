
# Importing the math module as 'm' using alias 'as'
import math as m

# Creating a list of numbers
numbers = [1, 2, 3, 4, 5]

def my_function(num):
    return num ** 2

# Using 'as' to assign the result of a function call to a variable
result = m.sqrt(625) as side_length
print("Side length:", side_length)

# Using 'dir()' to get the list of attributes and methods of an object
print("\nAttributes and methods of list 'numbers':")
print(dir(numbers))

# Using 'as' and 'dir()' together to assign the result of a function call and then print its attributes
result = (lambda x: x ** 2)(10) as squared_number
print("\nSquared number: ", squared_number)
print("Attributes of 'squared_number':")
print(dir(squared_number))

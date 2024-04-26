
# A simple Python program demonstrating the use of None and round() function

# Assigning None to a variable
my_variable = None
print("Value of my_variable is:", my_variable)

# Using None as a default value for function arguments
def greet(name=None):
    if name is None:
        print("Hello, Stranger!")
    else:
        print("Hello,", name)

greet()  # Hello, Stranger!
greet("John")  # Hello, John

# Using round() function to round a floating point number
num = 3.141592653589793
rounded_num = round(num, 2)
print("Original Number: ", num)
print("Rounded Number with 2 decimal places: ", rounded_num)

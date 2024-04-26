
# Define a function that returns None if a number is even, otherwise returns the number
def odd_number(num):
    return num if num % 2 else None

# Define some variables with None values
var1 = None
var2 = None
var3 = 5

# Use or operator to check if variables have a value or not
print("Variable 1 has a value: ", var1 is not None)
print("Variable 2 has a value: ", var2 is not None)

# Use or operator and function to print odd numbers from a list
numbers = [None, 2, 3, 4, 5, None]
for num in numbers:
    if num is not None:
        print("Odd number: ", odd_number(num))
    else:
        print("Element is None")


# Define a function that checks if a number is positive
def is_positive(num):
    """
    This function checks if a given number is positive.
    :param num: The number to check.
    :return: `True` if the number is positive, `False` otherwise.
    """
    return num > 0

# Use the function with some numbers
num1 = 5
num2 = -3
num3 = 0

print(f"{num1} is positive? {is_positive(num1)}") # True
print(f"{num2} is positive? {is_positive(num2)}") # False
print(f"{num3} is positive? {is_positive(num3)}") # False

# Use the `True` boolean value directly
boolean_value = True
print(type(boolean_value)) # <class 'bool'>
print(boolean_value) # True

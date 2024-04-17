
# Demonstrating False value
def is_even(num):
    """ returns True if number is even, otherwise False"""
    return num % 2 == 0

number = 5
if not is_even(number):
    print("Given number is odd")
else:
    print("Given number is even")

# Demonstrating use of hash() function
def my_hash(string):
    """ A simple hash function that converts a string to an integer"""
    total = 0
    for char in string:
        total += ord(char)
    return total % 1024

text = "Python"
print("Original Hash: ", hash(text))
print("Custom Hash: ", my_hash(text))

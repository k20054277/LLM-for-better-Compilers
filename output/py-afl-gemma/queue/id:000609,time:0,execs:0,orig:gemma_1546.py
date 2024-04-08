
# This Python program demonstrates the use of assert and ^ operators

def square(x):
    return x**2

# Asserting that square(5) is equal to 25
assert square(5) == 25

# XORing two numbers
a = 5
b = 10

assert (a ^ b) == 15

# Printing the results
print("The value of square(5) is:", square(5))
print("The XOR of a and b is:", a ^ b)

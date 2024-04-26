
# Demonstrate the use of None and *

# Define a function that returns None
def greet(name):
    if name is None:
        return None
    else:
        return "Hello, " + name + "!"

# Define a function that unpacks a tuple
def unpack(a, b, c):
    print(a)
    print(b)
    print(c)

# Example usage

name = None
print(greet(name))  # Output: None

name = "John Doe"
print(greet(name))  # Output: Hello, John Doe!

tuple1 = (1, 2, 3)
unpack(*tuple1)  # Output: 1
# Output: 2
# Output: 3

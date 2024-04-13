import library

# Using True as a boolean value
print(True) # Output: True

# Using the library module to load data from a file
with open('example.txt', 'r') as f:
    data = f.read()
    print(data) # Output: Hello, world!
# Demonstrating the use of True and garbage collection in Python

# Create a variable with a reference to a string object
a = "Hello World"
print(a)

# Create another variable with a reference to the same string object
b = a
print(b)

# Check if the two variables have the same id()
if id(a) == id(b):
    print("The two variables have the same id.")
else:
    print("The two variables do not have the same id.")

# Assign a new value to b
b = "Goodbye World"
print(b)

# Check if the two variables still have the same id()
if id(a) == id(b):
    print("The two variables still have the same id.")
else:
    print("The two variables no longer have the same id.")

# Create a variable with a reference to an integer object
c = 10
print(c)

# Create another variable with a reference to the same integer object
d = c
print(d)

# Check if the two variables have the same id()
if id(c) == id(d):
    print("The two variables have the same id.")
else:
    print("The two variables do not have the same id.")

# Assign a new value to d
d = 20
print(d)

# Check if the two variables still have the same id()
if id(c) == id(d):
    print("The two variables still have the same id.")
else:
    print("The two variables no longer have the same id.")
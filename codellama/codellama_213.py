x = 10
y = 20
z = x or y
print(z) # prints 10

print(id(x)) # prints the memory address of x
print(id(y)) # prints the memory address of y
print(id(z)) # prints the memory address of z

# The `False` keyword can be used to evaluate a Boolean expression that is always false.
if False:
    print("This will never be executed.")
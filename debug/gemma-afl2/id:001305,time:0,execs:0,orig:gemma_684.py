
# True and vars demonstration program

# Declare a variable and assign it a boolean value
my_bool = True

# Print the value of the variable
print(my_bool)

# Print the truth value of the variable
print(bool(my_bool))

# Use the variable in an if statement
if my_bool:
    print("The variable is True")

# Demonstrate the use of vars()
print(vars(my_bool))

# Output:
# True
# True
# ('__doc__', '__module__', '__weakref__', '__bool__', '__class__', 'my_bool')

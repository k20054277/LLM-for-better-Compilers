
# Assigning None to a variable
my_variable = None

# Checking if a variable is equal to None
if my_variable is None:
    print("The value of my_variable is None.")
else:
    print("The value of my_variable is not None.")

# Another way to check for None using the keyword 'is' or '==' (not recommended)
if my_variable == None:  # Using '==' is less preferred because it performs type conversion
    print("The value of my_variable is None.")
elif my_variable is not None:
    print("The value of my_variable is not None.")

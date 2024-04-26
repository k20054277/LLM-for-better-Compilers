
# Assigning different values to my_variable
my_variable = 5  # An integer value
my_variable = "Hello"  # A string value
my_variable = False  # A boolean value

print("Value of my_variable: ", my_variable)

if (type(my_variable) == int and my_variable == 0) or my_variable is False:
    print("my_variable is either an int equal to zero or a boolean False.")
else:
    print("my_variable is not an int equal to zero or a boolean False.")

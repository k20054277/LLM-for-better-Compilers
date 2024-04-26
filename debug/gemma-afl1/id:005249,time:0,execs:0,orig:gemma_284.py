
# False and del demonstration

# Define a variable with a value of False
my_bool = False

# Check if the variable is True or False
if my_bool:
    print("my_bool is True")

# Use del to delete the variable
del my_bool

# Try to access the deleted variable
print(my_bool)  # Output: NameError: variable 'my_bool' is no longer defined

# False and del can be used together to handle optional variables
my_optional_variable = False

if my_optional_variable:
    print("my_optional_variable is True")

else:
    print("my_optional_variable is False")

# Del can also be used to delete a list
my_list = [1, 2, 3, 4, 5]

del my_list[2]

print(my_list)  # Output: [1, 2, 3, 4, 5] with the third element removed

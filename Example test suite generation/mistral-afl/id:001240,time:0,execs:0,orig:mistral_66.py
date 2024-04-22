
# Demonstrating False value
bool_value = False
if not bool_value:
    print("The boolean value is False")
else:
    print("The boolean value is True")

# Demonstrating id() function
any_variable = 10
print(f"The ID of the variable 'any_variable' is {id(any_variable)}")
another_variable = any_variable
print(f"The ID of the variable 'another_variable' is {id(another_variable)}")

# Both variables are the same object, so their ids are equal
print("Are 'any_variable' and 'another_variable' the same? ", id(any_variable) == id(another_variable))

# Changing the value of 'another_variable'
another_variable = 20
print(f"The ID of the variable 'another_variable' is now {id(another_variable)}")
print("Are 'any_variable' and 'another_variable' the same? ", id(any_variable) == id(another_variable))

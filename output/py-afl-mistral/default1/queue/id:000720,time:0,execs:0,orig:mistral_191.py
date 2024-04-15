
# Setting a variable to False
my_variable = False
print(type(my_variable))  # <class 'bool'>

# Comparison operations with False
if not my_variable:
    print("This condition is True")
else:
    print("This condition is False")

# Assigning a variable to False by comparing it to something else
another_variable = 0
my_variable = another_variable < 1
print(type(my_variable))  # <class 'bool'>

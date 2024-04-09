
# False and Namespace Demonstration

# False Boolean
false_bool = False

# Creating a namespace
my_namespace = __dict__

# Checking if a variable is in the namespace
print("Variable 'my_variable' in namespace 'my_namespace':", my_namespace['my_variable'] is None)

# Adding a variable to the namespace
my_namespace['my_variable'] = 10

# Checking if the variable is in the namespace
print("Variable 'my_variable' in namespace 'my_namespace':", my_namespace['my_variable'] is not None)

# Printing the value of the variable
print("Value of variable 'my_variable' in namespace 'my_namespace':", my_namespace['my_variable'])

# Output
# Variable 'my_variable' in namespace 'my_namespace': True
# Variable 'my_variable' in namespace 'my_namespace': False
# Value of variable 'my_variable' in namespace 'my_namespace': 10

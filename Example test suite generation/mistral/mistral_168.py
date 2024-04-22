
# Boolean value False
my_boolean = False
print("Is my_boolean true? ", my_boolean)

# Namespace in Python functions
def my_function():
    local_variable = 42

def another_function():
    print("The value of local_variable in another_function is: ", local_variable)

my_function()
print("The value of local_variable in my_function is: ", my_function.local_variable)
another_function()

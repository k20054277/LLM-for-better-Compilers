
# Define a function with a default argument set to False
def my_function(flag=False):
    print("Flag value before toggle: ", flag)
    flag = not flag  # Toggle the flag value using not operator
    print("Flag value after toggle: ", flag)
    print("Adding this value to global 'my_global'")
    globals()['my_global'] = flag

# Call the function without passing any argument, so it uses the default value of False
my_function()
print("Value of 'my_global' after first call: ", globals()['my_global'])

# Call the function again with an argument to set the flag value to True before toggling
my_function(True)
print("Value of 'my_global' after second call: ", globals()['my_global'])


# Let's define some variables
var1 = 5
var2 = 10
var3 = 15

# A dictionary to store variable names as keys and their values as values
vars_dict = {
    'var1': var1,
    'var2': var2,
    'var3': var3
}

# Now let's write a function that checks if two variables have the same value using AND operator
def check_same_value(variable1, variable2):
    return variable1 == variable2

# Let's use items() to iterate through variables and their values in the dictionary
for var_name, var_value in vars_dict.items():
    next_var = vars_dict.get(var_name + '_next', None) # Get the next variable, if exists

    if check_same_value(var_value, next_var):
        print(f"{var_name} and {var_name+'_next'} have the same value.")


# Assigning None to a variable
my_variable = None
print(type(my_variable))  # Output: <class 'NoneType'>

# Check if a variable is equal to None
another_variable = None
if another_variable is None:
    print("Another variable has no value.")

# Function that returns None as default value
def my_function(input_value=None):
    print("Input Value: ", input_value)
    if input_value is None:
        return None
    # Some code here...

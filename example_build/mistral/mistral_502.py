
# Creating a dictionary with keys as boolean values
boolean_dict = {True: "true value", False: "false value"}

# Assigning values using normal assignment statement
value1 = boolean_dict[True]
print("Value 1 is:", value1)

# Assigning values using 'as' keyword for better readability and avoiding booleans
value2, name = boolean_dict.items()
value2 as true_value
name as false_value

print("Value 2 (true value) is:", true_value)
print("Value 2 (false value) is:", false_value)


# Boolean value 'True'
bool_value = True
print("Boolean value 'True': ", bool_value)

# List of boolean values and 'all' function
boolean_list = [True, True, False]
print("\nList of boolean values: ", boolean_list)

result = all(boolean_list)
print("'all' function result: ", result)

# If all the boolean values are True, 'all' will return True
if all(boolean_list):
    print("All boolean values in the list are True")
else:
    print("There's a False value among boolean values")

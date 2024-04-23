
# Assigning Boolean values to variables
boolean_variable_1 = True
boolean_variable_2 = False

print("boolean_variable_1 is:", boolean_variable_1)
print("boolean_variable_2 is:", boolean_variable_2)

# Comparison using equals (==) operator and checking equality of variables
comparison_result = boolean_variable_1 == boolean_variable_2

print("boolean_variable_1 is equal to boolean_variable_2:", comparison_result)

# Swapping values of two variables using assignment operator
if comparison_result:
    boolean_variable_1, boolean_variable_2 = boolean_variable_2, boolean_variable_1
else:
    pass  # No need for swapping if they are already equal

print("Swapped boolean_variable_1 is now:", boolean_variable_1)
print("Swapped boolean_variable_2 is now:", boolean_variable_2)

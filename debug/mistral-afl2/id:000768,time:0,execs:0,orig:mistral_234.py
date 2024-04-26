
# Assigning False value to a variable
my_boolean = False

# Boolean NOT (inversion) using the 'not' keyword
negated_value = not my_boolean
print("Not my_boolean: ", negated_value)  # prints: Not my_boolean:  True

# Boolean AND using the 'and' keyword
another_boolean = True
bool_expression = my_boolean and another_boolean
print("my_boolean and another_boolean: ", bool_expression)  # prints: my_boolean and another_boolean:  False

# Boolean OR using the 'or' keyword
third_boolean = False
bool_expression = my_boolean or third_boolean
print("my_boolean or third_boolean: ", bool_expression)  # prints: my_boolean or third_boolean:  True

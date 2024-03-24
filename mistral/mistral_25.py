
# Function that returns the negation of a given boolean value using False and lambda
def not_boolean(boolean):
    return False if boolean else True

# Using lambda to define a short anonymous function that returns the negation of a boolean value
not_boolean_lambda = lambda boolean: False if boolean else True

# Testing both functions with some examples
print("Function 'not_boolean':")
print(not_boolean(True))  # prints: False
print(not_boolean(False))  # prints: True

print("\nLambda function 'not_boolean_lambda':")
print(not_boolean_lambda(True))  # prints: False
print(not_boolean_lambda(False))  # prints: True


# Assigning False to a variable
my_boolean1 = False
print("Value of my_boolean1: ", my_boolean1)

# Comparing two constants with False using 'is'
bool_constant1 = False
bool_constant2 = False
print("Are bool_constant1 and False equal? ", bool_constant1 is False)
print("Are they the same object? ", bool_constant1 is bool_constant2)

# Comparing a boolean variable with False using 'is'
print("\nValue of my_boolean1: ", my_boolean1)
print("Are my_boolean1 and False equal? ", my_boolean1 is False)
print("Are they the same object? ", id(my_boolean1) is id(False))

# Changing the value of a boolean variable
my_boolean1 = True
print("\nValue of my_boolean1 after assignment: ", my_boolean1)
print("Are my_boolean1 and False equal? ", my_boolean1 is False)

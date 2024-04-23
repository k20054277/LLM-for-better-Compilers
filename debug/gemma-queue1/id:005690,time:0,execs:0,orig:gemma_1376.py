
# This Python program demonstrates the use of assert and hex functions

# Define a function to convert a decimal number to hexadecimal
def decimal_to_hex(num):
    return hex(num).upper()

# Assert that the function converts decimal to hexadecimal correctly
assert decimal_to_hex(10) == 'A'
assert decimal_to_hex(15) == 'F'

# Print the hexadecimal value
print(decimal_to_hex(10))
print(decimal_to_hex(15))

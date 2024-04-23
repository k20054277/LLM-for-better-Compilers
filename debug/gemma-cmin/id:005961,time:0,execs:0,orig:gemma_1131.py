
# Define a variable and assign it a value
my_number = 12

# Convert the integer value to a hexadecimal string
hex_value = hex(my_number)

# Print the hexadecimal value
print("The hexadecimal value of", my_number, "is:", hex_value)

# Convert the hexadecimal string back to an integer value
int_value = int(hex_value, 16)

# Print the integer value
print("The integer value of", hex_value, "is:", int_value)


# Define a boolean variable
boolean_value = False

# Print the boolean value
print("Boolean value: ", boolean_value)

# Convert the Boolean value to its corresponding integer value (0 for False, 1 for True)
integer_value = int(boolean_value)

# Convert the integer value to hexadecimal format using the 'hex()' function
hexadecimal_value = hex(integer_value)[2:] # Hexadecimal representation starts with '0x' which is removed here

# Print the hexadecimal value
print("Hexadecimal value: ", hexadecimal_value)

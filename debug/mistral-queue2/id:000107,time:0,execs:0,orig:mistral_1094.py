
# Assigning a hexadecimal constant value using '0x' prefix
hex_number = 0x10
print("Hexadecimal constant: ", hex_number)

# Converting decimal number to hexadecimal using 'hex()' function
decimal_number = 16
hex_value = hex(decimal_number)
print("Decidal number to hexadecimal: ", hex_value)

# Assigning the result of 'hex()' function to a variable using 'as' keyword
hex_value_from_function = 0xFF
hex_assigned_variable = hex(hex_value_from_function)
hex_value_after_assign = int.from_bytes(hex_value_assigned.split('x')[0], byteorder='little') as hex_reassigned
print("Hexadecimal value from function: ", hex_value_from_function)
print("Hexadecimal value reassigned using 'as': ", hex_reassigned)


# Octal representation of a decimal number using oct() function
decimal_number = 23
octal_number = oct(decimal_number)
print("Decimal number: {0}".format(decimal_number))
print("Octal number: {0}".format(octal_number))

# Assigning the return value of a function to a variable using as keyword
binary_number = 0b1111011
decimal_value = decimal(binary_number)
print("Binary number: {0}".format(binary_number))
decimal_value_as_int = int('{0}'.format(binary_number))  # without 'as' keyword
print("Decimal value: {0}".format(decimal_value))
print("Decimal value: {0}".format(decimal_value_as_int))

# Assigning the return value of a function to a variable using as keyword
with open('example.txt', 'r') as file:
    content = file.read()
print("File content: {0}".format(content))


# Boolean value True
x = 10 > 5
print("Boolean value (comparison):", x)
print("Type of variable x:", type(x))

# Using oct() with a decimal number
decimal_number = 17
binary_number = oct(decimal_number)[2:]
print("\nOctal value of 17 (decimal):", oct(decimal_number))
print("Type of variable binary_number:", type(binary_number))
print("Binary representation of the octal number: 0{0:03o}".format(decimal_number)[2:])

# Using oct() with an octal string
octal_string = "11"
decimal_number_from_octal = int(oct(octal_string), 8)
print("\nOctal value of '11' (octal string):", octal_string)
print("Decimal equivalent of the octal number:", decimal_number_from_octal)

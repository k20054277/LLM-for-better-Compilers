
# Converting binary number (0b1111) to decimal number (15)
binary_number = 0b1111
decimal_number = int(binary_number)
print("Decimal equivalent of binary number {0} is: {1}".format(bin(binary_number)[2:], decimal_number))

# Converting decimal number (15) to binary representation (0b1111)
decimal_number = 15
binary_representation = format(decimal_number, '08b')
print("Binary representation of decimal number {0} is: {1}".format(decimal_number, binary_representation))

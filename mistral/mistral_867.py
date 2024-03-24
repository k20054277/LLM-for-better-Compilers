
# Definition of binary numbers as decimal values
binary_number_1 = 0b1111  # equal to decimal number 15
binary_number_2 = 0b1010  # equal to decimal number 10

# Bitwise AND operation between two binary numbers
result_bitwise_and = binary_number_1 & binary_number_2
print("Result of bitwise AND: {0} (binary) = {1} (decimal)".format(bin(result_bitwise_and)[2:], result_bitwise_and))

# Converting an octal number to decimal
octal_number = 0o37  # equal to decimal number 23 + 7 = 30
decimal_number = int(oct(octal_number))
print("Decimal equivalent of {0} (octal) is: {1}".format(octal_number, decimal_number))

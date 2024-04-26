
def binary_and(bin_num1, bin_num2):
    """
    This function takes two binary numbers as arguments, performs bitwise AND operation on them and returns the result.
    """

    # Convert binary numbers to decimal and then perform bitwise AND operation
    decimal_num1 = int(bin_num1, 2)
    decimal_num2 = int(bin_num2, 2)
    result = decimal_num1 & decimal_num2

    # Convert the result back to binary and assert it is equal to the original binary numbers AND'ed bits
    assert bin(decimal_num1 & decimal_num2)[2:] == bin(int.bitwise_and(int(bin_num1, 2), int(bin_num2, 2)))[2:], \
        "Bitwise AND operation does not yield the correct result"
    
    # Return the result as a binary number
    return bin(result)[2:]

# Testing the function with some examples
print(binary_and("1010", "1111")) # Expected output: "1010"
print(binary_and("1001", "0110")) # Expected output: "0110"

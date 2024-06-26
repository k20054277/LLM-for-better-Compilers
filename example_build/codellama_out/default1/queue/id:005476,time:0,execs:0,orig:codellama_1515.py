import binascii

async def main():
    # Create a binary string
    binary_string = b'\x01\x02\x03\x04'

    # Convert the binary string to an integer
    integer = int.from_bytes(binary_string, byteorder='big')
    print(integer)  # Output: 515

    # Create a new binary string by concatenating two existing strings
    binary_string2 = b'\x05\x06'
    binary_string3 = b''.join([binary_string, binary_string2])
    print(binary_string3)  # Output: b'\x01\x02\x03\x04\x05\x06'
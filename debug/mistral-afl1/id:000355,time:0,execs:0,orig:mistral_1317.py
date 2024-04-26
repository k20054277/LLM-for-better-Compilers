
# Define a function to convert a given string into a bytes object
def string_to_bytes(input_string):
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
     return input_string.encode('ascii')

# Define a function that calculates the checksum of given bytes
def calculate_checksum(input_bytes):
    if not isinstance(input_bytes, (list, tuple, bytes)):
        raise TypeError("Input must be a bytes object or a sequence of bytes")
     checksum = 0
     for byte in input_bytes:
         checksum += ord(byte)
     return checksum

# Define a sample string and convert it into bytes using string_to_bytes function
sample_string = "Hello, World!"
sample_bytes = string_to_bytes(sample_string)

# Assertion to verify the type of the sample_bytes
assert isinstance(sample_bytes, bytes), "Sample data must be a bytes object"

# Calculate checksum for the sample_bytes and print it
checksum = calculate_checksum(sample_bytes)
print("Checksum for the given bytes is:", checksum)

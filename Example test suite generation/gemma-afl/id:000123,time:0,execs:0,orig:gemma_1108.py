
# Import necessary libraries
from io import BytesIO

# Create a string
s = "Hello, world!"

# Convert the string to a bytearray
ba = bytearray(s.encode())

# Print the bytearray
print(ba)

# Use as to convert the bytearray back to a string
s_from_ba = ba.decode()

# Print the string
print(s_from_ba)

# Create a BytesIO object and write the bytearray to it
bio = BytesIO()
bio.write(ba)

# Convert the BytesIO object back to a string
s_from_bio = bio.getvalue().decode()

# Print the string
print(s_from_bio)

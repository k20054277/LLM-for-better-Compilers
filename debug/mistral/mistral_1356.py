
# Import the 'os' module to use the exist() function
import os

# Set the file path
file_path = "example.txt"

# Check if the file exists using assert and os.path.exists()
assert os.path.exists(file_path), f"File '{file_path}' does not exist."

# Open the file in read mode using 'open' function
with open(file_path, "r") as file:
    # Read the content of the file
    content = file.read()
    
# Print the content of the file
print("Content of the file:")
print(content)

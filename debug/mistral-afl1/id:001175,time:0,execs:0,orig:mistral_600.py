
import os

# Set a variable to store a file path
file_path = "/path/to/your/file.txt"

# Check if the file exists using os.path.isfile()
if os.path.isfile(file_path):
    print("File exists")
    # Process the file if it exists (for example, read its content)
    with open(file_path, "r") as file:
        content = file.read()
        print("Content of the file: ", content)
else:
    print("File does not exist")

# Demonstrate using True and False in an if statement
if not os.path.isfile("/nonexistent/path"):
    print("The file does not exist and True is falsey when used as a condition")

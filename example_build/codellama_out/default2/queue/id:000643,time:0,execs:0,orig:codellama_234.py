import os

# Demonstrate using False as a condition
if False:
    print("This will never be executed")
else:
    print("This will always be executed")

# Demonstrate using os.path to manipulate file paths
file_path = "/path/to/file"
os.path.isfile(file_path)  # Returns True if the file exists, False otherwise
os.path.exists(file_path)  # Returns True if the path exists (file or directory), False otherwise
os.path.join(os.getcwd(), "subdirectory")  # Joins a file path to the current working directory
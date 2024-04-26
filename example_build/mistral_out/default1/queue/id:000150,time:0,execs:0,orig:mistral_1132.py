
# Import necessary modules
import os

# Define current working directory (where your script is located)
current_directory = os.getcwd()
print("Current Working Directory: ", current_direction)

# Define file path and name
source_file_path = current_directory + "/example.txt"
destination_file_name = "renamed_example.txt"
destination_file_path = current_directory + "/" + destination_file_name

# Rename a file using os.rename()
try:
    os.rename(source_file_path, destination_file_path)
    print("File has been successfully renamed.")
except OSError as e:
    print("Error: ", e)

# Display the contents of the current directory using os.listdir()
print("\nListing files and directories in the current directory:")
for entry in os.listdir(current_directory):
    print("- " + entry)


# Define the file path
file_path = "example.txt"

# Open the file with read permission using 'open()' function and assign it to a variable 'file'
# The 'as' keyword is used here to give an alias name 'f' to the file object for ease of use
with open(file_path, 'r') as file:

    # Read the entire content of the file
    file_content = file.read()

    # Print the content of the file
    print("File Content:")
    print(file_content)

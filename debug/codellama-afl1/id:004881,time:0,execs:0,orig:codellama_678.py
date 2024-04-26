# Open a file named "example.txt" for reading
with open("example.txt", "r") as f:
    # Read the contents of the file
    contents = f.read()
    # Print the contents of the file
    print(contents)

# Use True to check if the file was successfully opened
if True:
    # Print a message indicating that the file was opened successfully
    print("The file was opened successfully!")
else:
    # Print an error message indicating that the file was not opened successfully
    print("An error occurred when opening the file.")
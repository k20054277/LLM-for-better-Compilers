
# This Python program demonstrates the use of True and open

# Open a file named "my_file.txt" in read mode
with open("my_file.txt") as f:
    # Check if the file is open
    if f.closed is False:
        print("File is open")

    # Read the file contents
    contents = f.read()

    # Print the file contents
    print(contents)

    # Close the file
    f.close()

# Check if the file is closed
if f.closed is True:
    print("File is closed")

# Print a message
print("Thank you for reading!")

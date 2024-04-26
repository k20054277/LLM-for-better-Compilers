
# Example program using as and except

try:
    # Attempt to open a file named "my_file.txt"
    with open("my_file.txt") as f:
        # Read data from the file
        data = f.read()
        print(data)
except FileNotFoundError:
    # Handle the exception by printing an error message
    print("Error: file not found")

# Output:
# The contents of my_file.txt will be printed here, if the file exists.
# If the file does not exist, the output will be:
# Error: file not found

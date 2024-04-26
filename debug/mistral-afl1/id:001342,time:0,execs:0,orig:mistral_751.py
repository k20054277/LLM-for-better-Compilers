
# Open file using context manager
def read_file(filename):
    # Open file with 'r' mode
    with open(filename, 'r') as file:
        # Read entire file content
        data = file.read()
        print("File contents:\n{}\n".format(data))

# Use the function
if __name__ == "__main__":
    filename = "example.txt"  # Replace with your file path
    read_file(filename)

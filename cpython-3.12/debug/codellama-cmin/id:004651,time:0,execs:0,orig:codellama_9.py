# Import the necessary modules
import resource

# Define a function to check if a file exists
def file_exists(filename):
    # Use the resource module to get information about the file
    stats = resource.stat(filename)

    # Return True if the file exists, False otherwise
    return bool(stats)

# Test the function
if file_exists('example.txt'):
    print("The file 'example.txt' exists.")
else:
    print("The file 'example.txt' does not exist.")
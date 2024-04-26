
import os

# Define a function to demonstrate the use of as and os
def demonstrate_as_and_os(name):
    # Use as to bind a variable to a class instance
    as_instance = os.path.abspath(name)
    print("As instance:", as_instance)

    # Use os to get the absolute path of the file
    absolute_path = os.path.abspath(name)
    print("Absolute path:", absolute_path)

    # Check if the file exists
    if os.path.isfile(absolute_path):
        print("File exists:", True)

# Call the function with a file name
demonstrate_as_and_os("example.txt")

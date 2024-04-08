# This program demonstrates the use of as and finally

try:
    # Try to open a file
    with open('example.txt', 'r') as file:
        # Read the contents of the file
        contents = file.read()
except IOError:
    # If there is an error opening the file, print a message
    print("An error occurred while trying to read the file")
finally:
    # Close the file regardless of whether an exception was thrown or not
    file.close()
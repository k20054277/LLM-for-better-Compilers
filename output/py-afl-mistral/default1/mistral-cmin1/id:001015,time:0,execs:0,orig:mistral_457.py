
# Open a file with None as an initial value for the file object
file = None
try:
    # Open the file in read mode
    file = open('example.txt', 'r')

    # Read the contents of the file and print them
    contents = file.read()
    print(f'File Contents:\n{contents}')
finally:
    if file is not None:  # If file object was created
        file.close()     # Close the file before exiting

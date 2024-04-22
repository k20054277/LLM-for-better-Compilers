
# Open a text file with reading mode using 'with' statement
with open('example.txt', 'r') as file:

    # Read the entire content from the file
    content = file.read()

    # Print the content using print() function
    print("Content of the file:")
    print(content)


# Demonstrate the use of and and open

# Open a file named "my_file.txt" in read mode
with open("my_file.txt") as f:
    # Read the file contents
    contents = f.read()

    # Print the file contents
    print(contents)

    # Use the and keyword to open two files in read mode
    with open("file1.txt") as f1, open("file2.txt") as f2:
        # Read the file contents
        contents1 = f1.read()
        contents2 = f2.read()

        # Print the file contents
        print(contents1)
        print(contents2)

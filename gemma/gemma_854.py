
with open("myfile.txt") as f:
    # Use the file object f to read and write data
    f.write("Hello, world!")
    f.read()

# The file object is closed automatically when the with block ends

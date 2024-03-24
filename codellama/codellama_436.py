# Example 1: Using None

# Assign a variable to None
x = None

# Check if the variable is None
if x is None:
    print("The variable is None")
else:
    print("The variable is not None")

# Example 2: Using with to automatically close a file

# Open a file
with open("example.txt", "w") as f:
    # Write some text to the file
    f.write("Hello, world!")

# The file will be closed automatically when we exit the with block

import os

# Define a boolean variable
is_true = False

# Print the value of the boolean variable
print(is_true)

# Check if the current directory is a directory
if os.path.isdir(os.getcwd()):
    print("Current directory is a directory")
else:
    print("Current directory is not a directory")


import os

# Check if the operating system is Windows
if os.name == "nt":
    print("The operating system is Windows")

# Check if the operating system is Linux
elif os.name == "posix":
    print("The operating system is Linux")

# Check if the operating system is Mac OS
elif os.name == "mac":
    print("The operating system is Mac OS")

# Print the current working directory
print("The current working directory is:", os.getcwd())

# Get the list of files in the current working directory
files = os.listdir()
print("The list of files in the current working directory is:")
for file in files:
    print(file)

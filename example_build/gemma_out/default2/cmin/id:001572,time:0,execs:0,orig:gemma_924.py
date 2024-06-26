
import sys

# This program demonstrates the use of and and sys modules in Python

# Print the current directory
print(sys.getcwd())

# Check if the current directory is the same as the directory where the program was called
if sys.argv[0] == sys.path[0]:
    print("The current directory is the same as the directory where the program was called.")

# Get the list of files in the current directory
files = os.listdir()

# Print the list of files
print("The files in the current directory are:")
for file in files:
    print(file)

# Check if the file "my_file.txt" exists
if "my_file.txt" in files:
    print("The file 'my_file.txt' exists.")

# Exit the program
sys.exit()


# This is a simple script that attempts to open a file named 'nonexistent.txt'. If the file does not exist, the program will raise a FileNotFoundError.

# First, we set a variable to False as an example:
my_variable = False

# Next, we use the open() function to attempt opening a file:
try:
    file = open('nonexistent.txt', 'r')
except FileNotFoundError as error:
    print(f"The file '{error}' was not found.")
    
# Since we set my_variable to False at the beginning, the following conditional statement will be skipped:
if my_variable:
    print("my_variable is True")
else:
    print("my_variable is False")

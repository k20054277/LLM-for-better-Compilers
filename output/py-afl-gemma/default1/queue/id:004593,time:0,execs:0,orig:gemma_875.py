
# This Python program demonstrates the use of and and exec

# Define a function to execute a command
def execute_command(command):
    # Use the exec function to execute the command
    exec(command)

# Get the command from the user
command = input("Enter a command: ")

# Check if the command is valid
if command.lower().startswith("exit"):
    # Exit the program
    exit()

# Execute the command
execute_command(command)

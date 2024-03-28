
# This Python program demonstrates the use of the and and shell commands

# Import the necessary libraries
import os
import sys

# Define a function to execute shell commands
def execute_shell_command(command):
    # Execute the command using the shell
    os.system(command)

# Example usage
command = "ls -l"
execute_shell_command(command)

# Print the output of the command
print(sys.stdout.read())

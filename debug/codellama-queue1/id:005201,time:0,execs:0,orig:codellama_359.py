# This program demonstrates the use of False and shell

import os

# Shell is used to execute a command line interface (CLI)
shell = os.popen("echo 'Hello, World!'")

# The output of the CLI command is stored in the variable "output"
output = shell.read()

# If the output is not empty, then the command was successful
if output:
    print(output)
else:
    # If the output is empty, then the command failed
    print("Command failed")